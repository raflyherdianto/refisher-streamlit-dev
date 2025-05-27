import streamlit as st
import numpy as np
from PIL import Image, ImageEnhance
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
import io
import os
import random

# --- Diubah untuk tflite-runtime ---
# Mengimpor Interpreter dari tflite-runtime untuk efisiensi.
# Jika gagal, TFLITE_AVAILABLE akan False, dan aplikasi berjalan dalam mode demo.
try:
    from tflite_runtime.interpreter import Interpreter
    TFLITE_AVAILABLE = True
except ImportError:
    TFLITE_AVAILABLE = False

# --- Kelas MinimalTFLiteInterpreter ---
# Kelas ini digunakan sebagai fallback jika tflite-runtime tidak terinstal.
# Ini memungkinkan aplikasi tetap berjalan untuk demo UI.
class MinimalTFLiteInterpreter:
    """Minimal TensorFlow Lite interpreter for when TensorFlow is not available"""
    def __init__(self, model_path):
        st.warning("⚠️ Peringatan: `tflite-runtime` tidak ditemukan. Aplikasi berjalan dalam mode demo dengan prediksi acak.")
        self.model_path = model_path
        self.input_height = 224
        self.input_width = 224
        
    def allocate_tensors(self):
        pass
        
    def get_input_details(self):
        return [{'shape': [1, 224, 224, 3]}]
        
    def get_output_details(self):
        return [{'index': 0}]
        
    def set_tensor(self, index, data):
        pass
        
    def invoke(self):
        pass
        
    def get_tensor(self, index):
        # Mengembalikan prediksi pura-pura untuk tujuan demo
        fresh_confidence = np.random.uniform(0.6, 0.95)
        non_fresh_confidence = 1.0 - fresh_confidence
        return np.array([[fresh_confidence, non_fresh_confidence]], dtype=np.float32)

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="🐟 ReFisher - Klasifikasi Kesegaran Ikan",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Kustomisasi CSS untuk tampilan aplikasi
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        background: linear-gradient(90deg, #1e3c72, #2a5298);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .subtitle { text-align: center; color: #666; font-size: 1.2rem; margin-bottom: 3rem; }
    .prediction-box { padding: 1.5rem; border-radius: 10px; margin: 1rem 0; text-align: center; color: white; }
    .fresh-fish { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    .non-fresh-fish { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
    .info-card { background: #f8f9fa; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #007bff; margin: 1rem 0; }
    .metric-card { background: white; padding: 1rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center; margin: 0.5rem; }
    .footer { text-align: center; padding: 2rem; color: #666; border-top: 1px solid #eee; margin-top: 3rem; }
</style>
""", unsafe_allow_html=True)

class FishFreshnessClassifier:
    def __init__(self, model_path):
        """Inisialisasi model TensorFlow Lite."""
        try:
            # --- Diubah untuk tflite-runtime ---
            if TFLITE_AVAILABLE:
                self.interpreter = Interpreter(model_path=model_path)
            else:
                self.interpreter = MinimalTFLiteInterpreter(model_path)
            
            self.interpreter.allocate_tensors()
            self.input_details = self.interpreter.get_input_details()
            self.output_details = self.interpreter.get_output_details()
            self.input_shape = self.input_details[0]['shape']
            self.input_height = self.input_shape[1]
            self.input_width = self.input_shape[2]
            self.class_labels = ['Fresh Fish', 'Non Fresh Fish']
        except Exception as e:
            st.error(f"Error saat memuat model: {str(e)}")
            self.interpreter = None
    
    def preprocess_image(self, image):
        """Pra-pemrosesan gambar untuk input model."""
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image = image.resize((self.input_width, self.input_height))
        image_array = np.array(image, dtype=np.float32) / 255.0
        return np.expand_dims(image_array, axis=0)
    
    def predict(self, image):
        """Melakukan prediksi pada gambar."""
        if self.interpreter is None: return None, None
        
        try:
            processed_image = self.preprocess_image(image)
            self.interpreter.set_tensor(self.input_details[0]['index'], processed_image)
            self.interpreter.invoke()
            output_data = self.interpreter.get_tensor(self.output_details[0]['index'])
            
            # --- Diubah untuk tflite-runtime ---
            # Selalu gunakan implementasi softmax dari numpy karena tflite-runtime tidak punya tf.nn.softmax
            exp_values = np.exp(output_data[0] - np.max(output_data[0]))
            probabilities = exp_values / np.sum(exp_values)
            
            predicted_class_idx = np.argmax(probabilities)
            predicted_class = self.class_labels[predicted_class_idx]
            return predicted_class, probabilities
        except Exception as e:
            st.error(f"Error saat prediksi: {str(e)}")
            return None, None

def create_confidence_chart(probabilities, class_labels):
    """Membuat grafik batang untuk skor keyakinan."""
    fig = go.Figure(data=[go.Bar(
        x=class_labels, y=probabilities,
        marker_color=['#28a745' if prob == max(probabilities) else '#6c757d' for prob in probabilities],
        text=[f'{prob:.2%}' for prob in probabilities], textposition='auto',
    )])
    fig.update_layout(title="Visualisasi Skor Keyakinan", xaxis_title="Kelas", yaxis_title="Keyakinan", yaxis=dict(range=[0, 1]), height=400)
    return fig

def create_sample_images_section():
    """Membuat bagian untuk memilih gambar contoh."""
    st.subheader("🖼️ Contoh Gambar untuk Testing")
    st.markdown("<div class='info-card'><p>Tidak punya gambar ikan? Gunakan contoh gambar berikut untuk mencoba aplikasi:</p></div>", unsafe_allow_html=True)
    
    sample_col1, sample_col2, sample_col3 = st.columns(3)
    FRESH_DIR, NON_FRESH_DIR = "test_sample/Fresh Fish", "test_sample/Non Fresh Fish"
    
    def on_sample_click(path):
        try:
            if not os.path.isdir(path):
                st.error(f"Direktori tidak ditemukan: '{path}'. Pastikan folder 'test_sample' ada.")
                return
            files = [f for f in os.listdir(path) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
            if files:
                st.session_state.sample_image_path = os.path.join(path, random.choice(files))
            else:
                st.warning(f"Tidak ada file gambar di: '{path}'")
        except Exception as e:
            st.error(f"Gagal memuat gambar contoh: {e}")

    with sample_col1:
        if st.button("🟢 Fresh Fish Sample", use_container_width=True): on_sample_click(FRESH_DIR)
    with sample_col2:
        if st.button("🔴 Non-Fresh Fish Sample", use_container_width=True): on_sample_click(NON_FRESH_DIR)
    with sample_col3:
        if st.button("📷 Tips Foto yang Baik", use_container_width=True):
            st.info("Tips foto optimal: Pastikan mata ikan terlihat jelas, gunakan pencahayaan cukup, ambil dari jarak dekat, dan hindari gambar buram.")

def main():
    st.markdown('<h1 class="main-header">🐟 ReFisher</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Sistem Klasifikasi Kesegaran Ikan Menggunakan Computer Vision</p>', unsafe_allow_html=True)
    
    @st.cache_resource
    def load_model(): return FishFreshnessClassifier("model.tflite")
    classifier = load_model()

    if "sample_image_path" not in st.session_state: st.session_state.sample_image_path = None

    with st.sidebar:
        st.header("📋 Informasi & Pengaturan")
        st.markdown("<div class='info-card'><h4>Informasi Model</h4><p><strong>Sumber Data:</strong> Roboflow Universe</p><p><strong>Kelas:</strong> Fresh & Non Fresh</p><p><strong>Model:</strong> TensorFlow Lite</p></div>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("<h4>Cara Penggunaan</h4><ol><li>Upload gambar atau pilih contoh</li><li>Tunggu proses analisis</li><li>Lihat hasil prediksi</li></ol>", unsafe_allow_html=True)
        st.markdown("---")
        show_details = st.checkbox("Tampilkan detail teknis", value=True)
        show_confidence = st.checkbox("Tampilkan grafik keyakinan", value=True)

    st.markdown("---")
    create_sample_images_section()

    col1, col2 = st.columns([1, 1])
    image, caption = None, ""
    
    with col1:
        st.header("📤 Upload atau Pilih Gambar")
        uploaded_file = st.file_uploader("Pilih gambar ikan untuk diklasifikasi", type=['png', 'jpg', 'jpeg'])
        
        if uploaded_file:
            image, caption = Image.open(uploaded_file), "Gambar yang diupload"
            st.session_state.sample_image_path = None
        elif st.session_state.sample_image_path:
            try:
                image, caption = Image.open(st.session_state.sample_image_path), f"Contoh: {os.path.basename(st.session_state.sample_image_path)}"
            except Exception as e:
                st.error(f"Gagal membuka gambar contoh: {e}")
                st.session_state.sample_image_path = None

        if image:
            st.image(image, caption=caption, use_column_width=True)
            st.subheader("🎨 Peningkatan Kualitas Gambar")
            enhance_contrast = st.slider("Kontras", 0.5, 2.0, 1.0, 0.1)
            enhance_brightness = st.slider("Kecerahan", 0.5, 2.0, 1.0, 0.1)
            
            if abs(enhance_contrast - 1.0) > 0.01 or abs(enhance_brightness - 1.0) > 0.01:
                enhanced_image = ImageEnhance.Contrast(image).enhance(enhance_contrast)
                enhanced_image = ImageEnhance.Brightness(enhanced_image).enhance(enhance_brightness)
                image = enhanced_image
                st.image(image, caption="Gambar setelah enhancement", use_column_width=True)
    
    with col2:
        st.header("🤖 Hasil Prediksi")
        if image:
            with st.spinner("🔄 Menganalisis gambar..."):
                predicted_class, probabilities = classifier.predict(image)
            
            if predicted_class and probabilities is not None:
                confidence = max(probabilities)
                result_class = "fresh-fish" if predicted_class == "Fresh Fish" else "non-fresh-fish"
                result_icon = "🟢" if predicted_class == "Fresh Fish" else "🔴"
                recommendation = "Ikan terdeteksi dalam kondisi segar dan layak konsumsi" if predicted_class == "Fresh Fish" else "Ikan terdeteksi dalam kondisi tidak segar dan tidak layak konsumsi"
                
                st.markdown(f'<div class="prediction-box {result_class}"><h2>{result_icon} {predicted_class}</h2><h3>Keyakinan: {confidence:.2%}</h3><p>{recommendation}</p></div>', unsafe_allow_html=True)
                
                if show_details:
                    st.subheader("📈 Detail Metrik")
                    m_col1, m_col2 = st.columns(2)
                    m_col1.metric("Keyakinan Ikan Segar", f"{probabilities[0]:.2%}")
                    m_col2.metric("Keyakinan Ikan Tidak Segar", f"{probabilities[1]:.2%}")
                
                if show_confidence:
                    st.plotly_chart(create_confidence_chart(probabilities, classifier.class_labels), use_container_width=True)
                
                st.markdown("---")
                st.subheader("💾 Unduh Hasil")
                buffer = io.BytesIO()
                image.save(buffer, format='PNG')
                st.download_button(label="📥 Unduh Gambar Hasil Proses", data=buffer, file_name=f"processed_{caption.split(':')[-1].strip()}", mime="image/png", use_container_width=True)
            else:
                st.error("❌ Gagal melakukan prediksi. Coba lagi dengan gambar lain.")
        else:
            st.info("📷 Silakan unggah gambar ikan atau pilih dari contoh untuk memulai klasifikasi.")

    st.markdown("---")
    with st.expander("ℹ️ Tentang Aplikasi ReFisher"):
        st.markdown(
            """
            Aplikasi ini menggunakan **Computer Vision** dan **Deep Learning** untuk mengklasifikasikan kesegaran ikan berdasarkan analisis citra.
            - **Backend**: Python, Streamlit
            - **Machine Learning**: TensorFlow Lite
            - **Dataset**: Roboflow Universe (Fresh and Non-Fresh Fish)
            """
        )
    
    st.markdown('<div class="footer"><p>🐟 ReFisher - Capstone Project © 2025</p></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()