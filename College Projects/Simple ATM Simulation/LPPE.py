# PROGRAM ATM Language Preferences & PIN Entry
# Membantu user memilih bahasa pada mesin ATM dan memasukkan PIN ATM
# Sistem akan menyesuaikan sesuai input pengguna

# KAMUS
# registeredpin = array of integer -- PIN yang terdaftar
# inputpin = array of integer -- PIN yang dimasukkan
# pincorrect = boolean -- Pernyataan benar atau tidaknya PIN yang dimasukkan
# language = string -- Bahasa yang dapat dipilih
# English, Indonesia = boolean -- pilihan bahasa sebagai boolean

# ALGORITMA
# Pemilihan bahasa dan inisiasi awal pilihan bahasa sebagai boolean
def LPandPE():
    language = str(input('Select language: '))
    English = False
    Indonesia = False
    # Identifikasi bahasa yang dipilih pada sistem
    if language == "English":
        English = True
        Indonesia = False
    elif language == "Indonesia":
        Indonesia = True
        English = False
    # Penyesuaian sistem dengan bahasa yang dipilih
    if English == True:
        print("Enter your 6-digit PIN: ")
        print("_ _ _ _ _ _")
    elif Indonesia == True:
        print("Masukkan 6-digit PIN Anda: ")
        print("_ _ _ _ _ _")
    # Deklarasi array registeredpin dan pernyataan (boolean) pincorrect diawali dengan situasi pin salah karena belum dimasukkan ke mesin
    registeredpin = [4, 2, 3, 1, 5, 3]
    pincorrect = False
    # Input PIN pada mesin ATM dan dengan percabangan perbedaan bahasa
    if English == True:
        inputpin = [int(input("Enter PIN digit in order no. " + str(i + 1) + ": ")) for i in range (len(registeredpin))]
    elif Indonesia == True:
        inputpin = [int(input("Masukkan PIN urutan ke-" + str(i + 1) + ": ")) for i in range (len(registeredpin))]
    print("X X X X X X")
    if English == True:
        print("Loading...")
    elif Indonesia == True:
        print("Menunggu...")
    # Pengecekan apakah PIN yang diinput benar atau salah berdasarkan PIN yang terdaftar
    for i in range(len(inputpin)):
        if inputpin[i] == registeredpin[i]:
            pincorrect = True
        if inputpin[i] != registeredpin[i]:
            pincorrect = False
    # Jika PIN yang dimasukkan benar, mesin akan melanjutkan ke Main Menu untuk transaksi dan lain-lain
    if English == True:
        if pincorrect == True:
            print("MAIN MENU")
            print(">> Get Cash")
            print(">> Deposit cash and checks")
            print(">> Get balance or statements")
            print(">> Transfer Money or make payments")
            print(">> Donate to charity")
            print(">> Balance display")
            print(">> Cash Tracker")
            print(">> Return Card")
            print(">> Other transactions")
            print(">> More Choices")
    # Jika PIN salah, mesin akan meminta untuk input PIN kembali
        if pincorrect == False:
            print("Incorrect PIN. Please try again.")
            print("_ _ _ _ _ _")
    # Dengan bahasa lain
    if Indonesia == True:
        if pincorrect == True:
            print("MENU UTAMA")
            print(">> Penarikan tunai")
            print(">> Setor tunai dan cek")
            print(">> Dapatkan saldo atau laporan")
            print(">> Transfer atau bayar")
            print(">> Sumbangan")
            print(">> Informasi saldo")
            print(">> Pelacak uang tunai")
            print(">> Kembalikan kartu")
            print(">> Transaksi lain")
            print(">> Opsi lain")
        if pincorrect == False:
            print("PIN yang Anda masukkan salah. Silakan coba lagi.")
            print("_ _ _ _ _ _")