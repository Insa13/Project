import random
import datetime
from Customer import Customer

atm = Customer(id)

while True:
 
    id = int(input("Masukkan pin anda: "))
    trial = 0

    while (id != int(atm.checkPin())and trial < 3):
        id = int(input("Pin and salah. Silakan Masukkan lagi: "))
        trial += 1

        if trial == 3 : 
            print("Error. Silakan ambil kartu dan coba lagi..")
            exit()
    while True:
        print("Selamat datang di ATM Progate..")
        print("\n1 - Cek saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar ")
        select_menu = int(input("\nSilakan pilih menu: "))
        if select_menu == 1:
            print("\nSaldo anda sekarang: Rp. " + str(atm.checkBalance()) + "\n" )
        elif select_menu == 2:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_withdraw = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? y/n " + str(nominal) + " ")

            if verify_withdraw == "y":
                print("Saldo awal anda adalah: Rp. " + str(atm.checkBalance()) + " ") 
            else :
                pass
            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi debet berhasil!")
                print("Saldo sisa sekarang: Rp. " + str(atm.checkBalance()) + " ")
            else:
                print("Maaf. Saldo anda tidak cukup untuk melakukan debet!")
                print("Silakan lakukan penambahan nominal saldo")
        elif select_menu == 3 :
            nominal = float(input("Masukkan nominal saldo: "))
            verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut ? y/n " + str(nominal) + " ")
                    
            if verify_deposit == "y":
                atm.depositBalance(nominal)
                print("Saldo anda sekarang adalah: Rp." + str(atm.checkBalance()) + "\n" )
            else:
                pass
        elif select_menu == 4:
            verify_pin = int(input("masukkan pin anda: "))
             
            while verify_pin != int(atm.checkPin()):
                print("pin anda salah, silakan masukkan pin: ")
            
            updated_pin = int(input("silakan masukkan pin baru: "))
            print("pin anda berhasil diganti!")
                 
            verify_newpin = int(input("coba masukkan pin baru: "))
                    
            if verify_newpin == updated_pin:
                print("pin baru anda sukses!")
            else:
                print("maaf, pin anda salah!")

        elif select_menu == 5:
            print("Resi tercetak otomatis saat anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
            print("No. Rekord: ", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo akhir: ", atm.checkBalance())
            print("Terima kasih telah menggunakan ATM Progate!")
            exit()
        else:
            print("Error. Maaf, menu tidak tersedia")