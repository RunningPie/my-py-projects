#Program membuat history dari transaksi yang dilakukan
import os
import pandas as pd
import numpy as np
from datetime import datetime as dt
import dataframe_image as dfi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from csv2pdf import convert
from terjemahkan import terjemahkan

def History(controller, norek, awal, akhir, bahasa, label):
    awal_obj = dt.strptime(awal, '%Y-%m-%d')
    akhir_obj = dt.strptime(akhir, '%Y-%m-%d')
    
    print(f"Tanggal awal {awal}")
    print(f"Tanggal akhir {akhir}")
    print((akhir_obj-awal_obj).days)
    if (akhir_obj-awal_obj).days <= 7 and (akhir_obj-awal_obj).days >=0:
        df_1 = pd.read_csv('data_atm.csv')
        df_2 = pd.read_csv('data_history.csv')
        n = 0
        a = " "
        while n<3 :
            # norek = int(input("Masukkan no rekening :")) 
            try : 
                cek_rekening = df_1[(df_1['rekening'] == norek)]
                rekening = cek_rekening.iloc[0,0]
                if rekening >= 0 :
                    break
                if n >= 3 :
                    break
            except :
                n+= 1
                if n >= 3 :
                    print("Nomor rekening tidak ditemukan.")
                    break
                print("Nomor rekening tidak ditemukan, silahkan masukkan nomor rekening ulang!")
        
        # df_2["tanggal"] = pd.to_datetime(df_2["tanggal"])
        mask = (df_2["tanggal"] >= awal) & (df_2["tanggal"] <= akhir)
        
        try :  
            rekening_1 = df_2.loc[(df_2['rekening'] == norek) & mask]
            print(len(rekening_1))
            # rekening2 = rekening_1.iloc[0,1]
        except :
            a = "Tidak ada history"
            print(a)

        if len(rekening_1)==0:
            to_return = "Empty"
        
        elif len(rekening_1)<50:
            mutasi_styled = rekening_1.style.background_gradient()
            mutasi_styled = mutasi_styled.hide(axis="index")
            mutasi_styled = mutasi_styled.set_caption(f"Mutasi Rekening {norek} Periode {awal} sampai {akhir}").set_table_styles([{'selector': 'caption',
                                                                                                                                   'props': [('color', 'black'),
                                                                                                                                             ('font-size', '32px'),
                                                                                                                                             ('font-weight', 'bold')]}])
            
            dfi.export(mutasi_styled, terjemahkan(f"mutasi rekening {norek} periode {awal} sampai {akhir}.png", bahasa))
            
            
            # fig, ax =plt.subplots(figsize=(12,4))
            # ax.axis('tight')
            # ax.axis('off')
            # the_table = ax.table(cellText=rekening_1.values,colLabels=rekening_1.columns,loc='center')
            # pp = PdfPages("foo.pdf")
            # pp.savefig(fig, bbox_inches='tight')
            # pp.close()
            
            to_return = terjemahkan(f"mutasi rekening {norek} periode {awal} sampai {akhir}.png", bahasa)
        elif len(rekening_1)>=50:
            mutasi = df_2.loc[(df_2['rekening'] == norek) & mask]
            mutasi.drop(["rekening", "nomor"], axis=1, inplace=True)
            mutasi.to_csv("mutasi.csv", index=False)
            convert("mutasi.csv", terjemahkan(f"mutasi rekening {norek} periode {awal} sampai {akhir}.pdf", bahasa))
            os.remove("mutasi.csv")
            
            to_return = terjemahkan(f"mutasi rekening {norek} periode {awal} sampai {akhir}.pdf", bahasa)
        
        controller.tampilkan_frame("MutasiDone")
        return to_return

    else:
        label.config(text=terjemahkan("Durasi yang dapat dipilih hanya pada rentang 0-7 hari!", bahasa), fg="red", bg="white",
                     font=controller.headingTwoFont)
        label.after(5000, lambda: label.config(text="", fg="red", bg="dark blue",
                     font=controller.headingTwoFont))
        return