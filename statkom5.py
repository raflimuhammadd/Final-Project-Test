#SOAL :
#Suatu sampel acak dari 36 mahasiswa tingkat akhir berturut-turut menghasilkan
#ilai tengah dan simpangan baku IPK sebesar 2,6 dan 0,3. Buatlah selang
#Kepercayaan 95% dan 99% untuk nilai tengah IPK seluruh mahasiswa tingkat akhir!




# Nilai tengah dan simpangan baku IPK sampel acak
mean = 2.6
simpangBaku = 0.3

# Jumlah mahasiswa dalam sampel
n = 36

#untuk 95%
a = 5
b = 100
hasil_persen = a / b

c = 2
hasil_persen1 = hasil_persen / c

#untuk 99%
k = 1
j = 100
persen_99 = k / j

m = 2
hasil_persen99 = persen_99 / m


print("Jumlah Sampel : "+str(n))
print("Nilai tengah sampel (x̄ ) : " + str(mean))
print("Simpangan Baku (σ) = " +str(simpangBaku))
print("---")

print()
print("Kepercayaan 95% : "+str(hasil_persen1))
print("Kepercayaan 99% : "+ str(hasil_persen99))
print("----")

# Hitung selang kepercayaan 95%
ci_95 = 1.96 * simpangBaku / (n ** 0.5)
print("Selang kepercayaan 95%:", mean - ci_95, " < µ < ", mean + ci_95)

# Hitung selang kepercayaan 99%
ci_99 = 2.58 * simpangBaku / (n ** 0.5)
print("Selang kepercayaan 99%:", mean - ci_99, " < µ < ", mean + ci_99)

print(mean - 2.58 * simpangBaku / (n ** 0.5))