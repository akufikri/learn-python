# Credentials
names = "fikri"
passwords = "123"
bankName = "BRI"
bankNumber = 441231123

# Data akun
data = [
    {
        "detail": {
            "name": names,
            "bank_name": bankName,
            "bank_number": bankNumber
        },
        "amount": 1000000,  # Saldo awal
        "transaction": {
            "in": 0,
            "out": 0
        }
    }
]

# Fungsi login
def login():
    name = input("Username: ")
    password = input("Password: ")
    if name == names and password == passwords:
        return True
    else:
        return False

# Fungsi cek saldo
def cek_saldo():
    print("============= Balance Information =============")
    for d in data:
        print(f"Name: {d['detail']['name']}")
        print(f"Bank Name: {d['detail']['bank_name']}")
        print(f"Bank Number: {d['detail']['bank_number']}")
        print(f"Current Balance: Rp {d['amount']}")
        print("==============================================")

# Fungsi deposit saldo
def deposit_saldo():
    try:
        deposit = int(input("Masukkan jumlah deposit: Rp "))
        if deposit > 0:
            for d in data:
                d['amount'] += deposit
                d['transaction']['in'] += deposit
            print(f"Rp {deposit} berhasil ditambahkan ke saldo Anda.")
        else:
            print("Jumlah deposit harus lebih dari 0.")
    except ValueError:
        print("Masukkan jumlah dalam angka.")

# Fungsi menu utama
def menu():
    while True:
        print("\n=========== Mini ATM Menu ===========")
        print("1. Cek Saldo")
        print("2. Deposit Saldo")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            cek_saldo()
        elif pilihan == "2":
            deposit_saldo()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan layanan kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Main program
if login():
    print("\nLogin berhasil! Selamat datang di Mini ATM.")
    menu()
else:
    print("Login gagal. Username atau password salah.")