# 🐟 ReFisher - Klasifikasi Kesegaran Ikan

Aplikasi web interaktif untuk mengklasifikasikan kesegaran ikan menggunakan teknologi Computer Vision dan Deep Learning. Proyek ini menggunakan TensorFlow Lite untuk inference dan Streamlit untuk antarmuka pengguna yang menarik.

## 📋 Deskripsi Proyek

ReFisher adalah sistem klasifikasi otomatis yang dapat menentukan kesegaran ikan berdasarkan analisis citra mata ikan. Model machine learning yang digunakan telah dilatih menggunakan dataset dari Roboflow Universe dengan dua kelas utama:

- **Fresh Fish**: Ikan dalam kondisi segar dan layak konsumsi
- **Non Fresh Fish**: Ikan dalam kondisi tidak segar dan tidak layak konsumsi

## 🎯 Fitur Utama

- ✨ **Interface yang Menarik**: Desain modern dan responsif menggunakan Streamlit
- 🤖 **AI-Powered Classification**: Menggunakan TensorFlow Lite untuk inference yang cepat
- 📊 **Visualisasi Interaktif**: Grafik confidence score menggunakan Plotly
- 🎨 **Image Enhancement**: Tools untuk meningkatkan kualitas gambar sebelum prediksi
- 📱 **Responsive Design**: Dapat diakses dari berbagai perangkat
- 💡 **Rekomendasi Cerdas**: Memberikan saran berdasarkan hasil klasifikasi

## 🔧 Teknologi yang Digunakan

- **Frontend**: Streamlit dengan custom CSS
- **Machine Learning**: TensorFlow Lite
- **Image Processing**: PIL (Python Imaging Library)
- **Visualization**: Plotly
- **Data Processing**: NumPy
- **Deployment**: Python 3.8+

## 📊 Dataset

Dataset yang digunakan berasal dari [Roboflow Universe](https://universe.roboflow.com/meva-wfywb/fish-fresh-and-non-fresh) dengan karakteristik:

- **Total Classes**: 2 (Fresh Fish, Non Fresh Fish)
- **Data Split**: Train, Test, dan Validation
- **Focus**: Analisis citra mata ikan untuk menentukan kesegaran
- **Format**: Gambar dengan berbagai resolusi

## 🚀 Instalasi dan Penggunaan

### Prerequisites

```bash
Python 3.8 atau lebih tinggi
pip (Python package manager)
```

### Langkah Instalasi

1. **Clone atau download repository**
```bash
cd capstone-laskarai-streamlit-dev
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Pastikan model TensorFlow Lite tersedia**
```
Pastikan file model.tflite ada di direktori root
```

4. **Jalankan aplikasi**
```bash
streamlit run app.py
```

5. **Akses aplikasi**
```
Buka browser dan kunjungi: http://localhost:8501
```

## 📖 Cara Penggunaan

1. **Upload Gambar**: Pilih gambar ikan yang ingin diklasifikasi
2. **Enhancement (Opsional)**: Atur kontras dan brightness untuk hasil yang lebih baik
3. **Analisis**: Tunggu proses analisis AI selesai
4. **Hasil**: Lihat prediksi, confidence score, dan rekomendasi
5. **Visualisasi**: Analisis grafik confidence untuk setiap kelas

## 🎨 Fitur UI/UX

- **Gradient Headers**: Header dengan efek gradient yang menarik
- **Color-Coded Results**: Hasil prediksi dengan kode warna yang intuitif
- **Progress Indicators**: Progress bar untuk feedback real-time
- **Interactive Charts**: Grafik interaktif untuk analisis mendalam
- **Responsive Layout**: Tampilan yang optimal di berbagai ukuran layar
- **Custom Styling**: CSS kustom untuk pengalaman pengguna yang premium

## 📁 Struktur Proyek

```
capstone-laskarai-streamlit-dev/
├── app.py                 # Aplikasi utama Streamlit
├── model.tflite          # Model TensorFlow Lite
├── requirements.txt      # Dependencies Python
├── .streamlit/
│   └── config.toml      # Konfigurasi Streamlit
└── README.md            # Dokumentasi proyek
```

## 🔬 Detail Teknis

### Model Architecture
- **Framework**: TensorFlow Lite
- **Input Size**: Dinamis (disesuaikan dengan model)
- **Output**: Probabilitas untuk 2 kelas
- **Preprocessing**: Normalisasi dan resize otomatis

### Performance
- **Inference Time**: < 1 detik per gambar
- **Memory Usage**: Optimized untuk deployment
- **Compatibility**: Cross-platform (Windows, macOS, Linux)

## 🤝 Kontribusi

Proyek ini adalah bagian dari capstone project. Untuk kontribusi atau saran:

1. Fork repository
2. Buat feature branch
3. Commit changes
4. Push ke branch
5. Create Pull Request

## 📞 Support

Jika mengalami masalah atau memiliki pertanyaan:

- **Issues**: Gunakan GitHub Issues untuk bug reports
- **Documentation**: Baca dokumentasi lengkap di README
- **Community**: Bergabung dengan diskusi di repository

## 📄 Lisensi

Proyek ini dibuat untuk tujuan edukasi dan penelitian. Penggunaan dataset mengikuti ketentuan dari Roboflow Universe.

## 🙏 Acknowledgments

- **Roboflow Universe** untuk dataset fish freshness
- **TensorFlow Team** untuk framework machine learning
- **Streamlit Team** untuk framework web application
- **Open Source Community** untuk tools dan libraries yang digunakan

---

**© 2025 ReFisher - Computer Vision untuk Klasifikasi Kesegaran Ikan**
