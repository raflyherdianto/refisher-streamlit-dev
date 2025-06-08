import streamlit as st
import numpy as np
from PIL import Image, ImageEnhance
import plotly.graph_objects as go
import os
import sys
import random
import base64

# --- Menambahkan path proyek ke sys.path ---
# Ini memastikan bahwa aplikasi dapat menemukan folder 'modules' secara konsisten.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# --- Import halaman dari modules ---
from modules.panduan_penggunaan import page_panduan_penggunaan
from modules.faq import page_faq
from modules.articles import page_articles

# --- Logika Impor TensorFlow/TFLite ---
TFLITE_RUNTIME_AVAILABLE = False
TENSORFLOW_AVAILABLE = False
Interpreter = None
tf = None
try:
    from tflite_runtime.interpreter import Interpreter
    TFLITE_RUNTIME_AVAILABLE = True
except ImportError:
    try:
        import tensorflow as tf
        Interpreter = tf.lite.Interpreter
        TENSORFLOW_AVAILABLE = True
    except ImportError:
        pass

# ==============================================================================
# KONFIGURASI APLIKASI UTAMA
# ==============================================================================

st.set_page_config(
    page_title="ReFisher - Klasifikasi Kesegaran Ikan",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Kustomisasi CSS
st.markdown("""
<style>

/* Untuk tampilan website 
.st-emotion-cache-nccqt6 img {
    width: 17%;
    vertical-align: middle;
    word-break: break-word;
    margin-top: 15px;
    margin-left: 0px;
    margin-right: 0px;
}

/* Untuk tampilan handphone
@media (max-width: 768px) { 
    .st-emotion-cache-nccqt6 img {
        max-width: 40%;
        vertical-align: middle;
    }

    .st-emotion-cache-nccqt6 p {
        word-break: break-word;
        margin-top: 15px;
        margin-left: 0px;
        margin-right: 0px;
    }
}
    .app-logo-container { 
        text-align: center; 
        margin-bottom: -20px; 
    }
    .app-logo { 
        width: 17%;
        height: auto;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .app-jargon { 
        text-align: center; 
        font-size: 1.15rem; 
        color: #666; 
        margin-top: 0px; 
        margin-bottom: 3rem; 
    }
    .sidebar-logo { 
        width: 150px; 
        display: block; 
        margin: 10px auto 20px auto; 
    }
    .prediction-box { 
        padding: 20px; 
        border-radius: 10px; 
        margin: 10px 0; 
        text-align: center; 
    }
    .fresh-fish { 
        background-color: #d4edda; 
        border: 1px solid #c3e6cb; 
        color: #155724; 
    }
    .non-fresh-fish { 
        background-color: #f8d7da; 
        border: 1px solid #f5c6cb; 
        color: #721c24; 
    }
    .info-card { 
        background-color: #f8f9fa; 
        padding: 15px; 
        border-radius: 8px; 
        border-left: 4px solid #007bff; 
        margin: 10px 0; 
    }
    .footer { 
        text-align: center; 
        color: grey; 
        margin-top: 30px; 
    }
</style>
""", unsafe_allow_html=True)


# ==============================================================================
# HALAMAN UTAMA: KLASIFIKASI
# ==============================================================================

def page_klasifikasi_utama(classifier, logo_base64):
    """Fungsi untuk menampilkan halaman utama aplikasi klasifikasi."""
    st.markdown(f'<div class="app-logo-container"><img src="data:image/png;base64,{logo_base64}" class="app-logo"></div><p class="app-jargon">Segarnya Ikan, Amannya Sajian Anda.</p>', unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns([1, 1])
    image, caption = None, ""
    
    with col1:
        st.header("📤 Unggah Gambar untuk Analisis")
        st.info("💡 Anda juga bisa menemukan contoh gambar di halaman 'Panduan Penggunaan'.")
        uploaded_file = st.file_uploader("Pilih gambar ikan (.png, .jpg, .jpeg)", type=['png', 'jpg', 'jpeg'])
        
        if 'sample_image_path' in st.session_state and st.session_state.sample_image_path:
            try:
                image = Image.open(st.session_state.sample_image_path)
                caption = f"Contoh: {os.path.basename(st.session_state.sample_image_path)}"
                st.session_state.sample_image_path = None 
            except Exception as e:
                st.error(f"Gagal membuka gambar contoh: {e}")

        if uploaded_file:
            image, caption = Image.open(uploaded_file), "Gambar yang diunggah"

        if image:
            st.image(image, caption=caption, use_column_width=True)
            st.subheader("🎨 Sesuaikan Kualitas Gambar")
            enhance_contrast = st.slider("Kontras", 0.5, 2.0, 1.0, 0.1)
            enhance_brightness = st.slider("Kecerahan", 0.5, 2.0, 1.0, 0.1)
            
            if abs(enhance_contrast - 1.0) > 0.01 or abs(enhance_brightness - 1.0) > 0.01:
                original_image = image.copy()
                enhanced_image = ImageEnhance.Contrast(original_image).enhance(enhance_contrast)
                image = ImageEnhance.Brightness(enhanced_image).enhance(enhance_brightness)
                st.image(image, caption="Gambar setelah peningkatan kualitas", use_column_width=True)

    with col2:
        st.header("🤖 Hasil Analisis Kesegaran Ikan")
        if image and classifier:
            with st.spinner("🔄 Menganalisis gambar ikan..."):
                predicted_class, probabilities = classifier.predict(image)
            
            if predicted_class and probabilities is not None:
                confidence = max(probabilities)
                result_class = "fresh-fish" if predicted_class == "Fresh Fish" else "non-fresh-fish"
                result_icon = "🟢" if predicted_class == "Fresh Fish" else "🔴"
                recommendation = "Ikan terdeteksi dalam kondisi segar dan **layak konsumsi**." if predicted_class == "Fresh Fish" else "Ikan terdeteksi dalam kondisi **tidak segar** dan tidak layak konsumsi."
                
                st.markdown(f'<div class="prediction-box {result_class}"><h2>{result_icon} {predicted_class}</h2><h3>Keyakinan: {confidence:.2%}</h3><p>{recommendation}</p></div>', unsafe_allow_html=True)
                
                with st.expander("Lihat Detail Analisis"):
                    st.metric("Keyakinan Ikan Segar", f"{probabilities[0]:.2%}")
                    st.metric("Keyakinan Ikan Tidak Segar", f"{probabilities[1]:.2%}")
                    fig = go.Figure(data=[go.Bar(
                        x=classifier.class_labels, y=probabilities,
                        marker_color=['#28a745', '#dc3545'],
                        text=[f'{prob:.2%}' for prob in probabilities], textposition='auto',
                    )])
                    fig.update_layout(title_text="Visualisasi Skor Keyakinan", yaxis=dict(range=[0, 1]))
                    st.plotly_chart(fig, use_container_width=True)
            else:
                st.error("❌ Gagal melakukan prediksi.")
        else:
            st.info("📷 Silakan unggah gambar ikan untuk memulai klasifikasi.")

# ==============================================================================
# FUNGSI-FUNGSI PEMBANTU DAN KELAS MODEL
# ==============================================================================
class MinimalTFLiteInterpreter:
    def __init__(self, model_path): 
        self.model_path = model_path
    def allocate_tensors(self): pass
    def get_input_details(self): return [{'shape': [1, 224, 224, 3]}]
    def get_output_details(self): return [{'index': 0}]
    def set_tensor(self, index, data): pass
    def invoke(self): pass
    def get_tensor(self, index):
        fresh_confidence = np.random.uniform(0.6, 0.95)
        return np.array([[fresh_confidence, 1.0 - fresh_confidence]], dtype=np.float32)

class FishFreshnessClassifier:
    def __init__(self, model_path):
        self.interpreter = None
        self.class_labels = ['Fresh Fish', 'Non Fresh Fish']
        if not (TFLITE_RUNTIME_AVAILABLE or TENSORFLOW_AVAILABLE):
            st.warning("⚠️ TensorFlow atau TFLite Runtime tidak ditemukan. Aplikasi berjalan dalam mode demo.")
            self.interpreter = MinimalTFLiteInterpreter(model_path)
            return
        try:
            self.interpreter = Interpreter(model_path=model_path)
            self.interpreter.allocate_tensors()
            self.input_details = self.interpreter.get_input_details()
            self.output_details = self.interpreter.get_output_details()
        except Exception as e:
            st.error(f"Error saat memuat model: {e}")
            self.interpreter = None

    def predict(self, image):
        if self.interpreter is None: return None, None
        input_shape = self.input_details[0]['shape']
        img_resized = image.resize((input_shape[2], input_shape[1])).convert('RGB')
        img_array = np.array(img_resized, dtype=np.float32) / 255.0
        img_expanded = np.expand_dims(img_array, axis=0)
        self.interpreter.set_tensor(self.input_details[0]['index'], img_expanded)
        self.interpreter.invoke()
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])
        exp_values = np.exp(output_data[0] - np.max(output_data[0]))
        probabilities = exp_values / np.sum(exp_values)
        return self.class_labels[np.argmax(probabilities)], probabilities

