donaturList = [
    {
        "date": 12,
        "month": "Feb",
        "years": 2024,
        "donate": 2000000,
        "admin": -2000,
        "donatur": {
            "name": "Jhon",
            "addres": "jakarta"
        },
        "bank": "BCA"
    },
    {
        "date": 10,
        "month": "March",
        "years": 2024,
        "donate": 1000000,
        "admin": 0,
        "donatur": {
            "name": "Loki",
            "addres": "banten"
        },
        "bank": "Mandiri"
    },
]

print("#==================== DETAIL INFORMATION  ==========================#")
for m in donaturList:
    print()
    print("Name: ", m['donatur']['name'])
    print("Berdonasi sebesar: ", "Rp.", m['donate'])
    
    if not m['admin']:
        print("Tidak ada potongan admin")
    else:
        donate = m['donate']
        admin = m['admin']
        dec = donate + admin
        print("Potongan admin: ", "Rp.", abs(admin))
        print("Sisa uang: ", "Rp.", dec)
    
    print("Bank name: ", m['bank'])
    print()

total_donate = sum(m['donate'] for m in donaturList)
print()
print("Total amount: ", "Rp.", total_donate)
print()
print("#==================== Thank you for your donations!  ==========================#")