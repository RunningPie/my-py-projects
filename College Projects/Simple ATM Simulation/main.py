import pandas as pd
import numpy as np
from datetime import datetime as dt
from datetime import timedelta
import os
import time
import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

from ChangePin import ChangePin
from ChangeLanguage import ChangeLanguage
# from CPCL import CPandCL
from DepositCash import DepositCash
from GetCash import GetCash
from History import History
from InputPin import InputPin
# from LPPE import LPandPE
from OneTouch import OneTouch
from terjemahkan import terjemahkan
from TransferMoney import TransferMoney

# base_dir = "D:\OneDrive - Institut Teknologi Bandung/01-Akademis/02-Assignments/[351] Semester 1/[351] Pengkom K16/Tubes 1/Program Script/Main Program/"

df_rekening = pd.read_csv("data_atm.csv")
df_history = pd.read_csv("data_history.csv")

norek = 1
bahasa_rek = df_rekening[(df_rekening['rekening'] == norek)].iloc[0,2]
saldof = df_rekening[(df_rekening['rekening'] == norek)].iloc[0,1]
opt = -1
nama_mutasi = ""

def tentukan_OT(tipe, pin_valid, jumlah, controller, label):
    global bahasa_rek
    if pin_valid == 1:
        if tipe == terjemahkan("Deposit Cash", bahasa_rek):
                update_saldo(DepositCash(norek, int(jumlah), controller))
                controller.update_globals()
        elif tipe == terjemahkan("Get Cash", bahasa_rek):
                update_saldo(GetCash(norek, int(jumlah), controller, bahasa_rek, label))

def update_bahasa(bahasa):
    global bahasa_rek
    bahasa_rek = bahasa
    print(f"Bahasa rek sekarang: {bahasa_rek}")
    return

def update_saldo(nilai):
    global saldof
    saldof = nilai
    print(f"Saldo rek saat ini: {saldof}")
    return

def update_nammus(nama):
    global nama_mutasi
    nama_mutasi = nama
    print(f"Nama file mutasi: {nama_mutasi}")
    return

def update_trfFrame(nilai):
    global opt
    opt = nilai
    print(f"Opsi yang dipilih {opt}")
    return

