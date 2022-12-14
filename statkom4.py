#SOAL
#Tujuh kaleng masing-masing berisi asam sulfat sebanyak 9,8; 10,2; 10,4; 9,8; 10,0;
#10,2; dan 9,6 liter. Tentukan selang kepercayaan 95% bagi nilai tengah isi semua
#kaleng jika isi kaleng-kaleng tersebut menyebar normal!
#Hitung ragam sampelnya



# mengimport library statistik
import statistics

# menentukan daftar isi kaleng
isi_kaleng = [9.8, 10.2, 10.4, 9.8, 10.0, 10.2, 9.6]

# menghitung rata-rata isi kaleng
rata_rata = statistics.mean(isi_kaleng)

# menghitung jumlah kaleng
n = len(isi_kaleng)

a = 5
b = 100
hasil_persen = a / b

c = 2
hasil_persen1 = hasil_persen / c


# menghitung ragam sampel dari isi kaleng
ragam_sampel = sum((x - rata_rata) ** 2 for x in isi_kaleng) / (n - 1)

# menghitung standar deviasi isi kaleng
stdev = statistics.stdev(isi_kaleng)

# menghitung selang kepercayaan 95% bagi nilai tengah isi kaleng
selang_kepercayaan = 1.96 * stdev / (len(isi_kaleng) ** 0.5)

# menghitung selang kepercayaan 99% bagi nilai tengah isi kaleng
selang_kepercayaan = 1.96 * stdev / (len(isi_kaleng) ** 0.1)

# mencetak hasil
print()
print("\tSelang kepercayaan untuk varians populasi")
print()
print("Sampel " + str(isi_kaleng))
print()

print("Hasil persen : " + str(hasil_persen))
print("Hasil 95% : " + str(hasil_persen1))

print("Ragam sampel dari isi kaleng-kaleng : " + str(ragam_sampel))
print()
print("Selang kepercayaan 95% bagi nilai tengah isi semua kaleng : ")
print("(" + str(rata_rata - selang_kepercayaan) + " <  µ < " + str(rata_rata + selang_kepercayaan) + ")")
print()
print("Derajat bebas: "+ str(n - 1))