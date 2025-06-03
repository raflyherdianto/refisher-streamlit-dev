import streamlit as st
import os
import random

def page_panduan_penggunaan():
    st.header("📖 Panduan Penggunaan")
    st.markdown("""
    <div class='info-card'>
        <p>Aplikasi ReFisher dirancang untuk membantu Anda mengidentifikasi kesegaran ikan dengan mudah. Ikuti langkah-langkah di bawah untuk memulai klasifikasi:</p>
        <ul>
            <li><p><strong>Unggah Gambar atau Pilih Contoh:</strong> Anda dapat mengunggah foto ikan Anda sendiri atau menggunakan salah satu contoh gambar ikan yang kami sediakan di bawah.</p></li>
            <li><p><strong>Tunggu Proses Analisis:</strong> Setelah gambar diunggah, aplikasi akan menganalisisnya secara otomatis.</p></li>
            <li><p><strong>Lihat Hasil Prediksi:</strong> Anda akan melihat hasil prediksi kesegaran (Segar atau Tidak Segar) beserta tingkat keyakinannya.</p></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🐟 Tips Mengambil Foto Ikan yang Baik")
    st.markdown("""
    <div class='info-card'>
        <ul>
            <li><strong>Fokus pada Mata Ikan:</strong> Mata ikan adalah indikator utama kesegaran. Pastikan terlihat jelas.</li>
            <li><strong>Pencahayaan Cukup:</strong> Gunakan pencahayaan yang merata dan hindari bayangan.</li>
            <li><strong>Ambil dari Jarak Dekat:</strong> Foto close-up memberikan detail yang lebih baik untuk dianalisis model.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📸 Contoh Gambar untuk Dicoba")
    st.markdown("<div class='info-card'><p>Tidak punya gambar ikan? Klik tombol di bawah untuk mencoba langsung aplikasi dengan gambar contoh kami.</p></div>", unsafe_allow_html=True)

    # Fungsi ini akan dipanggil saat tombol diklik
    def set_sample_and_redirect(path, fish_type):
        """Menyiapkan status untuk pengalihan dan pesan popup."""
        try:
            # Pastikan direktori ada sebelum mencoba mengaksesnya
            if not os.path.isdir(path):
                st.error(f"Direktori contoh tidak ditemukan: '{path}'. Pastikan folder 'test_sample' ada dan terisi gambar.")
                return

            files = [f for f in os.listdir(path) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
            if files:
                # 1. Atur path gambar untuk digunakan oleh halaman utama
                st.session_state.sample_image_path = os.path.join(path, random.choice(files))
                # 2. Atur pesan yang akan ditampilkan sebagai popup
                st.session_state.toast_message = f"Anda dialihkan ke halaman utama dengan gambar contoh {fish_type}."
                # 3. Atur halaman tujuan
                st.session_state.current_page = "🏡 Aplikasi Klasifikasi"
            else:
                st.warning(f"Tidak ada file gambar di: '{path}'")
        except Exception as e:
            st.error(f"Gagal memuat gambar contoh: {e}")

    col1, col2 = st.columns(2)
    with col1:
        st.button(
            "Contoh Ikan Segar",
            on_click=set_sample_and_redirect,
            args=("test_sample/Fresh Fish", "Ikan Segar"),
            use_container_width=True
        )
    with col2:
        st.button(
            "Contoh Ikan Tidak Segar",
            on_click=set_sample_and_redirect,
            args=("test_sample/Non Fresh Fish", "Ikan Tidak Segar"),
            use_container_width=True
        )