class apkUtama(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title_font = tkfont.Font(family='Leelawadee', size=30, weight="bold")
        self.headingOneFont = tkfont.Font(family='Leelawadee', size=22, weight="bold")
        self.headingTwoFont = tkfont.Font(family='Leelawadee', size=16, weight="bold")
        self.normalFont = tkfont.Font(family='Leelawadee', size=12, weight="bold")
        
        self.state("zoomed")
        self.title("ATM")
        
        self.containerUtama = tk.Frame(self)
        self.containerUtama.pack(side="top", fill="both", expand = True)
        self.containerUtama.grid_rowconfigure(0, weight=1)
        self.containerUtama.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        self.laman_laman = (Landing, MainMenu, Lainnya, Successful, Setor, 
                            Transfer, Trf_Opts, LanguagePref, Tarik, Mutasi, MutasiDone,
                            ChangeLangFr, ChangePinFr)
        
        self.buat_frame()
        
        self.tampilkan_frame("Landing")
    
    def buat_frame(self):
        for F in self.laman_laman:
            nama_laman = F.__name__
            frame = F(parent=self.containerUtama, controller=self, bg="dark blue")
            self.frames[nama_laman] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")
    
    def reset(self, nama):
        for F in self.laman_laman:
            nama_laman = F.__name__
            frame = self.frames[nama_laman]
            frame.destroy
        self.buat_frame()
        
        self.tampilkan_frame(nama)
    
    def tampilkan_frame(self, nama_laman, pin_validity=0, duration=0):
        if pin_validity == 1 or pin_validity == 0:
            frame = self.frames[nama_laman]
            frame.after(duration, lambda: frame.tkraise())
    
    def update_globals(self):
        for names in self.laman_laman:
            frame = self.frames[names.__name__]
            frame.update_globals()

class Landing(tk.Frame):  
    def __init__(self, parent, controller, bg):
        tk.Frame.__init__(self, parent, bg=bg)
        self.controller = controller
        chances = tk.IntVar()
        chances.set(3)
        
        headerUtama = tk.Label(self, text="Bads Nearcome ATM", font=controller.title_font,
                         bg=bg, foreground="white")
        headerUtama.pack(side="top", fill="x", pady=10)
        
        space_label = tk.Label(self, height=5, bg="dark blue")
        space_label.pack(side="top", fill="x")
        
        welcome_label = tk.Label(self, text=terjemahkan("Selamat datang di ATM", bahasa_rek), font=controller.headingOneFont,
                                   bg=bg, fg="white")
        welcome_label.pack(side="top", fill="x", pady=10)
        
        pin_entry_label = tk.Label(self, text=terjemahkan("Masukkan PIN Anda", bahasa_rek), font=controller.headingTwoFont,
                                   bg=bg, fg="white")
        pin_entry_label.pack(side="top", fill="x", pady=10)
        
        entered_pin = tk.StringVar()
        entered_pin.set(terjemahkan("Masukkan PIN Anda", bahasa_rek))
        
        pin_entry_box = tk.Entry(self, textvariable=entered_pin,
                                 font=controller.headingTwoFont, width=22)
        pin_entry_box.pack(ipady=10, pady=10)
        pin_entry_box.focus()
        
        
        def on_click(event):
            pin_entry_box.delete(0, len(entered_pin.get()))
        pin_entry_box.bind("<Button-1>", on_click)

        validation_label = tk.Label(self, text=" ", fg="white", bg=bg, font=controller.headingTwoFont)
        validation_label.pack(pady=10)
        
        OT_button = tk.Button(self, text=OneTouch(norek, bahasa_rek), font=controller.normalFont,
                              command=lambda: tentukan_OT(OneTouch(norek, bahasa_rek).split("\n")[0],
                                                          InputPin(norek, entered_pin, chances, validation_label, controller, bahasa_rek),
                                                          OneTouch(norek, bahasa_rek).split("\n")[1].replace(",", ""),
                                                          controller, validation_label),
                              relief="raised", borderwidth= 5)
        
        MM_button = tk.Button(self, text=terjemahkan("Main Menu", bahasa_rek), font=controller.normalFont,
                              command=lambda: controller.tampilkan_frame("MainMenu",
                                                                         InputPin(norek, entered_pin, chances, validation_label, controller, bahasa_rek)),
                              relief="raised", borderwidth= 5)
        
        LP_button = tk.Button(self, text=terjemahkan("Language Preferences", bahasa_rek), font=controller.normalFont,
                              command=lambda: controller.tampilkan_frame("LanguagePref"),
                              relief="raised", borderwidth= 5)
        
        OT_button.pack(pady=10)
        MM_button.pack(pady=10)
        LP_button.pack(pady=10)

    def update_globals(self):
        pass

class LanguagePref(tk.Frame):
    def __init__(self, parent, controller, bg):
        tk.Frame.__init__(self, parent, bg=bg)
        self.controller = controller
        self.bahasa = tk.StringVar()
        self.bahasa.set(bahasa_rek)
        
        headerUtama = tk.Label(self, text="Bads Nearcome ATM", font=controller.title_font,
                         bg=bg, foreground="white")
        headerUtama.pack(side="top", fill="x", pady=10)
        
        self.label = tk.Label(self, text=terjemahkan("Pilih bahasa yang ingin digunakan", bahasa_rek), font=controller.headingOneFont)
        self.label.pack(side="top", fill="x", pady=10)
        
        Indo_button = tk.Button(self, text="Bahasa Indonesia", font=controller.normalFont,
                              command=lambda: [update_bahasa("id"), controller.reset("LanguagePref")])
        English_button = tk.Button(self, text="English", font=controller.normalFont,
                              command=lambda: [update_bahasa("en"), controller.reset("LanguagePref")])
        
        back_btn = tk.Button(self, text=terjemahkan("Kembali", bahasa_rek), font=controller.normalFont,
                             command=lambda: [controller.tampilkan_frame("Landing"), controller.update_globals()])
        
        Indo_button.pack(pady=10)
        English_button.pack(pady=10)
        back_btn.pack(pady=10)
        
    def update_globals(self):
        self.bahasa.set(bahasa_rek)
        self.label.config(text=terjemahkan("Pilih bahasa yang ingin digunakan", bahasa_rek))

class MainMenu(tk.Frame):
    def __init__(self, parent, controller, bg):
        tk.Frame.__init__(self, parent, bg=bg)
        self.controller = controller
        self.bahasa = tk.StringVar()
        self.bahasa.set(bahasa_rek)
        
        headerUtama = tk.Label(self, text="Bads Nearcome ATM", font=controller.title_font,
                         bg=bg, foreground="white")
        headerUtama.pack(side="top", fill="x", pady=10)
        
        label = tk.Label(self, text=terjemahkan("Ini adalah Menu Utama", self.bahasa.get()), font=controller.headingOneFont)
        label.pack(side="top", fill="x", pady=10)
        
        self.label_saldo = tk.Label(self, text=terjemahkan(f"Saldo Anda: {saldof:,}".replace(",", "."), self.bahasa.get()), font=controller.headingTwoFont,
                                    bg="white")
        self.label_saldo.pack(pady=10)
        
        DC_button = tk.Button(self, text=terjemahkan("Setor Tunai", self.bahasa.get()), font=controller.normalFont,
                              command=lambda: controller.tampilkan_frame("Setor"))
        Trf_button = tk.Button(self, text=terjemahkan("Transfer Uang", self.bahasa.get()), font=controller.normalFont,
                               command=lambda: controller.tampilkan_frame("Transfer"))
        GC_button = tk.Button(self, text=terjemahkan("Tarik Tunai", self.bahasa.get()), font=controller.normalFont,
                              command=lambda: controller.tampilkan_frame("Tarik"))
        GS_button = tk.Button(self, text="History", font=controller.normalFont,
                             command=lambda: controller.tampilkan_frame("Mutasi"))
        
        O_button = tk.Button(self, text=terjemahkan("Lainnya", self.bahasa.get()), font=controller.normalFont,
                              command=lambda: controller.tampilkan_frame("Lainnya"))
        
        exit_btn = tk.Button(self, text=terjemahkan("Keluar dari Aplikasi", bahasa_rek), font=controller.normalFont,
                             command= lambda: controller.after(1500, controller.destroy()))
        
        DC_button.pack(pady=10)
        Trf_button.pack(pady=10)
        GC_button.pack(pady=10)
        GS_button.pack(pady=10)
        O_button.pack(pady=10)
        exit_btn.pack(pady=10)
        
    def update_globals(self):
        self.bahasa.set(bahasa_rek)
        self.label_saldo.configure(text=terjemahkan(f"Saldo Anda: {saldof:,}".replace(",", "."), self.bahasa.get()))
        

class Successful(tk.Frame):
    def __init__(self, parent, controller, bg):
        tk.Frame.__init__(self, parent, bg=bg)
        self.controller = controller
        
        headerUtama = tk.Label(self, text="Bads Nearcome ATM", font=controller.title_font,
                         bg=bg, foreground="white")
        headerUtama.pack(side="top", fill="x", pady=10)
        
        label = tk.Label(self, text=terjemahkan("Transaksi Anda Sudah Berhasil!", bahasa_rek), font=controller.headingOneFont)
        label.pack(side="top", fill="x", pady=10)
        
        self.nama_file_label = tk.Label(self, text=terjemahkan(f"Saldo Anda sekarang {saldof:,}.".replace(",","."), bahasa_rek), font=controller.headingTwoFont)
        self.nama_file_label.pack(pady=10)
        
        exit_btn = tk.Button(self, text=terjemahkan("Keluar dari Aplikasi", bahasa_rek), font=controller.normalFont,
                             command= lambda: controller.after(1500, controller.destroy()))
        exit_btn.pack(pady=10)
        
        main_btn = tk.Button(self, text=terjemahkan("Kembali ke Menu Utama", bahasa_rek), font=controller.normalFont,
                             command=lambda: [controller.tampilkan_frame("MainMenu"), controller.update_globals()])
        main_btn.pack(pady=10)
    
    def update_globals(self):
            self.nama_file_label.config(text=terjemahkan(f"Saldo Anda sekarang {saldof:,}.".replace(",","."), bahasa_rek))

class Setor(tk.Frame):
    def __init__(self, parent, controller, bg):
        tk.Frame.__init__(self, parent, bg=bg)
        self.controller = controller
        
        headerUtama = tk.Label(self, text="Bads Nearcome ATM", font=controller.title_font,
                         bg=bg, foreground="white")
        headerUtama.pack(side="top", fill="x", pady=10)
        
        label = tk.Label(self, text=terjemahkan("Berapa jumlah yang ingin disetorkan?", bahasa_rek), font=controller.headingOneFont)
        label.pack(side="top", fill="x", pady=10)
        
        btn_100 = tk.Button(self, text="100.000", font=controller.normalFont,
                            command=lambda: [update_saldo(DepositCash(norek, 100000, controller)), controller.update_globals()])
        btn_100.pack(pady=10)
        btn_200 = tk.Button(self, text="200.000",  font=controller.normalFont,
                            command=lambda: [update_saldo(DepositCash(norek, 200000, controller)), controller.update_globals()])
        btn_200.pack(pady=10)
        btn_300 = tk.Button(self, text="300.000", font=controller.normalFont,
                            command=lambda: [update_saldo(DepositCash(norek, 300000, controller)), controller.update_globals()])
        btn_300.pack(pady=10)
        btn_400 = tk.Button(self, text="400.000", font=controller.normalFont,
                            command=lambda: [update_saldo(DepositCash(norek, 400000, controller)), controller.update_globals()])
        btn_400.pack(pady=10)
        btn_500 = tk.Button(self, text="500.000", font=controller.normalFont,
                            command=lambda: [update_saldo(DepositCash(norek, 500000, controller)), controller.update_globals()])
        btn_500.pack(pady=10)
        
        back_btn = tk.Button(self, text=terjemahkan("Kembali ke Menu Utama", bahasa_rek), font=controller.normalFont,
                             command=lambda: [controller.tampilkan_frame("MainMenu"), controller.update_globals()])
        back_btn.pack(pady=10)
        
    def update_globals(self):
        pass
    
class Transfer(tk.Frame):
    def __init__(self, parent, controller, bg):
        tk.Frame.__init__(self, parent, bg=bg)
        self.controller = controller
        
        headerUtama = tk.Label(self, text="Bads Nearcome ATM", font=controller.title_font,
                         bg=bg, foreground="white")
        headerUtama.pack(side="top", fill="x", pady=10)
        
        label = tk.Label(self, text=terjemahkan("Transfer jenis apa yang ingin dilakukan?", bahasa_rek), font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        trf_rek = tk.Button(self, text=terjemahkan("Transfer Antar Rekening", bahasa_rek), font=controller.normalFont,
                            command=lambda: [controller.tampilkan_frame("Trf_Opts"), update_trfFrame(1), controller.update_globals()])
        trf_rek.pack(pady=10)
        trf_bank = tk.Button(self, text=terjemahkan("Transfer Antar Bank", bahasa_rek), font=controller.normalFont,
                             command=lambda: [controller.tampilkan_frame("Trf_Opts"), update_trfFrame(2), controller.update_globals()])
        trf_bank.pack(pady=10)
        pembayaran = tk.Button(self, text=terjemahkan("Pembayaran", bahasa_rek), font=controller.normalFont,
                               command=lambda: [controller.tampilkan_frame("Trf_Opts"), update_trfFrame(3), controller.update_globals()])
        pembayaran.pack(pady=10)
        
        back_btn = tk.Button(self, text=terjemahkan("Kembali ke Menu Utama", bahasa_rek), font=controller.normalFont,
                             command=lambda: [controller.tampilkan_frame("MainMenu"), controller.update_globals()])
        back_btn.pack(pady=10)
        
    def update_globals(self):
        pass
    
class Trf_Opts(tk.Frame):
    def __init__(self, parent, controller, bg):
        tk.Frame.__init__(self, parent, bg=bg)
        self.controller = controller

        
        self.trf_opt = tk.IntVar()
        self.trf_opt.set(-1)
        
        headerUtama = tk.Label(self, text="Bads Nearcome ATM", font=controller.title_font,
                         bg=bg, foreground="white")
        headerUtama.pack(side="top", fill="x", pady=10)

        self.chances = tk.IntVar()
        self.chances.set(0)
        
        self.label_rekt = tk.Label(self, text=terjemahkan("Masukkan nomor rekening tujuan", bahasa_rek), font=controller.headingTwoFont)
        self.label_rekt.pack(side="top", fill="x", pady=10)
        
        self.entered_rek = tk.StringVar()
        self.entered_rek.set(terjemahkan("Masukkan rekening", bahasa_rek))
        
        self.rek_tujuan = tk.Entry(self, textvariable=terjemahkan(self.entered_rek.get(), bahasa_rek),
                                 font=controller.normalFont, width=22)
        self.rek_tujuan.pack(ipady=10, pady=10)
        
        self.rek_tujuan.focus()
        def on_click(event):
            self.rek_tujuan.delete(0, len(self.entered_rek.get()))
        self.rek_tujuan.bind("<Button-1>", on_click)
        
        self.label_rekeningInvalid = tk.Label(self, text="", font=controller.headingTwoFont, bg="dark blue")
        
        self.label_jumlah = tk.Label(self, text=terjemahkan("Masukkan nominal yang akan ditransfer", bahasa_rek), font=controller.normalFont)
        self.label_jumlah.pack(side="top", fill="x", pady=10)
        
        self.jumlah_trf = tk.StringVar()
        self.jumlah_trf.set(terjemahkan("Masukkan jumlah", bahasa_rek))
        
        self.jumlah_trf_entry = tk.Entry(self, textvariable=terjemahkan(self.jumlah_trf.get(), bahasa_rek),
                                 font=controller.normalFont, width=22)
        self.jumlah_trf_entry.pack(ipady=10, pady=10)
        
        self.jumlah_trf_entry.focus()
        def on_click(event):
            self.jumlah_trf_entry.delete(0, len(self.jumlah_trf.get()))
        self.jumlah_trf_entry.bind("<Button-1>", on_click)
        
        
        
        # ===================================================================================================================
        # Widget untuk menu Pembayaran
        self.label_jenis = tk.Label(self, text=terjemahkan("Pilih Jenis Pembayaran", bahasa_rek), font=controller.headingOneFont)
        
        pilihan_var = tk.StringVar()
        
        pilihanArr = ("Air", "Tagihan Listrik", "Pulsa/Internet")
        
        def on_select(event):
            self.send_m.pack_forget()
            self.validateOpt.pack_forget()
            self.back_btn.pack_forget()
            self.validateOpt.configure(text=terjemahkan(f"Yakin ingin melakukan pembayaran {pilihan_var.get()}?"),
                                       fg="red",  font=controller.normalFont)
            self.send_m.config(command=lambda: [update_saldo(TransferMoney(controller, norek, -1,
                                                                           self.trf_opt.get(), -1,
                                                                           self.label_rekeningInvalid, bahasa_rek, self.chances,
                                                                           kode=int(self.cb.current()+1))), controller.update_globals()])
            self.validateOpt.pack(pady=10)
            self.back_btn.pack(pady=10)
            self.send_m.pack(pady=10)
        
        self.cb = ttk.Combobox(self, textvariable=pilihan_var)
        self.cb['values']= pilihanArr
        self.cb['state']= 'readonly'
        self.cb.bind('<<ComboboxSelected>>', on_select)
        
        self.validateOpt = tk.Label(self, text="",
                               font=controller.normalFont)
        
        print(self.cb.current())
        
        self.send_m = tk.Button(self, text=terjemahkan("Kirim", bahasa_rek),  font=controller.normalFont,
                                command=lambda: [update_saldo(TransferMoney(controller, norek, int(self.rek_tujuan.get()),
                                                                            self.trf_opt.get(), int(self.jumlah_trf_entry.get()),
                                                                            self.label_rekeningInvalid, bahasa_rek, self.chances,
                                                                            kode=int(self.cb.current()+1))),
                                                 controller.update_globals()])
        self.send_m.pack(pady=10)
        
        self.back_btn = tk.Button(self, text=terjemahkan("Kembali ke Menu Utama", bahasa_rek),
                             command=lambda: [controller.tampilkan_frame("MainMenu"), controller.update_globals()])
        self.back_btn.pack(pady=10)
        
    def update_globals(self):
            global opt
            self.trf_opt.set(opt)
            print(opt)
            
            if opt==1 or opt==2:
                self.label_jenis.pack_forget()
                self.cb.pack_forget()
                self.send_m.pack_forget()
                self.validateOpt.pack_forget()
                self.back_btn.pack_forget()
                
                self.chances.set(0)
                self.entered_rek.set("Masukkan rekening")
                self.jumlah_trf.set("Masukkan jumlah")
                
                self.rek_tujuan.configure(textvariable=terjemahkan(self.entered_rek.get(), bahasa_rek))
                self.jumlah_trf_entry.configure(textvariable=terjemahkan(self.jumlah_trf, bahasa_rek))
                
                self.send_m.configure(command=lambda: [update_saldo(TransferMoney(self.controller, norek, int(self.rek_tujuan.get()),
                                                                                                      self.trf_opt.get(), int(self.jumlah_trf_entry.get()), self.label_rekeningInvalid,
                                                                                                      bahasa_rek, self.chances, kode=int(self.cb.current()+1))),
                                                                                         self.controller.update_globals()])
                
                self.label_rekt.pack(pady=10)
                self.rek_tujuan.pack(pady=10)
                self.label_jumlah.pack(pady=10)
                self.jumlah_trf_entry.pack(pady=10)
                self.send_m.pack(pady=10)
                self.back_btn.pack(pady=10)
            
            elif opt == 3:
                self.label_rekt.pack_forget()
                self.label_jumlah.pack_forget()
                self.rek_tujuan.pack_forget()
                self.jumlah_trf_entry.pack_forget()
                self.send_m.pack_forget()
                self.label_rekeningInvalid.pack_forget()
                self.back_btn.pack_forget()
                
                self.label_jenis.pack(side="top", fill="x", pady=10)
                self.cb.pack(fill='x',padx= 5, pady=5)
                self.send_m.pack(pady=10)
                self.back_btn.pack(pady=10)
                
    
class Tarik(tk.Frame):
    def __init__(self, parent, controller, bg):
        tk.Frame.__init__(self, parent, bg=bg)
        self.controller = controller
        
        headerUtama = tk.Label(self, text="Bads Nearcome ATM", font=controller.title_font,
                         bg=bg, foreground="white")
        headerUtama.pack(side="top", fill="x", pady=10)
        
        label = tk.Label(self, text=terjemahkan("Berapa jumlah yang ingin ditarik?", bahasa_rek), font=controller.headingOneFont)
        label.pack(side="top", fill="x", pady=10)
        
        self.label_status = tk.Label(self, text="", font=controller.headingTwoFont, bg=bg)
        self.label_status.pack(pady=10)
        
        btn_100 = tk.Button(self, text="100.000", font=controller.normalFont,
                            command=lambda: [update_saldo(GetCash(norek, 100000, controller, bahasa_rek, self.label_status)),
                                             controller.update_globals()])
        btn_100.pack(pady=10)
        btn_200 = tk.Button(self, text="200.000", font=controller.normalFont,
                            command=lambda: [update_saldo(GetCash(norek, 200000, controller, bahasa_rek, self.label_status)),
                                             controller.update_globals()])
        btn_200.pack(pady=10)
        btn_300 = tk.Button(self, text="300.000", font=controller.normalFont,
                            command=lambda: [update_saldo(GetCash(norek, 300000, controller, bahasa_rek, self.label_status)),
                                             controller.update_globals()])
        btn_300.pack(pady=10)
        btn_400 = tk.Button(self, text="400.000", font=controller.normalFont,
                            command=lambda: [update_saldo(GetCash(norek, 400000, controller, bahasa_rek, self.label_status)),
                                             controller.update_globals()])
        btn_400.pack(pady=10)
        btn_500 = tk.Button(self, text="500.000", font=controller.normalFont,
                            command=lambda: [update_saldo(GetCash(norek, 500000, controller, bahasa_rek, self.label_status)),
                                             controller.update_globals()])
        btn_500.pack(pady=10)
        
        back_btn = tk.Button(self, text=terjemahkan("Kembali ke Menu Utama", bahasa_rek), font=controller.normalFont,
                             command=lambda: [controller.tampilkan_frame("MainMenu"), controller.update_globals()])
        back_btn.pack(pady=10)
        
    def update_globals(self):
        pass
    

class Mutasi(tk.Frame):
    def __init__(self, parent, controller, bg):
        tk.Frame.__init__(self, parent, bg=bg)
        self.controller = controller
        
        headerUtama = tk.Label(self, text="Bads Nearcome ATM", font=controller.title_font,
                         bg=bg, foreground="white")
        headerUtama.pack(side="top", fill="x", pady=10)
        
        label_awal = tk.Label(self, text=terjemahkan("Pilih Tanggal Awal", bahasa_rek), font=controller.headingOneFont)
        label_awal.pack(pady=10)
        
        label_status = tk.Label(self, text="", font=controller.headingOneFont, bg=bg)
        label_status.pack(pady=10)
        
        # def on_select_awal(event):
        #     label_taw.config(text=kalender_awal.get_date())
        #     label_taw.pack()
        
        kalender_awal = Calendar(self, selectmode="day",
                                 year=dt.now().year, month=dt.now().month, day=dt.now().day,
                                 bg="red", fg="black", date_pattern='yyyy-mm-dd',
                                 maxdate=dt.today(), mindate=dt.today()-timedelta(days=30))
        # kalender_awal.bind('<<CalendarSelected>>', on_select_awal)
        kalender_awal.pack(pady=10)
        
        # label_taw = tk.Label(text="", bg="white", fg="black", font=controller.headingTwoFont)
        
        label_akhir = tk.Label(self, text=terjemahkan("Pilih Tanggal Akhir", bahasa_rek), font=controller.headingOneFont)
        label_akhir.pack(pady=10)
        
        # def on_select_akhir(event):
        #     label_tak.config(text=kalender_akhir.get_date())
        #     label_tak.pack()
        
        kalender_akhir = Calendar(self, selectmode="day",
                                 year=dt.now().year, month=dt.now().month, day=dt.now().day,
                                 bg="red", fg="black", date_pattern='yyyy-mm-dd',
                                 maxdate=dt.today(), mindate=dt.today()-timedelta(days=30))
        # kalender_awal.bind('<<CalendarSelected>>', on_select_akhir)
        kalender_akhir.pack(pady=10)
        
        # label_tak = tk.Label(text="", bg="white", fg="black", font=controller.headingTwoFont)
        
        setDate_button = tk.Button(self, text="Set Date", font=controller.normalFont,
                              command=lambda: [update_nammus(History(controller, norek, kalender_awal.get_date(), kalender_akhir.get_date(), bahasa_rek, label_status)),
                                               controller.update_globals()])
        setDate_button.pack(pady=10)
        
        back_btn = tk.Button(self, text=terjemahkan("Kembali ke Menu Utama", bahasa_rek), font=controller.normalFont,
                             command=lambda: [controller.tampilkan_frame("MainMenu"), controller.update_globals()])
        back_btn.pack(pady=10)
        
    def update_globals(self):
        pass

class MutasiDone(tk.Frame):
    def __init__(self, parent, controller, bg):
        tk.Frame.__init__(self, parent, bg=bg)
        self.controller = controller
        
        headerUtama = tk.Label(self, text="Bads Nearcome ATM", font=controller.title_font,
                         bg=bg, foreground="white")
        headerUtama.pack(side="top", fill="x", pady=10)
        
        self.label = tk.Label(self, text=terjemahkan("Mutasi rekening berhasil dibuat", bahasa_rek), font=controller.headingOneFont)
        self.label.pack(side="top", fill="x", pady=10)
        
        self.nama_file_label = tk.Label(self, text=terjemahkan(f"Silakan periksa pada file bernama:\n{nama_mutasi}", bahasa_rek),
                                        font=controller.headingTwoFont)
        self.nama_file_label.pack(pady=10)
        
        exit_btn = tk.Button(self, text=terjemahkan("Keluar dari Aplikasi", bahasa_rek), font=controller.normalFont,
                             command= lambda: controller.after(1500, controller.destroy()))
        exit_btn.pack(pady=10)
        
        main_btn = tk.Button(self, text=terjemahkan("Kembali ke Menu Utama", bahasa_rek), font=controller.normalFont,
                             command=lambda: [controller.tampilkan_frame("MainMenu"), controller.update_globals()])
        main_btn.pack(pady=10)
    
    def update_globals(self):
        if nama_mutasi != "Empty":
            self.label.config(text=terjemahkan("Mutasi rekening berhasil dibuat", bahasa_rek))
            self.nama_file_label.configure(text=terjemahkan(f"Silakan periksa pada file bernama:\n{nama_mutasi}", bahasa_rek), bg="white")
        else:
            self.label.config(text=terjemahkan("Mutasi pada rentang waktu yang dipilih kosong", bahasa_rek))
            self.nama_file_label.config(text="", bg="dark blue")

class Lainnya(tk.Frame):
    def __init__(self, parent, controller, bg):
        tk.Frame.__init__(self, parent, bg=bg)
        self.controller = controller
        
        headerUtama = tk.Label(self, text="Bads Nearcome ATM", font=controller.title_font,
                         bg=bg, foreground="white")
        headerUtama.pack(side="top", fill="x", pady=10)
        
        label = tk.Label(self, text=terjemahkan("Ini Menu Lainnya", bahasa_rek), font=controller.headingOneFont)
        label.pack(side="top", fill="x", pady=10)
        
        CP_button = tk.Button(self, text=terjemahkan("Ganti Pin Rekening", bahasa_rek), font=controller.normalFont,
                              command=lambda: controller.tampilkan_frame("ChangePinFr"))
        CL_button = tk.Button(self, text=terjemahkan("Ganti Bahasa Rekening", bahasa_rek), font=controller.normalFont,
                              command=lambda: controller.tampilkan_frame("ChangeLangFr"))
        MM_button = tk.Button(self, text=terjemahkan("Main Menu", bahasa_rek), font=controller.normalFont,
                              command=lambda: controller.tampilkan_frame("MainMenu"))
        
        CP_button.pack(pady=10)
        CL_button.pack(pady=10)
        MM_button.pack(pady=10)
        
    def update_globals(self):
        pass
    
class ChangePinFr(tk.Frame):
    def __init__(self, parent, controller, bg):
        tk.Frame.__init__(self, parent, bg=bg)
        self.controller = controller
        
        headerUtama = tk.Label(self, text="Bads Nearcome ATM", font=controller.title_font,
                         bg=bg, foreground="white")
        headerUtama.pack(side="top", fill="x", pady=10)
        
        label = tk.Label(self, text=terjemahkan("Ini Menu Lainnya", bahasa_rek), font=controller.headingOneFont)
        label.pack(side="top", fill="x", pady=10)
        
        # =============== Old Pin Entry =======================
        self.old_pin_var = tk.StringVar()
        self.old_pin_var.set(terjemahkan("Masukkan pin lama", bahasa_rek))
        old_pin_label = tk.Label(self, text=self.old_pin_var.get(), font=controller.headingTwoFont)
        old_pin_label.pack(pady=10)
        self.old_pin_entry = tk.Entry(self, textvariable=self.old_pin_var,
                                 font=controller.headingTwoFont, width=22)
        self.old_pin_entry.pack(ipady=10, pady=10)
        
        self.old_pin_entry.focus()
        def on_click(event):
            self.old_pin_entry.delete(0, len(self.old_pin_entry.get()))
        self.old_pin_entry.bind("<Button-1>", on_click)
        
        # =============== New Pin Entry =======================
        self.new_pin_var = tk.StringVar()
        self.new_pin_var.set(terjemahkan("Masukkan pin baru", bahasa_rek))
        new_pin_label = tk.Label(self, text=self.new_pin_var.get(), font=controller.headingTwoFont)
        new_pin_label.pack(pady=10)
        self.new_pin_entry = tk.Entry(self, text=self.new_pin_var,
                                 font=controller.headingTwoFont, width=22)
        self.new_pin_entry.pack(ipady=10, pady=10)
        
        self.new_pin_entry.focus()
        def on_click(event):
            self.new_pin_entry.delete(0, len(self.new_pin_entry.get()))
        self.new_pin_entry.bind("<Button-1>", on_click)
        
        # =============== New Pin Confirmation =======================
        self.c_new_var = tk.StringVar()
        self.c_new_var.set(terjemahkan("Konfirmasi pin baru", bahasa_rek))
        confirm_new_label = tk.Label(self, text=self.c_new_var.get(), font=controller.headingTwoFont)
        confirm_new_label.pack(pady=10)
        self.new_pin_confirm = tk.Entry(self, textvariable=self.c_new_var,
                                 font=controller.headingTwoFont, width=22)
        self.new_pin_confirm.pack(ipady=10, pady=10)
        
        self.new_pin_confirm.focus()
        def on_click(event):
            self.new_pin_confirm.delete(0, len(self.new_pin_confirm.get()))
        self.new_pin_confirm.bind("<Button-1>", on_click)
        
        self.label_status = tk.Label(self, text="", bg=bg)
        self.label_status.pack(pady=10)
        
        change_btn = tk.Button(self, text=terjemahkan("Ganti Pin", bahasa_rek), font=controller.normalFont,
                               command=lambda: ChangePin(controller, self.label_status, bahasa_rek, norek,
                                                         self.old_pin_entry.get(), self.new_pin_entry.get(), self.new_pin_confirm.get()))
        change_btn.pack(pady=10)
        
        MM_button = tk.Button(self, text=terjemahkan("Main Menu", bahasa_rek), font=controller.normalFont,
                              command=lambda: controller.tampilkan_frame("MainMenu"))
        MM_button.pack(pady=10)
        
        exit_btn = tk.Button(self, text=terjemahkan("Keluar dari Aplikasi", bahasa_rek), font=controller.normalFont,
                             command= lambda: controller.after(1500, controller.destroy()))
        exit_btn.pack(pady=10)
        
    def update_globals(self):
        self.old_pin_var.set(terjemahkan("Masukkan pin lama", bahasa_rek))
        self.new_pin_var.set(terjemahkan("Masukkan pin baru", bahasa_rek))
        self.c_new_var.set(terjemahkan("Konfirmasi pin baru", bahasa_rek))
        self.old_pin_entry.config(textvariable=self.old_pin_var)
        self.new_pin_entry.config(textvariable=self.new_pin_var)
        self.new_pin_confirm.config(textvariable=self.c_new_var)
        
class ChangeLangFr(tk.Frame):
    def __init__(self, parent, controller, bg):
        tk.Frame.__init__(self, parent, bg=bg)
        self.controller = controller
        self.bahasa = tk.StringVar()
        self.bahasa.set(bahasa_rek)
        
        headerUtama = tk.Label(self, text="Bads Nearcome ATM", font=controller.title_font,
                         bg=bg, foreground="white")
        headerUtama.pack(side="top", fill="x", pady=10)
        
        self.label = tk.Label(self, text=terjemahkan("Pilih bahasa yang ingin digunakan", bahasa_rek), font=controller.headingOneFont)
        self.label.pack(side="top", fill="x", pady=10)
        
        self.label_status = tk.Label(self, text="", bg=bg)
        self.label_status.pack(pady=10)
        
        Indo_button = tk.Button(self, text="Bahasa Indonesia", font=controller.normalFont,
                              command=lambda: ChangeLanguage(controller, self.label_status, norek, "id", bahasa_rek))
        English_button = tk.Button(self, text="English", font=controller.normalFont,
                              command=lambda: ChangeLanguage(controller, self.label_status, norek, "en", bahasa_rek))
        
        back_btn = tk.Button(self, text=terjemahkan("Kembali", bahasa_rek), font=controller.normalFont,
                             command=lambda: [controller.tampilkan_frame("MainMenu"), controller.update_globals()])
        
        Indo_button.pack(pady=10)
        English_button.pack(pady=10)
        back_btn.pack(pady=10)
        
        exit_btn = tk.Button(self, text=terjemahkan("Keluar dari Aplikasi", bahasa_rek), font=controller.normalFont,
                             command= lambda: controller.after(1500, controller.destroy()))
        exit_btn.pack(pady=10)
        
    def update_globals(self):
        self.bahasa.set(bahasa_rek)
        self.label.config(text=terjemahkan("Pilih bahasa yang ingin digunakan", bahasa_rek))

if __name__ == "__main__":
    app = apkUtama()
    
    app.geometry("750x750")
    app.mainloop()