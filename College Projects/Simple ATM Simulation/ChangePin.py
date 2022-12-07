import pandas as pd
from terjemahkan import terjemahkan

def ChangePin(controller, label, bahasa, norek, pin_lama, pin_baru, kon_pb):
    df_rekening = pd.read_csv("data_atm.csv")
    PIN_rek = str(df_rekening[(df_rekening['rekening'] == norek)].iloc[0,3])
    
    print(f"Pin Ref: {PIN_rek}, datatype: {type(PIN_rek)}.")
    print(f"Pin Lama: {pin_lama}, datatype: {type(pin_lama)}.")
    print(f"Pin Baru: {pin_baru}, datatype: {type(pin_baru)}.")
    
    # base_dir = "D:/OneDrive - Institut Teknologi Bandung/01-Akademis/02-Assignments/[351] Semester 1/[351] Pengkom K16/Tubes 1/Program Script/Segmentasi Pengaturan Rekening (Joel)/"

    # invalid = True

    # while invalid:
    # newpin = input("Masukkan pin baru Anda: ")
    if pin_lama == PIN_rek:
        print("PIN LAMA OK")
        if pin_baru != kon_pb:
            label.configure(text=terjemahkan("Pin konfirmasi tidak sesuai pin baru", bahasa), fg="red", bg="white", font=controller.normalFont)
            label.after(2500, lambda: label.configure(text="", bg="dark blue"))
        else:
            print("PIN KONFIRMASI OK")
            if len(pin_baru) == 6:
                nomor = df_rekening.index[df_rekening['rekening'] == norek].tolist()
                df_rekening.iloc[nomor,3] = pin_baru
                df_rekening.to_csv('data_atm.csv', index = False)
                label.configure(text=terjemahkan("Pin berhasil diganti\nPerubahan akan berlaku pada penggunaan selanjutnya", bahasa), fg="green", bg="white", font=controller.normalFont)
                label.after(2500, lambda: label.configure(text="", bg="dark blue"))
            else:
                print("PIN KONFIRMASI X")
                label.configure(text=terjemahkan("Mohon masukkan 6 digit untuk PIN baru", bahasa), fg="red", bg="white", font=controller.normalFont)
                label.after(2500, lambda: label.configure(text="", bg="dark blue"))
    else:
        print("PIN LAMA X")
        label.configure(text=terjemahkan("Pin lama salah", bahasa), fg="red", bg="white", font=controller.normalFont)
        label.after(2500, lambda: label.configure(text="", bg="dark blue"))
    
    return
    # File1 = open(base_dir+"Akun bank.txt" , "r+")
    # File1.write(newpin)
    # File1.close