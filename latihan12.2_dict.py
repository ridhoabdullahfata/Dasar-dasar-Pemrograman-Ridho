# nested dictionary
siswa = {
    's1' : {'nama' : 'Dower','nilai' : 85},
    's2' : {'nama' : 'cipung','nilai' : 90},
    's3' : {'nama' : 'malih','nilai' : 70},
    's4' : {'nama' : 'agoy','nilai' : 79},
    's5' : {'nama' : 'nan','nilai' : 100},
}

hasil = []

print("ID\tNama\t\tNilai")
for id, data in siswa.items() : 
    nama = data ['nama']
    nilai = data ['nilai']
    print(f'{id}\t{nama}\t{nilai}')

#Proses penilaian dan status
for id, data in siswa.items():
    nama = data['nama']
    nilai = data['nilai']

    status = ('Gagal', 'Lulus') [nilai >80]
    #menentukan grade berdasarkan nilai
    if 90 <= nilai <= 100:
        grade = 'A'
    elif 80 <= nilai < 90:
        grade = 'B'
    elif 70 <= nilai < 80:
        grade = 'C'
    elif 60 <= nilai < 70:
        grade = 'D'
    else:
        grade = 'E'

    #menentukan predikat berdasarkan grade
    match grade:
        case 'A' : predikat = 'Sangat Baik'
        case 'B' : predikat = 'Baik'
        case 'C' : predikat = 'Cukup'
        case 'D' : predikat = 'Kurang'
        case 'E' : predikat = 'Sangat Kurang'

    hasil.append((id, nama, nilai, status, grade, predikat))

#menampilkan hasil
print('\nHasil Evaluasi Nilai Siswa')
print("ID\tNama\tNilai\tStatus\tGrade\tPredikat")
print("================================================")

for data in hasil:
    id, nama, nilai, status, grade, predikat = data
    print(f"{id}\t{nama}\t{nilai}\t{status}\t{grade}\t{predikat}")