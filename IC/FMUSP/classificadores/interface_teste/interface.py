import streamlit as st
import numpy as np
import joblib
import SimpleITK as sitk
from radiomics import featureextractor
import tempfile
import os

# ==============================
# CONFIG
# ==============================
FEATURES = [
    'original_glcm_DifferenceEntropy',
    'original_firstorder_InterquartileRange',
    'wavelet-H_gldm_DependenceVariance',
    'original_glrlm_ShortRunEmphasis'
]

MODEL_PATH = "modelo_PD_CR.pkl"
SCALER_PATH = "scaler.pkl"

# ==============================
# CARREGAR MODELO
# ==============================
@st.cache_resource
def load_model():
    clf = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    return clf, scaler

clf, scaler = load_model()

# ==============================
# FUNÇÃO DE EXTRAÇÃO
# ==============================
def extract_features(image_path, mask_path):
    extractor = featureextractor.RadiomicsFeatureExtractor()

    result = extractor.execute(image_path, mask_path)

    features_dict = {}

    for f in FEATURES:
        if f in result:
            features_dict[f] = result[f]
        else:
            features_dict[f] = 0  # fallback

    return features_dict

# ==============================
# CLASSIFICAÇÃO
# ==============================
def classify(features_dict):
    X = np.array([[features_dict[f] for f in FEATURES]])
    X_scaled = scaler.transform(X)

    pred = clf.predict(X_scaled)[0]

    return "CR" if pred == 1 else "PD"

# ==============================
# INTERFACE
# ==============================
st.title("🧠 Classificador Radiômico PD vs CR")

st.write("Upload da imagem médica e da máscara (ROI)")

image_file = st.file_uploader("Imagem", type=["nii", "nii.gz"])
mask_file = st.file_uploader("Máscara", type=["nii", "nii.gz"])

if st.button("Classificar"):

    if image_file is None or mask_file is None:
        st.error("Envie imagem e máscara!")
    else:
        with tempfile.TemporaryDirectory() as tmpdir:

            image_path = os.path.join(tmpdir, image_file.name)
            mask_path = os.path.join(tmpdir, mask_file.name)

            with open(image_path, "wb") as f:
                f.write(image_file.read())

            with open(mask_path, "wb") as f:
                f.write(mask_file.read())

            st.info("Extraindo features radiômicas...")

            features = extract_features(image_path, mask_path)

            st.write("### Features extraídas:")
            st.json(features)

            result = classify(features)

            st.success(f"Classificação: **{result}**")