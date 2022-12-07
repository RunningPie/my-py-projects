#Program Deposit cash
"""
====Kamus====
saldoakhir = integer = untuk menyimpan data akhir
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

def DepositCash(norek, jumlah, controller):
    if __name__ == "__main__" :
        sistem_operasi = os.name

        match sistem_operasi :
            case "posix": os.system("clear")
            case "nt" : os.system("cls")

    df = pd.read_csv('data_atm.csv')
    saldoakhir = 0
    n = 0
    # tes = True
    # while n<3 :
    #     try :
    # norek = int(input("Masukkan no rekening :")) 
    cek_rekening = df[(df['rekening'] == norek)]
    saldoawal = cek_rekening.iloc[0,1]
    print(f"saldo awal anda adalah  : {saldoawal}")
    #         if saldoawal >= 0 :
    #             break
    #     except :
    #         n+= 1
    #         print("Nomor rekening tidak ditemukan, silahkan masukkan nomor rekening ulang!")
            
    # if n >= 3 :
    #     print("rekening Anda tidak ditemukan")
    #     exit()
    nomor = df.index[df['rekening'] == norek].tolist()
    print("Pilih jumlah yang ingin disetorkan :")
    print(" 1. Rp100.000")
    print(" 2. Rp200.000")
    print(" 3. Rp300.000")
    print(" 4. Rp400.000")
    print(" 5. Rp500.000")

    saldoakhir = saldoawal + jumlah

    df.iloc[nomor,1] = saldoakhir
    df.to_csv('data_atm.csv', index = False)
    print(f"Saldo akhir Anda adalah : {saldoakhir}") 
    hari_ini = dt.date.today()

    df = pd.read_csv('data_history.csv')

    datagcdic = [
        {"nomor" : len(df.index)+1, 
        "rekening" : norek, 
        "tanggal" : hari_ini, 
        "tipe_transaksi" : "Deposit_Cash",
        "debit_kredit" : "K",
        "jumlah": jumlah,
        "saldo" : saldoakhir }
        ]

    df = pd.DataFrame(datagcdic)

    df.to_csv('data_history.csv', mode='a', index=False, header=False)
    
    controller.tampilkan_frame("Successful")
    
    return saldoakhir
