import random
import datetime
from customer import Customer

atm = Customer(id, 1234, 10000)

while True :
    id = int(input("Silahkan Masukkan Nomor Pin Anda: "))
    trial = 0

    while (id != int(atm.cek_pin()) and trial < 3):
        id = int(input("Pin Anda Salah!\nMasukkan Pin Lagi: "))
        trial += 1
        if trial == 3:
            print("Error!!\nSilahkan Ambil Kartu dan Coba Lagi..")
            exit()
    
    while (id == int(atm.cek_pin())):
        print("Selamat Datang")
        print("Menu ATM :\n1.Cek Saldo\n2.Debet\n3.Simpan Uang\n4.Ganti Pin\n5.Keluar..")
        pilihan = int(input("Pilihan Transaksi: "))
        
        if pilihan == 1 :
            print("Jumlah Saldo Anda: Rp." + str(atm.cek_saldo()))
        
        elif pilihan == 2 :
            uangDebet = int(input("Masukkan Jumlah Uang yang akan didebet: Rp."))
            if uangDebet < int(atm.cek_saldo()) :
                print("Sisa Saldo Anda: Rp." + str(atm.debet(uangDebet)))
            else :
                print("Uang Anda Tidak Cukup!")
        
        elif pilihan == 3 :
            uangSimpan = int(input("Masukkan Jumlah Uang yang akan Disimpan: Rp."))
            print("Uang Berhasil Disimpan!")
            print("Jumlah Uang Anda: Rp." + str(atm.simpan(uangSimpan)))
        
        elif pilihan == 4 :
            newPin = int(input("Masukkan Pin Baru yang akan Diubah: "))
            atm.ubahPin(newPin)
        
        elif pilihan == 5:
            print("Terima Kasih Telah Melakukan Transaksi!!")
            print("---- No. Rec " + str(random.randint(100000, 1000000)) + " ----")
            print("Tanggal dan Waktu: " + str(datetime.datetime.now()))
            print("Saldo Akhir Anda: Rp. " + str(atm.cek_saldo()))
            exit()
        
        else:
            print("Masukkan Pilihan Menu yang Benar!!")
