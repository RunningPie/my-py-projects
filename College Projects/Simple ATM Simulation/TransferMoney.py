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

def TransferMoney(controller, norek, rek_t, option, jumlah, label, bahasa, chances, kode=0):
    if __name__ == "__main__" :
        sistem_operasi = os.name

        match sistem_operasi :
            case "posix": os.system("clear")
            case "nt" : os.system("cls")

    df = pd.read_csv('data_atm.csv')
    df1 = pd.read_csv('data_transaksi.csv')
    saldoakhir1 = 0
    saldoakhir2 = 0
    n = 0
    tes = True
    while n<3 :
        try :
            # norek = int(input("Masukkan no rekening :")) 
            cek_rekening = df[(df['rekening'] == norek)]
            saldoawal1 = cek_rekening.iloc[0,1]
            print(f"saldo awal anda adalah  : {saldoawal1}")
            if saldoawal1 >= 0 :
                break
            if n >= 3 :
                break
        except :
            n+= 1
            if n >= 3 :
                break
            print("Nomor rekening tidak ditemukan, silahkan masukkan nomor rekening ulang!")
            
    if n >= 3 :
        print("rekening Anda tidak ditemukan")
        exit()
    nomor1 = df.index[df['rekening'] == norek].tolist()

    print("Pilih jenis transaksi :")
    print("1. Transaksi antar rekening")
    print("2. Transaksi antar bank")
    print("3. Pembayaran")
    # option = int(input("Silahkan pilihan menu :"))
    if option == 1 :
        # while n<3 :
        #     # rek_t = rek_t
        if rek_t == norek :
            print("Invalid input")
            # exit()
            label.config(text=terjemahkan("Invalid input", bahasa), fg="red", bg="white")
            label.pack()
            chances.set(chances.get()+1) 
        try :
            cek_rekening_tujuan = df[(df['rekening'] == rek_t)]
            saldoawal2 = cek_rekening_tujuan.iloc[0,1]
            # if saldoawal2 >= 0 :
            #     break
            # if n >= 3 :
            #     break
        except :
            print("Nomor rekening tidak ditemukan, silahkan masukkan nomor rekening ulang!" )  
            label.config(text=terjemahkan("Nomor rekening tidak ditemukan, silahkan masukkan nomor rekening ulang!", bahasa),
                         bg = "white", fg = "red")
            label.pack()
            chances.set(chances.get()+1) 
            # n+= 1
            # if n >= 3 :
            #     break
                    
        if chances.get() >= 3 :
            # print("rekening Anda tidak ditemukan")
            label.config(text=terjemahkan("Nomor rekening tidak ditemukan, silahkan coba lagi nanti", bahasa),
                         bg = "white", fg = "red")
            label.pack()
            controller.tampilkan_frame("MainMenu", duration=2500)
            # exit()
        
        nomor2 = df.index[df['rekening'] == rek_t].tolist() 
        # jumlah = int(input("Masukkan jumlah yang ingin ditransfer :"))
        if saldoawal1 >= jumlah :
            saldoakhir1 = saldoawal1 - jumlah
            saldoakhir2 = saldoawal2 + jumlah 
        else : 
            print("Saldo Anda tidak cukup")
        
        df.iloc[nomor2,1] = saldoakhir2
        df.to_csv('data_atm.csv', index = False) 

    elif option == 2 :
        n = 0
        print("Untuk transfer antar bank akan dikenakan biaya tambahan sebesar Rp2.500,- ")
        while n<3 :
            # rek_t = int(input("Masukkan rekening tujuan : "))
            if rek_t == norek :
                print("Invalid input")
                exit()
            try : 
                cek_rekening_tujuan = df[(df['rekening'] == rek_t)]
                saldoawal2 = cek_rekening_tujuan.iloc[0,1]
                print(saldoawal2)
                if saldoawal2 >= 0 :
                    break
                if n >= 3 :
                    break
            except :
                print("Nomor rekening tidak ditemukan, silahkan masukkan nomor rekening ulang!")       
                n+= 1
                if n >= 3 :
                    break
        if n >= 3 :
            print("rekening Anda tidak ditemukan")
            exit()
        nomor2 = df.index[df['rekening'] == rek_t].tolist() 
        # jumlah = int(input("Masukkan jumlah yang ingin dibayarakan :"))
        if saldoawal1 >= jumlah + 2500:
            saldoakhir1 = saldoawal1 - (jumlah + 2500)
            saldoakhir2 = saldoawal2 + jumlah
        else : 
            print("Saldo anda tidak cukup")
        df.iloc[nomor2,1] = saldoakhir2
        df.to_csv('data_atm.csv', index = False) 
    elif option == 3 :
        print("Pilih jenis pembayaran :")
        print("1. Pembayaran Air")
        print("2. Pembayaran Tagihan Listrik")
        print("3. Pembayaran Pulsa/Internet/Wifi")
        # jenis_pembayaran = int(input("Silahkan pilih menu :"))
        while n<3 : 
            try : 
                # kode = int(input("Masukkan kode pembayaran :"))
                nominal_bayar = df1[(df1['kodebayar'] == kode) & df1["rekening"] == norek]
                jumlah = nominal_bayar.iloc[0,3]
                if jumlah >= 0 :
                    break
                if n >= 3 :
                    break
            except :
                print("Kode pembayaran tidak ditemukan, silahkan masukkan kode ulang!")       
                n+= 1
                if n >= 3 :
                    break
        if n >= 3 :
            print("kode pembayaran tidak ditemukan")
            exit()
        saldoakhir1 = saldoawal1 - jumlah
    else :
        print("Invalid input")
        exit()
    
    if option != 3:
        df.iloc[nomor1,1] = saldoakhir1
        df.iloc[nomor2,1] = saldoakhir2
        df.to_csv('data_atm.csv', index = False)
        print(f"Saldo akhir Anda adalah : {saldoakhir1}") 
        
        # Update history transaksi rekening asal
        hari_ini = dt.date.today()
        datagcdic = [
            {"nomor" : len(df.index)+1, 
            "rekening" : norek, 
            "tanggal" : hari_ini, 
            "tipe transaksi" : "Transfer_Money",
            "debit_kredit" : "D",
            "jumlah": jumlah,
            "saldo" : saldoakhir1},
            {"nomor" : len(df.index)+1, 
            "rekening" : rek_t, 
            "tanggal" : hari_ini, 
            "tipe transaksi" : "Transfer_Money",
            "debit_kredit" : "K",
            "jumlah": jumlah,
            "saldo" : saldoakhir2}
            ]
        df = pd.DataFrame(datagcdic)
        df.to_csv('data_history.csv', mode='a', index=False, header=False)
        
    elif option == 3:
        df.iloc[nomor1,1] = saldoakhir1
        df.to_csv('data_atm.csv', index = False)
        print(f"Saldo akhir Anda adalah : {saldoakhir1}") 
        
        # Update history transaksi rekening asal
        hari_ini = dt.date.today()
        datagcdic = [
            {"nomor" : len(df.index)+1, 
            "rekening" : norek, 
            "tanggal" : hari_ini, 
            "tipe transaksi" : "Pembayaran",
            "debit_kredit" : "D",
            "jumlah": jumlah,
            "saldo" : saldoakhir1},
            ]
        df = pd.DataFrame(datagcdic)
        df.to_csv('data_history.csv', mode='a', index=False, header=False)
    
    controller.tampilkan_frame("Successful")
    
    return saldoakhir1