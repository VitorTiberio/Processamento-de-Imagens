## Autor: Vitor Augusto Tibério - 14658834 - Engenharia Elétrica - EESC/USP
## Aluno de Iniciação Científica - LAVI (Laboratório Avançado de Visão e Imagem)
## Orientador: Prof. Dr. Marcelo Andrade da Costa Vieira
## Código que faz a geração da interface de classificação de imagens usando o modelo treinado para distinguir pacientes PD e CR, com base nas features extraídas das imagens médicas. 
# A interface é feita usando Streamlit, permitindo que usuários façam upload de imagens e máscaras para obter a classificação.

## Como ativar a interface: 
## Configurando a Interface Streamlit -- para startar o sistema, basta rodar este arquivo (interface.py) com o comando: streamlit run interface.py no CMD, estando na pasta onde o arquivo se encontra. !!!
## Para estar na pasta que o arqvuivo se encontra, use o comando: cd C:\Users\lavi\Desktop\interface_fmusp !!!

import streamlit as st
import numpy as np
import joblib
import SimpleITK as sitk
from radiomics import featureextractor
import tempfile
import os

## Configurações de caminhos e features
# O 'r' antes das aspas evita erros com as barras invertidas do Windows
MODEL_PATH = r'C:\Users\lavi\Desktop\interface_fmusp\modelo_PD_CR.pkl'
SCALER_PATH = r'C:\Users\lavi\Desktop\interface_fmusp\scaler.pkl'

FEATURES = [
    'original_glcm_DifferenceEntropy',
    'original_firstorder_InterquartileRange',
    'wavelet-H_gldm_DependenceVariance',
    'original_glrlm_ShortRunEmphasis'
]

## Carregamndo o modelo treinado e o scaler com cache para otimizar a performance
@st.cache_resource
def load_assets():
    try:
        clf = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        return clf, scaler
    except Exception as e:
        st.error(f"Erro ao carregar arquivos do modelo: {e}")
        return None, None

clf, scaler = load_assets()

# Função de extração corrigida para PNG (Label 255)
def extract_features(image_path, mask_path):
    # Inicializa o extrator
    extractor = featureextractor.RadiomicsFeatureExtractor()
    # ajustes críticos para PNG
    # Define que a máscara é o valor 255 (branco no PNG) em vez de 1
    extractor.settings['label'] = 255 
    # Tolera a falta de metadados espaciais comum em arquivos não-médicos (PNG/JPG)
    extractor.settings['geometryTolerance'] = 1e-3
    # Garante que a imagem seja tratada como 2D se necessário
    extractor.settings['force2D'] = True 
    # Executa a extração
    result = extractor.execute(image_path, mask_path)
    features_dict = {}
    for f in FEATURES:
        if f in result:
            # Converte de objeto NumPy para float comum
            features_dict[f] = float(result[f])
        else:
            features_dict[f] = 0.0
    return features_dict
## Função de Classificação
def classify(features_dict):
    # Organiza as features na ordem correta para o modelo
    X = np.array([[features_dict[f] for f in FEATURES]])
    # Aplica a normalização (scaler)
    X_scaled = scaler.transform(X)
    # Realiza a predição
    pred = clf.predict(X_scaled)[0]
    return "CR" if pred == 1 else "PD"

## Configurando a Interface Streamlit -- para startar o sistema, basta rodar este arquivo (interface.py) com o comando: streamlit run interface.py no CMD, estando na pasta onde o arquivo se encontra. !!!
## Para estar na pasta que o arqvuivo se encontra, use o comando: cd C:\Users\lavi\Desktop\interface_fmusp !!!

st.set_page_config(page_title="Classificador Radiômico", page_icon="🧠", layout="centered")

# Configurando a página com logo e título
col_logo, col_titulo = st.columns([1, 4])

with col_logo:
    # Ajuste o caminho para o nome real do seu arquivo de imagem
    st.image("logo_lavi.png", width=120) 

with col_titulo:
    st.markdown("<h1 style='margin-top: 0;'>Classificador Radiômico</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; color: #555; margin-top: 5px;'>Classificador utilizado no modelo treinado PD e CR com parceria com a FMUSP</p>", unsafe_allow_html=True)

# Informações adicionais e rodapé
st.markdown("""
    <div style="text-align: center; line-height: 1.6; margin-top: 20px;">
        <hr>
        <strong>Laboratório:</strong> Laboratório Avançado de Visão e Imagem (LAVI) - EESC/USP<br>
        <strong>Desenvolvido por:</strong> Vitor Augusto Tibério - Aluno de Iniciação Científica - Engenharia Elétrica - EESC/USP<br>
        <strong>Orientador:</strong> Prof. Dr. Marcelo Andrade da Costa Vieira
        <hr>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.write("### 📤 Upload dos Arquivos")
col1, col2 = st.columns(2)

with col1:
    image_file = st.file_uploader("Imagem Médica (PNG, JPG, NII)", type=["nii", "nii.gz", "dcm", "png", "jpg"])
with col2:
    mask_file = st.file_uploader("Máscara ROI (PNG, JPG, NII)", type=["nii", "nii.gz", "dcm", "png", "jpg"])

if st.button("🚀 Executar Classificação"):
    if image_file is None or mask_file is None:
        st.error("Por favor, envie ambos os arquivos: Imagem e Máscara.")
    elif clf is None or scaler is None:
        st.error("O modelo não foi carregado corretamente. Verifique os caminhos dos arquivos .pkl")
    else:
        with st.spinner("Processando..."):
            with tempfile.TemporaryDirectory() as tmpdir:
                # Salva arquivos temporários para o PyRadiomics ler
                img_path = os.path.join(tmpdir, image_file.name)
                msk_path = os.path.join(tmpdir, mask_file.name)

                with open(img_path, "wb") as f:
                    f.write(image_file.getbuffer())
                with open(msk_path, "wb") as f:
                    f.write(mask_file.getbuffer())

                try:
                    # Extaindo as features
                    st.info("Passo 1: Extraindo características da imagem...")
                    features = extract_features(img_path, msk_path)
                    
                    # Mostra os valores extraídos
                    with st.expander("Ver detalhes das features extraídas"):
                        st.json(features)

                    # Classifica com base nas features extraídas
                    st.info("Passo 2: Aplicando o modelo de classificação desenvolvido no laboratório...")
                    resultado = classify(features)

                    # Resultado Final
                    st.markdown("---")
                    st.subheader("Resultado da Análise:")
                    if resultado == "CR":
                        st.success(f"O modelo classificou como: **{resultado}**")
                    else:
                        st.warning(f"O modelo classificou como: **{resultado}**")

                except Exception as e:
                    st.error(f"Erro durante o processamento: {e}")
                    st.info("Dica: Verifique se a máscara cobre exatamente uma área da imagem.")
