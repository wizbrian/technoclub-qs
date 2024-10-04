"""
Mencari Makanan di Hutan

Penduduk Pulau Tara meminta bantuanmu untuk menghitung berapa banyak buah yang ada di hutan. 
Mereka memiliki daftar jumlah buah yang ditemukan setiap hari selama seminggu, 
dan mereka butuh bantuanmu untuk mengetahui jumlah total buah yang dikumpulkan selama seminggu.

Contoh
Input:
[10, 20, 30, 40, 50, 60, 70]

Output:
Total buah yang dikumpulkan selama seminggu adalah 280
"""
buah = []
for i in range(7):
    jumlah = int(input(f"Masukkan jumlah buah yang ditemukan pada hari ke-{i + 1}: "))
    buah.append(jumlah)
total_buah = sum(buah)
print(f"Total buah yang dikumpulkan selama seminggu adalah {total_buah}")