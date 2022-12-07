from terjemahkan import terjemahkan
import pandas as pd
import numpy as np

def OneTouch(norek, bahasa):
    df = pd.read_csv("data_history.csv")

    from collections import Counter
    df_rek = df.loc[df["rekening"] == norek]
    transaksi_tersering = Counter(" ".join(df_rek.tipe_transaksi).split()).most_common(1)[0][0]
    print(f"Jenis transaksi yang paling sering dilakukan adalah : {transaksi_tersering}")
    
    df_rek_tersering = df_rek.loc[df_rek["tipe_transaksi"] == transaksi_tersering]
    print(df_rek_tersering.jumlah)
    nilai_transaksi_tersering = Counter(df_rek_tersering.jumlah.tolist()).most_common(1)[0][0]

    return f"{terjemahkan(transaksi_tersering.replace('_', ' '), bahasa)}\n{nilai_transaksi_tersering:,}"