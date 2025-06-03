# modules/articles_content/artikel_2.py
import streamlit as st
import os # Penting: Pastikan baris ini ada untuk os.path.exists()

def show_artikel_2():
    # Judul Artikel Utama
    st.subheader("Bahaya Mengonsumsi Ikan Tidak Segar")
    st.markdown("---") # Garis pemisah untuk visualisasi

    image_path = ".streamlit/static/Gambar-Artikel2.jpg"
    
    # Periksa apakah file gambar ada sebelum ditampilkan
    if not os.path.exists(image_path):
        st.error(f"Error: Gambar artikel '{os.path.basename(image_path)}' tidak ditemukan. Pastikan file ada di lokasi yang benar: '{os.path.abspath(image_path)}'.")
    else:
        # Menampilkan gambar dengan use_container_width
        st.image(image_path, caption="Ikan tidak segar dapat membahayakan kesehatan", use_container_width=True)
    
    # Paragraf Isi Artikel
    st.write(
        """
        Mengonsumsi ikan yang **tidak segar** dapat menimbulkan risiko serius bagi kesehatan Anda.
        Bahaya ini bervariasi mulai dari gangguan pencernaan ringan hingga keracunan makanan yang membutuhkan penanganan medis serius.
        """
    )

    st.write(
        """
        Ikan yang sudah mulai membusuk seringkali menjadi media yang ideal bagi pertumbuhan bakteri berbahaya.
        Bakteri seperti ***Salmonella***, ***Vibrio parahaemolyticus***, atau ***Clostridium botulinum*** dapat berkembang biak
        dengan cepat pada ikan yang tidak disimpan atau ditangani dengan benar.
        Konsumsi ikan yang terkontaminasi ini dapat menyebabkan gejala seperti mual, muntah, diare,
        kram perut, dan dalam kasus yang parah, infeksi sistemik yang membutuhkan rawat inap.
        """
    )

    st.write(
        """
        Risiko keracunan ikan ini sangat tinggi terutama jika ikan tidak disimpan pada suhu dingin
        yang memadai atau telah melewati masa kesegarannya. Gejala keracunan bisa muncul dengan cepat,
        seringkali dalam hitungan jam setelah mengonsumsi ikan yang terkontaminasi.
        Waspadai tanda-tanda seperti bau amis yang sangat menyengat, tekstur daging yang lembek,
        atau mata ikan yang keruh, karena ini adalah indikator kuat bahwa ikan sudah tidak layak konsumsi.
        """
    )

    # Paragraf Penutup dan CTA
    st.write(
        """
        Untuk melindungi diri dan keluarga dari bahaya ini, **selalu prioritaskan kesegaran ikan**.
        Pilih ikan dengan ciri mata jernih, sisik mengkilap, dan bau segar.
        Segera setelah membeli, simpan ikan pada suhu dingin yang tepat untuk memperlambat
        pertumbuhan bakteri.
        """
    )

    st.info(
        """
        💡 **Pastikan Keamanan Konsumsi Ikan Anda!**
        Gunakan aplikasi **ReFisher** untuk membantu Anda memeriksa kesegaran ikan dengan cepat
        hanya melalui foto mata ikan. Teknologi AI kami akan memberikan prediksi akurat
        sehingga Anda bisa terhindar dari risiko kesehatan yang tidak diinginkan dan
        menikmati hidangan laut yang aman dan lezat.
        """
    )
    st.markdown("---")