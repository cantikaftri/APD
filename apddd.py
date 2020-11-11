import os  

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

        
def option():
    clear_screen()
    print("-----------------------------------------------")
    print("Selamat Datang di Program Operasi Aritmatika")
    print("Nama : Cantika Fitri Ayu Darmayanti")
    print("NIM  :2009106045")
    print("-----------------------------------------------")
    print("Menu Pilihan :")
    print("[1] Penjumlahan")
    print("[2] Pengurangan")
    print("[3] Perkalian")
    print("[4] Pembagian")
    print("[5] Sisa Bagi Modulus")
    print("[0] Keluar")
    print("Masukkan Option")
    option = int(input("Option :"))
    if option==1:
        a=int(input("Masukan Bilangan Pertama : "))
        b=int(input("Masukan Bilangan Kedua   : "))
        c=a+b
        print(c)
        back_to_option()
    elif option==2:
        a=int(input("Masukan Bilangan Pertama : "))
        b=int(input("Masukan Bilangan Kedua   : "))
        c=a-b
        print(c)
        back_to_option()
    elif option==3:
        a=int(input("Masukan Bilangan Pertama : "))
        b=int(input("Masukan Bilangan Kedua   : "))
        c=a*b
        print(c)
        back_to_option()
    elif option==4:
        a=int(input("Masukan Bilangan Pertama : "))
        b=int(input("Masukan Bilangan Kedua   : "))
        c=a/b
        print(c)
        back_to_option()
    elif option==5:
        a=int(input("Masukan Bilangan Pertama : "))
        b=int(input("Masukan Bilangan Kedua   : "))
        c=a%b
        print(c)
        back_to_option()
    elif option==0:
        print("Terimakasih")
        exit()
    else:
        print("Maaf Menu Tidak Tersedia")
        back_to_option()

    
def back_to_option():
    print("\n")
    input("Tekan Enter Untuk Kembali...")
    option()
    

#program utama
option()
back_to_option()


    