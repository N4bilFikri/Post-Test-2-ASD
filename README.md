# Post Test 2 ASD

Deskripsi Singkat

Program ini adalah sebuah program Python yang menggunakan algoritma linear search untuk mencari data pada sebuah list yang telah didefinisikan sebelumnya. Data yang dicari adalah sebagai berikut:

- Nama "Arsel" di index ke-0, nama "Avivah" di index ke-1, dan nama "Daiva" di index ke-2 dari list tersebut.

- String "Wahyu" di index ke-0 pada list yang berada di index ke-3 dari list utama.

- String "Wibi" di index ke-1 pada list yang berada di index ke-3 dari list utama.

-------------------------------------------------------------------------------------------------------------------------------
Cara Kerja Program

Pada program ini terdiri dari satu fungsi yaitu 'linear_search()' dan sebuah list yang bernama 'var'. Fungsi dari 'linear_search()' digunakan untuk melakukan pencarian linear pada sebuah list untuk mencari nilai yang dicari. Fungsi ini menerima dua parameter yaitu sebuah list dan sebuah nilai yang akan dicari pada list tersebut.

Pada fungsi 'linear_search()'dipanggil sebanyak tiga kali dengan parameter yang berbeda untuk mencari tiga nilai yang berbeda pada list 'var'. Output program yang dihasilkan sesuai dengan data yang dicari pada program.

-------------------------------------------------------------------------------------------------------------------------------
Fungsionalitas Program

Program di atas berfungsi untuk mencari data-data tertentu pada sebuah list yang sudah didefinisikan sebelumnya. Terdapat lima data yang ingin dicari, yaitu "Arsel", "Avivah", "Daiva", "Wahyu", dan "Wibi", masing-masing pada indeks yang berbeda pada list.

Program ini cukup fleksibel, karena kita dapat mencari data apapun pada list yang kita inginkan hanya dengan memodifikasi elemen input pada program.            Selain itu, program ini cukup efektif untuk list dengan jumlah elemen yang sedikit, meskipun pada list yang sangat besar kemungkinan memakan waktu eksekusi yang menjadi lambat.

-------------------------------------------------------------------------------------------------------------------------------
Algoritma Yang Digunakan

Algoritma yang digunakan dalam program ini adalah algoritma linear search. Algoritma ini bekerja dengan cara memeriksa setiap elemen pada sebuah list secara berurutan hingga menemukan elemen yang dicari atau sampai habis. Jika elemen yang dicari sudah ditemukan, maka algoritma akan mengembalikan indeks dari elemen tersebut dalam list. Jika elemen tidak ditemukan, maka algoritma akan mengembalikan nilai -1.

-------------------------------------------------------------------------------------------------------------------------------
Elemen Yang Digunakan 

1. 'var' - Sebuah list yang berisi beberapa data yang akan dicari pada program.
2. 'linear_search(arr, x)' - Fungsi untuk melakukan pencarian linear pada sebuah list. Fungsi ini menerima dua parameter yaitu sebuah list dan sebuah nilai yang akan dicari pada list tersebut.
3. 'range(len(arr))' - Fungsi range() digunakan untuk menghasilkan urutan bilangan dari 0 hingga panjang list arr.
4. 'if arr[i] == x' - Digunakan untuk memeriksa apakah elemen yang sedang diperiksa saat ini sama dengan nilai yang dicari. Jika ya, maka fungsi akan mengembalikan indeks elemen tersebut. Jika tidak, maka fungsi akan terus mencari hingga habis.
5. 'print()' - Fungsi untuk mencetak output pada program.
