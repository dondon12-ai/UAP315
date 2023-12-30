# UAP315

## Data yang digunakan
![Screenshot (14)](https://github.com/dondon12-ai/UAP315/assets/92214578/1f52d019-cae4-44dd-9cfc-257cc95aac40)

-Data income memiliki 43957 entry dan 15 atribut diantaranya:

-age: Umur seseorang dalam tahun.

-workclass: Kategori yang menggambarkan kelas pekerjaan atau jenis pekerjaan seseorang (e.g., "Private", "Government", "Self-employed").

-fnlwgt: Sebuah angka yang merupakan faktor perampingan (tidak jelas kegunaannya tanpa konteks lebih lanjut).

-education: Tingkat pendidikan tertinggi yang telah dicapai (e.g., "Bachelors", "Masters", "Doctorate").

-educational-num: Jumlah tahun pendidikan yang telah diselesaikan.

-marital-status: Status perkawinan seseorang (e.g., "Married", "Single", "Divorced").

-occupation: Jenis pekerjaan atau profesi seseorang (e.g., "Tech-support", "Craft-repair", "Exec-managerial").

-relationship: Hubungan seseorang dalam keluarga (e.g., "Husband", "Wife", "Own-child").

-race: Ras atau etnisitas seseorang (e.g., "White", "Black", "Asian-Pac-Islander").

-gender: Jenis kelamin seseorang (e.g., "Male", "Female").

-capital-gain: Keuntungan finansial dari aset (dalam dolar).

-capital-loss: Kerugian finansial dari aset (dalam dolar).

-hours-per-week: Jumlah jam kerja per minggu.

-native-country: Negara asal atau negara kelahiran seseorang.

-income_>50K: Target variabel yang menunjukkan apakah pendapatan seseorang melebihi $50,000 per tahun atau tidak (1 untuk ya, 0 untuk tidak).

## Model yang digunakan(RandomForest)
![Random Forest Classifier](https://www.spotfire.com/content/dam/spotfire/images/graphics/inforgraphics/random-forest-diagram.svg)

Random Forest Classifier adalah sebuah algoritma klasifikasi dalam machine learning yang membangun sejumlah besar decision tree selama pelatihan dan menggabungkan hasil prediksi dari setiap pohon untuk menghasilkan prediksi akhir. Dalam proses ini, sampel acak diambil dari kumpulan data pelatihan dengan penggantian, dan untuk setiap sampel yang diambil, sebuah pohon keputusan dibangun dengan memilih fitur terbaik secara acak untuk membagi simpul-simpul dalam pohon. Setelah pembangunan pohon selesai, hasil prediksi dari setiap pohon digunakan untuk menentukan prediksi akhir dengan menggunakan metode voting atau penggabungan. Kelebihan Random Forest meliputi kemampuan menangani jumlah fitur yang besar, mengurangi overfitting, dan memberikan estimasi kepentingan fitur. Algoritma ini sering digunakan dalam berbagai aplikasi machine learning karena kinerjanya yang stabil dan kuat.

## Hasil Evaluasi Model

![Screenshot (15) (1)](https://github.com/dondon12-ai/UAP315/assets/92214578/d8323e5f-1d50-4d98-a9be-c6c128285679)



## Instalasi

1. clone repository ini
2. jalankan model.py
3. jalankan app.py
4. akses http://127.0.0.1:5000/

## Penggunaan

1. masukan value pada masing-masing fitur
2. klik predict
3. maka hasil klassifikasi income akan muncul (0 = tidak lebih dari 50k, 1 = lebih dari 50k)
