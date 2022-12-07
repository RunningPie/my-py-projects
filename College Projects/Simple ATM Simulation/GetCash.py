#Program Menarik Uang
"""
====Kamus====
saldoakhir = integer = untuk menyimpan data akhir
tes = boolean = untuk menegecek perulangan ketika memasukkan
                saldo yang ingin ditarik
nomor = integer = index dari pandas
cek_rekening = integer = untuk mengecek kesesuaian nomor rekening yang
                         diinput dengan inputan user
norek = integer = inputan nomor rekening pengguna
n = integer = jumlah perulangan maksimal ketika user menginput
              nomor rekening
data_atm.csv = data yang digunakan berfungsi sebagai database

"""
import csv
import pandas as pd
import numpy as np
import os
import datetime as dt
from terjemahkan import terjemahkan

def GetCash(norek, jumlah, controller, bahasa, label):
    if __name__ == "__main__" :
        sistem_operasi = os.name

        match sistem_operasi :
            case "posix": os.system("clear")
            case "nt" : os.system("cls")

    df = pd.read_csv('data_atm.csv')
    # n = 0
    tes = True
    # while n<3 :
    # try :
    # norek = int(input("Masukkan no rekening :")) 
    cek_rekening = df[(df['rekening'] == norek)]
    saldoawal = cek_rekening.iloc[0,1]
    print(f"saldo awal anda adalah  : {saldoawal}")
    saldoakhir = saldoawal
    # if saldoawal >= 0 :
    #     break
    # except :
    #     #n+= 1
    #     label.configure(text=terjemahkan("Nomor rekening tidak ditemukan, silahkan masukkan nomor rekening ulang!", bahasa),
    #                     fg="red", bg="white", font=controller.headingOneFont)
    #     print("Nomor rekening tidak ditemukan, silahkan masukkan nomor rekening ulang!")
            
    # if n >= 3 :
    #     print("rekening Anda tidak ditemukan")
    #     exit()
    nomor = df.index[df['rekening'] == norek].tolist()
    print("Pilih jumlah penarikan :")
    print(" 1. Rp100.000")
    print(" 2. Rp200.000")
    print(" 3. Rp300.000")
    print(" 4. Rp400.000")
    print(" 5. Rp500.000")
    # print(" 6. Rp1.500.000")
    # print(" 7. Rp2.000.000")
    # option = int(input("Silahkan pilihan menu :"))
    # # if option == 1 :
    #     x = 100000
    # elif option == 2 :
    #     x = 200000
    # elif option == 3 :
    #     x = 300000
    # elif option == 4 :
    #     x = 400000
    # elif option == 5 :
    #     x = 500000

    if saldoawal > jumlah :
        saldoakhir = saldoawal - jumlah
        df.iloc[nomor,1] = saldoakhir
        df.to_csv('data_atm.csv', index = False)
        print(f"Saldo akhir Anda adalah : {saldoakhir}") 
        hari_ini = dt.date.today()
        datagcdic = [
            {"nomor" : len(df.index)+1 , 
            "rekening" : norek, 
            "tanggal" : hari_ini, 
            "tipe transaksi" : "Get_Cash",
            "debit_kredit" : "D",
            "jumlah": jumlah,
            "saldo" : saldoakhir }
            ]
        df = pd.DataFrame(datagcdic)
        df.to_csv('data_history.csv', mode='a', index=False, header=False)
        
        controller.tampilkan_frame("Successful")
    else :
        # n += 1
        # if n>= 3 :
        #     print("Invalid input")
        #     exit()
        label.configure(text=terjemahkan("Saldo Anda tidak cukup, silahkan pilih nominal lagi!", bahasa),
                    fg="red", bg="white", font=controller.headingOneFont)
        label.after(5000, lambda: label.configure(fg="dark blue", bg="dark blue"))
        
        print("Saldo anda tidak cukup, silahkan pilih nominal lagi!")
    
    return saldoakhir
