import pandas as pd
from terjemahkan import terjemahkan
import tkinter

def ChangeLanguage(controller, label, norek, bahasa_baru, bahasa_curr):
    df_rekening = pd.read_csv("data_atm.csv")
    bahasa_ori = str(df_rekening[(df_rekening['rekening'] == norek)].iloc[0,2])
    
    # base_dir = "D:/OneDrive - Institut Teknologi Bandung/01-Akademis/02-Assignments/[351] Semester 1/[351] Pengkom K16/Tubes 1/Program Script/Segmentasi Pengaturan Rekening (Joel)/"

    # invalid = True

    # while invalid:
    # newpin = input("Masukkan pin baru Anda: ")
    if bahasa_baru == bahasa_ori:
        label.configure(text=terjemahkan("Bahasa sudah digunakan!", bahasa_curr), fg="red", bg="white", font=controller.normalFont)
        label.after(2500, lambda: label.config(text="", bg="dark blue"))
    else:
        nomor = df_rekening.index[df_rekening['rekening'] == norek].tolist()
        df_rekening.iloc[nomor,2] = bahasa_baru
        df_rekening.to_csv('data_atm.csv', index = False)
        label.configure(text=terjemahkan("Bahasa berhasil diganti!\nPerubahan akan berlaku pada penggunaan selanjutnya", bahasa_curr), fg="green", bg="white", font=controller.normalFont)
        label.after(2500, lambda: label.config(text="", bg="dark blue"))
    
    return
    # File1 = open(base_dir+"Akun bank.txt" , "r+")
    # File1.write(newpin)
    # File1.close