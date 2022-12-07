# Program Ganti PIN dan Bahasa
# Membantu pengguna mengganti PIN ATM dan bahasa di mesin ATM

# KAMUS
# menu = string -- untuk memilih menu
# choice = string -- pilihan pengaturan dalam menu
# options = string -- opsi pengaturan lebih lanjut
# oldpin = array of integer -- PIN lama yang terdaftar
# inputoldpin = array of integer -- Input PIN lama
# inputnewpin = array of integer -- Input PIN baru
# confirmnewpin = array of integer -- Konfirmasi PIN baru
# language = string -- pilihan penggantian bahasa
# correct = boolean -- pernyataan apakah konfirmasi PIN baru sama dengan input awal PIN baru
# cont = string -- pertanyaan dengan jawaban "Ya" atau "Tidak" ("Yes" or "No") apakah ingin melanjutkan penggunaan mesin ATM atau tidak
# active = boolean -- ATM aktif beroperasi atau tidak

# ALGORITMA
    # Deklarasi array oldpin dan boolean correct
def CPandCL():
    oldpin = [4, 2, 3, 1, 5, 3]
    correct = False
    active = True
    currentlanguage = str(input('Current language: '))
    # Pemilihan menu, choice, dan options
    while active == True:
        if currentlanguage == "English":
            if currentlanguage != "Indonesia":
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
                menu = str(input("Choose menu: "))
                if menu == "More Choices":
                    print("MORE CHOICES")
                    print(">> ATM Settings and Services")
                    print(">> My Rewards")
                    print(">> Wells Fargo Services")
                choice = str(input("Select choices: "))
                if choice == "ATM Settings and Services":
                    print("ATM SETTINGS AND SERVICES")
                    print(">> Change Language")
                    print(">> Change PIN")
                    print(">> View/print nearby ATMs")
                    print(">> Manage cash trackers")
                    print(">> Change ATM privacy settings")
                options = str(input("Find and select options: "))
                # Jika ingin mengganti bahasa terlebih dahulu
                if options == "Change Language":
                            language = str(input("Change language to: "))
                            if language == "English":
                                print("Your language has successfully changed. We'll get you back to Main Menu...")
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
                            elif language == "Indonesia":
                                currentlanguage == "Indonesia"
                                print("Bahasa telah diganti. Kami akan mengembalikan Anda ke Menu Utama...")
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
                if options == "Change PIN":
                    print("Enter your old PIN: ")
                    print("_ _ _ _ _ _")
                    # Input PIN lama ke dalam array
                    inputoldpin = [int(input("Enter old PIN digit in order no. " + str(i + 1) + ": ")) for i in range (len(oldpin))]
                    # Mengecek apakah PIN lama yang terdaftar sama dengan yang diinput
                    for i in range(len(inputoldpin)):
                        active = True
                        correct = False
                        if inputoldpin[i] == oldpin[i]:
                            correct = True
                        else:
                            correct = False
                    # Input PIN baru jika input PIN lama benar
                    if correct == True:
                        print("Authorizing...")
                        print("Enter your new PIN: ")
                        print("_ _ _ _ _ _")
                    else: 
                        print("Incorrect PIN. Try again.")
                    # Input PIN baru
                    if correct == True:
                        inputnewpin = [int(input("Enter new PIN digit in order no. " + str(i + 1) + ": ")) for i in range (len(oldpin))]
                        print("Confirm your new PIN: ")
                        print("_ _ _ _ _ _")
                    # Konfirmasi input PIN baru
                    if correct == True:
                        confirmnewpin = [int(input("Confirm your new PIN digit in order no. " + str(i + 1) + ": ")) for i in range (len(inputnewpin))]
                        if confirmnewpin[i] == inputnewpin[i]:
                            print("Your PIN has successfully changed.") 
                            print("Your new PIN is", (confirmnewpin))
            # Pertanyaan untuk lanjut menggunakan ATM atau tidak
            cont = str(input("Continue? "))
            # ATM tetap beroperasi jika user akan lanjut menggunakan ATM
            if cont == "Yes":
                active = True  
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
                # Memilih menu kembali
                menu = str(input("Choose menu: "))
                if menu == "More Choices":
                    print("MORE CHOICES")
                    print(">> ATM Settings and Services")
                    print(">> My Rewards")
                    print(">> Wells Fargo Services")
                # Memilih pilihan menu kembali
                choice = str(input("Select choices: "))
                if choice == "ATM Settings and Services":
                        print("ATM SETTINGS AND SERVICES")
                        print(">> Change Language")
                        print(">> Change PIN")
                        print(">> View/print nearby ATMs")
                        print(">> Manage cash trackers")
                        print(">> Change ATM privacy settings")
                # Memilih opsi kembali dan jika opsinya adalah mengganti bahasa
                options = str(input("Find and select options: "))
                if options == "Change Language":
                            language = str(input("Change language to: "))
                            if language == "English":
                                print("Your language has successfully changed. We'll get you back to Main Menu...")
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
                            elif language == "Indonesia":
                                print("Bahasa telah diganti. Kami akan mengembalikan Anda ke Menu Utama...")
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
            # Jika tidak lanjut, maka kartu akan dikembalikan
            elif cont == "No":
                        active = False
                        currentlanguage = "English"
                        print("Waiting for your card to come out...")
                        print("Please take your card.")
                        print("Thank you for using our service.")
                        break
        # Dalam bahasa Indonesia
        if currentlanguage == "Indonesia":
            if currentlanguage != "English":
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
                menu = str(input("Pilih menu: "))
                if menu == "Opsi lain":
                    print("OPSI LAIN")
                    print(">> Pengaturan dan Layanan ATM")
                    print(">> Hadiah Saya")
                    print(">> Layanan Wells Fargo")
                choice = str(input("Masukkan pilihan: "))
                if choice == "Pengaturan dan Layanan ATM":
                    print("PENGATURAN DAN LAYANAN ATM")
                    print(">> Ganti Bahasa")
                    print(">> Ganti PIN")
                    print(">> Lihat ATM terdekat")
                    print(">> Atur lacak tunai")
                    print(">> Ubah privasi ATM")
                options = str(input("Pilih opsi lebih lanjut: "))
                # Jika ingin mengganti bahasa terlebih dahulu
                if options == "Ganti Bahasa":
                            language = str(input("Ganti bahasa ke: "))
                            if language == "English":
                                currentlanguage = "English"
                                print("Your language has successfully changed. We'll get you back to Main Menu...")
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
                            elif language == "Indonesia":
                                print("Bahasa telah diganti. Kami akan mengembalikan Anda ke Menu Utama...")
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
                if options == "Ganti PIN":
                    print("Masukkan PIN lama: ")
                    print("_ _ _ _ _ _")
                    # Input PIN lama ke dalam array
                    inputoldpin = [int(input("Masukkan PIN lama urutan ke-" + str(i + 1) + ": ")) for i in range (len(oldpin))]
                    # Mengecek apakah PIN lama yang terdaftar sama dengan yang diinput
                    for i in range(len(inputoldpin)):
                        active = True
                        correct = False
                        if inputoldpin[i] == oldpin[i]:
                            correct = True
                        else:
                            correct = False
                    # Input PIN baru jika input PIN lama benar
                    if correct == True:
                        print("Menyesuaikan...")
                        print("Masukkan PIN baru: ")
                        print("_ _ _ _ _ _")
                    else: 
                        print("PIN yang Anda masukkan salah. Silakan coba lagi")
                    # Input PIN baru
                    if correct == True:
                        inputnewpin = [int(input("Masukkan PIN baru urutan ke-" + str(i + 1) + ": ")) for i in range (len(oldpin))]
                        print("Konfirmasi PIN baru: ")
                        print("_ _ _ _ _ _")
                    # Konfirmasi input PIN baru
                    if correct == True:
                        confirmnewpin = [int(input("Konfirmasi PIN baru urutan ke-" + str(i + 1) + ": ")) for i in range (len(inputnewpin))]
                        if confirmnewpin[i] == inputnewpin[i]:
                            print("PIN Anda berhasil diganti.") 
                            print("PIN baru Anda adalah", (confirmnewpin))
            # Pertanyaan untuk lanjut menggunakan ATM atau tidak
            cont = str(input("Apakah Anda ingin melanjutkan transaksi? "))
            # ATM tetap beroperasi jika user akan lanjut menggunakan ATM
            if cont == "Ya":
                    active = True   
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
                    # Memilih menu kembali
                    menu = str(input("Pilih menu: "))
                    if menu == "Opsi lain":
                            print("OPSI LAIN")
                            print(">> Pengaturan dan Layanan ATM")
                            print(">> Hadiah Saya")
                            print(">> Layanan Wells Fargo")
                    choice = str(input("Masukkan pilihan: "))
                    if choice == "Pengaturan dan Layanan ATM":
                            print("PENGATURAN DAN LAYANAN ATM")
                            print(">> Ganti Bahasa")
                            print(">> Ganti PIN")
                            print(">> Lihat ATM terdekat")
                            print(">> Atur lacak tunai")
                            print(">> Ubah privasi ATM")
                    options = str(input("Pilih opsi lebih lanjut: "))
                    if options == "Ganti Bahasa":
                            language = str(input("Ganti ke bahasa: "))
                            if language == "English":
                                currentlanguage = "English"
                                print("Your language has successfully changed. We'll get you back to Main Menu...")
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
                            elif language == "Indonesia":
                                print("Bahasa telah diganti. Kami akan mengembalikan Anda ke Menu Utama...")
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
            # Jika tidak lanjut, maka kartu akan dikembalikan
            elif cont == "Tidak":
                            active = False
                            print("Menunggu hingga kartu Anda keluar...")
                            print("Silakan ambil kartu Anda.")
                            print("Terima kasih atas kepercayaan Anda menggunakan layanan kami.")
                            break