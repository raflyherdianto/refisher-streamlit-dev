# modules/articles.py
import streamlit as st
import os
from PIL import Image
import base64

# Import fungsi show_artikel dari masing-masing artikel
from modules.articles_content.artikel_1 import show_artikel_1
from modules.articles_content.artikel_2 import show_artikel_2
from modules.articles_content.artikel_3 import show_artikel_3

def page_articles():
    # Inisialisasi session_state jika belum ada
    if "selected_article" not in st.session_state:
        st.session_state["selected_article"] = None

    # Tampilkan artikel terpilih jika ada
    if st.session_state["selected_article"] == "artikel_1":
        show_artikel_1()
    elif st.session_state["selected_article"] == "artikel_2":
        show_artikel_2()
    elif st.session_state["selected_article"] == "artikel_3":
        show_artikel_3()
    else:
        # Jika tidak ada artikel yang dipilih, tampilkan daftar kartu artikel
        st.header("📰 Baca Artikel Terbaru Kami")
        st.markdown("""
            Temukan informasi dan wawasan menarik seputar kesegaran ikan, teknologi computer vision,
            dan machine learning di sini.
            """)

        st.info("Pilih artikel di bawah untuk membacanya:")

        # Menggunakan st.columns untuk grid artikel
        col1, col2, col3 = st.columns(3)

        with col1:
            display_article_card(
                title="Pentingnya Kesegaran Ikan",
                image_filename="Gambar-Artikel1.jpg",
                summary="Mengapa kesegaran ikan sangat krusial untuk kesehatan dan keamanan konsumsi Anda? Pahami manfaat dan risiko ikan tidak segar.",
                article_key="artikel_1"
            )
        with col2:
            display_article_card(
                title="Bahaya Mengonsumsi Ikan Tidak Segar",
                image_filename="Gambar-Artikel2.jpg",
                summary="Kenali berbagai risiko kesehatan, mulai dari gangguan pencernaan hingga keracunan serius, akibat konsumsi ikan yang tidak segar.",
                article_key="artikel_2"
            )
        with col3:
            display_article_card(
                title="Cara Menyimpan Ikan Agar Tetap Segar Lebih Lama",
                image_filename="Gambar-Artikel3.jpg",
                summary="Pelajari teknik penyimpanan yang tepat, mulai dari pembersihan hingga pembekuan, untuk menjaga kualitas dan rasa ikan.",
                article_key="artikel_3"
            )


def display_article_card(title, image_filename, summary, article_key):
    img_src = "https://via.placeholder.com/60?text=No+Image" # Default placeholder

    filesystem_path = os.path.join(".streamlit", "static", image_filename)

    if os.path.exists(filesystem_path):
        try:
            with open(filesystem_path, "rb") as f:
                encoded_string = base64.b64encode(f.read()).decode()
            img_src = f"data:image/jpeg;base64,{encoded_string}" # Sesuaikan 'jpeg' jika gambar Anda PNG/lainnya

        except Exception as e:
            st.warning(f"Gagal memuat gambar '{image_filename}' sebagai base64: {e}")
            img_src = "https://via.placeholder.com/60?text=Error"
    else:
        st.warning(f"Gambar '{image_filename}' tidak ditemukan di '{filesystem_path}' untuk artikel '{title}'.")

    # Konten kartu HTML
    card_html = f"""
    <div class="article-card">
        <div class="article-card-header">
            <img src="{img_src}" class="article-card-img" alt="{title}"/>
            <h5 class="article-card-title">{title}</h5>
        </div>
        <p class="article-card-summary">{summary}</p>
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)
    
    # Menambahkan jarak 16px di atas tombol menggunakan CSS inline sederhana atau margin.
    st.markdown(
        f"""
        <style>
            /* Target tombol spesifik ini untuk margin */
            div[data-testid="stColumn"] > div[data-testid^="stVerticalBlock"] > div[data-testid^="stButton"] button[key="hidden_button_{article_key}"] {{
                margin-top: 8px !important;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Tombol "Baca Artikel" yang terlihat
    if st.button("Baca Artikel", key=f"hidden_button_{article_key}", use_container_width=True):
        st.session_state["selected_article"] = article_key
        st.rerun() 
        # Tidak selalu diperlukan di sini karena perubahan session_state
        # di awal fungsi page_articles sudah akan memicu render ulang yang benar.
        # Tapi tidak ada salahnya jika dibiarkan.