#memanggil module textable 
#agar hasil yang di print membentuk table
from texttable import Texttable
jawab = "y" #pariable untuk melakukan pengulangan mengisi nilai dan identitas
table = Texttable() #variabel module texttable
no = 0 #variable untuk penomeran
nama = [] #variable list nama
nim = [] #list nim
n_tugas = [] #list nilai tugas
n_uts = [] #list nilai uts
n_uas = [] #list nilai uas
#pengulangan while untuk memasukan data
while( jawab == "y"):
    nama.append(input("Nama :")) #menambahkan nilai pada list nama
    nim.append(input("Nim :"))  #menambahkan nilai pada list nim
    n_tugas.append(input("Nilai Tugas :"))  #menambahkan nilai pada list nilai tugas
    n_uts.append(input("Nilai UTS :")) #menambahkan nilai pada list nilai uts
    n_uas.append (input("Nilai UAS :"))  #menambahkan nilai pada list nilai uas
    jawab = input("Tambah data (y/t)?") #jika menekan y maka akan mengulang kembali
    no += 1 #merubah nilai variable no
for n in range(no):
    akhir = (float(n_tugas[n])*30/100) + (float(n_uts[n])*35/100) + (float(n_uas[n])*35/100) #perhitungan nilai akhir
    #mennambahkan data pada list kedalam tabel
    table.add_rows([['No','Nama','Nim','Nilai Tugas','Nilai UTS','Nilai UAS','Nilai Akhir'],[n+1, nama[n], nim[n], n_tugas[n], n_uts[n], n_uas[n],akhir]])
table.set_chars(['=','|','=','='])
print(table.draw()) #menampilkan table pada layar