def _get_image_as_base64(filepath):
    if not os.path.exists(filepath):
        return ""
    with open(filepath, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

# ==============================================================================
# MAIN APP ROUTER
# ==============================================================================
def main():
    """Fungsi utama aplikasi yang mengatur navigasi dan konten."""
    
    @st.cache_resource
    def load_model():
        return FishFreshnessClassifier("model.tflite")
    classifier = load_model()

    main_logo_base64 = _get_image_as_base64('Logo ReFisher.png')
    sidebar_logo_base64 = _get_image_as_base64('Logo-Name.png')

    if "current_page" not in st.session_state:
        st.session_state.current_page = "🏡 Aplikasi Klasifikasi"

    PAGES = {
        "🏡 Aplikasi Klasifikasi": lambda: page_klasifikasi_utama(classifier, main_logo_base64),
        "📖 Panduan Penggunaan": page_panduan_penggunaan,
        "📰 Artikel": page_articles,
        "❓ FAQ": page_faq,
    }
    page_keys = list(PAGES.keys())

    with st.sidebar:
        if sidebar_logo_base64:
            st.markdown(f'<img src="data:image/png;base64,{sidebar_logo_base64}" class="sidebar-logo">', unsafe_allow_html=True)
        else:
            st.title("ReFisher")
        
        st.header("📋 Navigasi")

        def on_nav_change():
            st.session_state.current_page = st.session_state.sidebar_radio
            st.session_state.sample_image_path = None

        st.radio(
            "Pilih Halaman:",
            page_keys,
            index=page_keys.index(st.session_state.current_page),
            on_change=on_nav_change,
            key='sidebar_radio'
        )
        
        st.markdown("---")
        with st.expander("ℹ️ Tentang Aplikasi"):
            st.markdown("Aplikasi ini menggunakan **Computer Vision** untuk mengklasifikasikan kesegaran ikan.")
        st.markdown("---")

    if st.session_state.get("toast_message"):
        st.toast(st.session_state.toast_message, icon="🎉")
        st.session_state.toast_message = None

    page_function = PAGES[st.session_state.current_page]
    page_function()

    st.markdown("---") 
    st.markdown('<div class="footer">© 2025 ReFisher. All rights reserved.</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
