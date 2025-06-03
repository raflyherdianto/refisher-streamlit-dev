# modules/articles_content/artikel_1.py
import streamlit as st
import os # Penting: Pastikan baris ini ada untuk os.path.exists()

def show_artikel_1():
    st.subheader("Ciri-Ciri Ikan Segar yang Perlu Kamu Ketahui")
    st.markdown("---")

    image_path = ".streamlit/static/Gambar-Artikel1.jpg"
    
    if not os.path.exists(image_path):
        st.error(f"Error: Gambar artikel '{os.path.basename(image_path)}' tidak ditemukan. Pastikan file ada di lokasi yang benar: '{os.path.abspath(image_path)}'.")
    else:
        st.image(image_path, caption="Ikan segar di pasar tradisional", use_container_width=True)
    
    # Paragraf Pembuka
    st.write(
        """
        Mengetahui kesegaran ikan adalah kunci untuk memastikan kualitas dan keamanan makanan yang akan Anda konsumsi.
        Ikan segar memiliki ciri-ciri khusus yang mudah dikenali jika Anda tahu apa yang harus diperhatikan dengan cermat.
        """
    )

    # Poin-poin Ciri-Ciri Ikan Segar
    st.markdown("Berikut adalah beberapa ciri utama ikan segar yang perlu Anda ketahui:")

    st.markdown("""
    * **Mata Ikan:** Perhatikan matanya. Ikan segar memiliki mata yang **jernih, bening, bulat, dan menonjol**. Jika mata ikan terlihat keruh, cekung, atau bahkan berwarna putih susu, itu adalah tanda kuat bahwa ikan sudah tidak segar.
    * **Insang Ikan:** Angkat penutup insang dan periksa. Insang ikan segar berwarna **merah cerah** dan bersih, tanpa lendir. Jika insang terlihat pucat, keabu-abuan, atau ditutupi lendir tebal, hindari ikan tersebut.
    * **Sisik dan Kulit:** Ikan segar memiliki **sisik yang mengkilap, menempel erat** pada kulit, dan terasa licin. Kulitnya juga tampak cerah sesuai jenis ikannya. Jika sisik mudah lepas atau kulit terlihat kusam dan lengket, kesegarannya diragukan.
    * **Aroma Ikan:** Cium aroma ikan. Ikan segar memiliki **bau laut yang segar dan bersih**, tidak amis menyengat atau busuk. Jika baunya tajam dan tidak sedap (seperti amonia), sebaiknya hindari membeli ikan tersebut.
    * **Daging Ikan:** Sentuh daging ikan. Daging ikan segar terasa **kenyal dan elastis** saat ditekan, serta akan kembali ke bentuk semula dengan cepat. Jika daging terasa lembek atau meninggalkan bekas jari, itu tanda ikan sudah tidak segar.
    """)

    # Paragraf Penutup dan CTA
    st.write(
        """
        Dengan memperhatikan ciri-ciri di atas, Anda dapat dengan mudah memilih ikan yang segar dan berkualitas untuk kebutuhan Anda. Pastikan juga untuk menyimpan ikan dengan benar agar kesegarannya tetap terjaga hingga saat dimasak.
        """
    )

    st.info(
        """
        💡 Ingin cara lebih cepat dan mudah?
        Gunakan aplikasi **ReFisher** untuk membantu Anda memeriksa kesegaran ikan secara instan
        hanya melalui foto mata ikan. Teknologi AI kami akan memberikan prediksi akurat
        sehingga Anda tidak perlu ragu lagi saat membeli ikan.
        """
    )
    st.markdown("---")