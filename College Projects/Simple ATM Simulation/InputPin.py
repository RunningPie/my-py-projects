from terjemahkan import terjemahkan
import pandas as pd

def InputPin(norek, entered_pin, chances, label, controller, bahasa):
    
    validity = -1

    df = pd.read_csv("data_atm.csv")
    pinrek = str((df.loc[df["rekening"] == norek]).iloc[0]["PIN"])

    pin = entered_pin.get()
    if len(pin) != 6:
        print(pin)
        print(len(pin))
        label.config(text=terjemahkan("Mohon Masukkan 6 digit", bahasa), fg="Red", bg="white")
        validity = -1
    elif pin == pinrek:
        print("continue to main menu")
        chances.set(0)
        label.config(text=terjemahkan("PIN benar", bahasa), fg="Green", bg="white")
        validity = 1
    else:
        if chances.get() > 0:
            # print(f"Anda bisa mencoba {chances.get()} kali lagi")
            label.config(text=terjemahkan(f"PIN salah\nAnda bisa mencoba {chances.get()} kali lagi", bahasa), fg="Red", bg="white")
            chances.set(chances.get()-1)
            validity = -1
        elif chances.get() == 0:
            # print(f"Terlalu banyak kesalahan. Silakan coba lagi nanti.")
            label.config(text=terjemahkan("Terlalu banyak kesalahan. Silakan coba lagi nanti.", bahasa), fg="Red", bg="white")
            chances.set(chances.get()-1)
            controller.after(1500, lambda: controller.destroy())
            validity = -1
            
    return validity

    