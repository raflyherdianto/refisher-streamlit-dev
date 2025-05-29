# modules/articles_content/artikel_3.py
import streamlit as st
import os # Penting: Pastikan baris ini ada untuk os.path.exists()

def show_artikel_3():
    # Judul Artikel Utama
    st.subheader("Cara Menyimpan Ikan Agar Tetap Segar Lebih Lama")
    st.markdown("---") # Garis pemisah untuk visualisasi

    image_path = ".streamlit/static/Gambar-Artikel3.jpg"
    
    # Periksa apakah file gambar ada sebelum ditampilkan
    if not os.path.exists(image_path):
        st.error(f"Error: Gambar artikel '{os.path.basename(image_path)}' tidak ditemukan. Pastikan file ada di lokasi yang benar: '{os.path.abspath(image_path)}'.")
    else:
        # Menampilkan gambar dengan use_container_width
        st.image(image_path, caption="Penyimpanan ikan yang tepat sangat penting", use_container_width=True)
    
    # Paragraf Isi Artikel
    st.write(
        """
        Menyimpan ikan dengan benar adalah langkah krusial untuk **mempertahankan kualitas dan rasa**nya agar tetap segar
        lebih lama. Dengan teknik penyimpanan yang tepat, Anda dapat memastikan ikan tetap lezat dan aman dikonsumsi
        selama beberapa hari, atau bahkan berbulan-bulan jika dibekukan.
        """
    )

    st.markdown("Berikut adalah langkah-langkah efektif untuk menyimpan ikan agar kesegarannya terjaga:")

    st.markdown("""
    1.  **Bersihkan Segera Setelah Dibeli:**
        * Begitu ikan tiba di rumah, segera bersihkan. Buang **isi perut dan insang**, karena bagian ini adalah yang pertama membusuk dan mengandung banyak bakteri.
        * **Bilas ikan dengan air dingin** yang mengalir hingga bersih. Hindari penggunaan air hangat.
        * **Keringkan ikan secara menyeluruh** menggunakan tisu dapur bersih atau kain bersih. Kelembapan adalah musuh utama kesegaran ikan, karena dapat mempercepat pertumbuhan bakteri.
    2.  **Penyimpanan di Kulkas (Jangka Pendek 1-2 Hari):**
        * Bungkus setiap ikan secara individual dengan **plastik *wrap*** atau kertas lilin.
        * Tempatkan ikan yang sudah dibungkus ke dalam wadah kedap udara atau kantong plastik *ziplock*.
        * Tambahkan **es batu** di sekeliling ikan di dalam wadah untuk menjaga suhu tetap sangat rendah (ideal: 0–4°C).
        * Letakkan wadah di bagian **paling dingin** dari kulkas Anda (biasanya di rak paling bawah atau laci khusus daging).
    3.  **Penyimpanan di *Freezer* (Jangka Panjang 2-3 Bulan):**
        * Untuk penyimpanan lebih dari 1-2 hari, **bekukan ikan**.
        * Pastikan ikan bersih dan kering sebelum dibekukan.
        * Bungkus ikan dengan rapat menggunakan **plastik vakum** atau masukkan ke dalam kantong *freezer* tebal yang kedap udara, usahakan tidak ada udara yang terperangkap.
        * Simpan di *freezer* pada suhu **-18°C atau lebih rendah**. Pembekuan yang tepat dapat mempertahankan kualitas ikan hingga 2-3 bulan, atau bahkan lebih lama untuk jenis ikan tertentu.
    """)

    # Paragraf Penutup
    st.write(
        """
        Selalu pastikan ikan tetap dingin selama seluruh proses penyimpanan. Hindari membiarkan
        ikan berada di suhu ruangan terlalu lama, karena ini adalah pemicu utama pembusukan.
        Dengan menerapkan tips penyimpanan ini, Anda dapat memastikan kualitas, tekstur, dan
        rasa ikan tetap terjaga hingga saatnya siap diolah menjadi hidangan lezat.
        """
    )

    st.info(
        """
        💡 **Ingin Memastikan Ikan Anda Layak Disimpan?**
        Sebelum menyimpan, gunakan aplikasi **ReFisher** untuk memeriksa kesegaran awal ikan
        melalui foto mata ikan. Ini akan membantu Anda memastikan hanya ikan yang benar-benar
        segar yang Anda simpan, sehingga hasil akhirnya lebih baik dan aman untuk dikonsumsi!
        """
    )
    st.markdown("---")