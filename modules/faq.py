# modules/faq.py
import streamlit as st

def page_faq():
    st.header("❓ Pertanyaan yang Sering Diajukan (FAQ)")
    
    st.write(
        """
        Di sini Anda dapat menemukan jawaban atas pertanyaan umum seputar aplikasi ReFisher.
        Kami berharap bagian ini dapat membantu Anda memahami lebih lanjut tentang cara kerja aplikasi ini dan mendapatkan hasil terbaik.
        """
    )
    
    st.markdown("---")

    faq_items = [
        {
            "question": "1. Apa itu ReFisher?",
            "content": """
            ReFisher adalah aplikasi berbasis **Kecerdasan Buatan (AI)** yang dirancang untuk mengklasifikasikan kesegaran ikan.
            Aplikasi ini bekerja dengan menganalisis gambar **mata ikan** menggunakan teknologi **Computer Vision** dan **Deep Learning**.
            """
        },
        {
            "question": "2. Bagaimana cara kerja ReFisher?",
            "content": """
            ReFisher menganalisis gambar mata ikan yang Anda unggah. Model **TensorFlow Lite** kami, yang telah dilatih secara ekstensif dengan dataset dari **Roboflow**, akan memproses gambar tersebut dan mengklasifikasikannya sebagai **“Segar”** atau **“Tidak Segar”**.
            """
        },
        {
            "question": "3. Jenis gambar seperti apa yang bisa saya unggah?",
            "content": """
            Anda dapat mengunggah gambar mata ikan dalam format **PNG, JPG, atau JPEG**.
            Untuk hasil prediksi terbaik, sangat disarankan untuk:
            * Mengambil gambar **dari dekat mata ikan**.
            * Memastikan gambar **fokus** (tidak buram).
            * Menyediakan **pencahayaan yang cukup** dan merata pada ikan.
            """
        },
        {
            "question": "4. Berapa ukuran file maksimum yang diizinkan?",
            "content": """
            Ukuran file maksimal yang bisa Anda unggah adalah **200MB** per gambar.
            """
        },
        {
            "question": "5. Saya tidak punya gambar ikan sendiri. Apa yang bisa saya lakukan?",
            "content": """
            Jangan khawatir! Anda bisa menggunakan contoh gambar yang telah kami sediakan di halaman **"Panduan Penggunaan"**. Tersedia:
            * **🟢 Gambar Contoh Ikan Segar (Fresh Fish Sample)**
            * **🔴 Gambar Contoh Ikan Tidak Segar (Non-Fresh Fish Sample)**
            """
        },
        {
            "question": "6. Seberapa akurat prediksi ReFisher?",
            "content": """
            Model ReFisher telah dilatih dengan **ratusan gambar** dan menunjukkan tingkat akurasi yang baik dalam klasifikasi kesegaran ikan. Namun, penting untuk diingat bahwa ReFisher adalah **alat bantu**, bukan satu-satunya penentu kualitas ikan. Kami selalu menyarankan untuk menggunakan penilaian pribadi Anda sebagai pertimbangan akhir.
            """
        },
        {
            "question": "7. Apakah data saya disimpan atau dibagikan?",
            "content": """
            **Tidak.** Kami menjamin privasi Anda. Gambar yang Anda unggah untuk analisis **tidak disimpan** atau **dibagikan** ke pihak mana pun. Semua proses klasifikasi gambar dilakukan secara lokal di *browser* Anda atau server sementara saat Anda menggunakannya.
            """
        },
        {
            "question": "8. Teknologi apa saja yang digunakan di ReFisher?",
            "content": """
            ReFisher dibangun dengan beberapa teknologi inti:
            * **Framework Aplikasi:** Streamlit (untuk antarmuka pengguna web interaktif)
            * **Model Machine Learning:** TensorFlow Lite (untuk inferensi AI yang efisien)
            * **Dataset Pelatihan:** Roboflow - Fresh vs Non-Fresh Fish
            * **Bahasa Pemrograman Utama:** Python
            """
        }
    ]

    for item in faq_items:
        with st.expander(item["question"]):
            st.markdown(item["content"])

    st.markdown("---")