class Luas:
    def __init__(self):
        self.satu = nilai1
        self.dua = nilai2
    def persegi_panjang(self,):
        print(self.satu * self.dua)
    def lingkaran(self):
        print(self.satu * self.dua * self.dua)
    def segitiga(self):
        print(1/2 * (self.satu * self.dua))

class Volume:
    def __init__(self):
        self.satu = nilai1
        self.dua = nilai2
        self.tiga = nilai3
    def kubus(self):
        print(self.satu**3)
    def balok(self):
        print(self.satu*self.dua*self.tiga)
    def bola(self):
        print(self.satu*self.dua*(self.tiga**3))
    def tabung(self):
        print(self.satu*(self.dua**2)*self.tiga)
    def kerucut(self):
        print(1/3*(self.satu*(self.dua**2)*self.tiga))



print( "Menghitung Luas & Volume")

while True:
    print("\n1. Menghitung Luas \n2. Menghitung Volume \n3. Keluar")
    pilihan = int(input("Silahkan Input Pilihan Untuk Melanjutkan: "))
    if pilihan == 1:
            print("\n1. Persegi / Persegi Panjang \n2. Lingkaran \n3. Segitiga \n4. Kembali")
            pilihan = int(input("Silahkan Input Pilihan Untuk Melanjutkan: "))
            if pilihan == 1:
                nilai1 = float(input("Input panjang persegi : "))
                nilai2 = float(input("Input lebar persegi : "))
                hasil = Luas()
                hasil.persegi_panjang()
                print("Lanjut?")
                print("Ketik ya untuk lanjut & tidak untuk berhenti")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break             
            elif pilihan == 2:
                nilai1 = 3.14
                nilai2 = float(input("Input Jari-Jari Lingkaran : "))
                hasil = Luas()
                hasil.lingkaran()
                print("Lanjut?")
                print("Ketik ya untuk lanjut & tidak untuk berhenti")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break            
            elif pilihan == 3:
                nilai1 = float(input("Input Tinggi Segitiga : "))
                nilai2 = float(input("Input Alas Segitiga : "))
                hasil = Luas()
                hasil.segitiga()
                print("Lanjut?")
                print("Ketik ya untuk lanjut & tidak untuk berhenti")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break            
            elif pilihan == 4:
                break
            else:
                print("Perintah Tidak Ditemukan")
    elif pilihan == 2:
            print("\n1. Kubus \n2. Bola \n3. Tabung \n4. Kerucut \n5. Kembali")
            pilihan = int(input("Input Pilihan : "))
            if pilihan == 1:
                nilai1 = float(input("Input panjang rusuk : "))
                nilai2 = 0
                nilai3 = 0
                hasil = Volume()
                hasil.kubus()
                print("Lanjut?")
                print("Ketik ya untuk lanjut & tidak untuk berhenti")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break            
            
            elif pilihan == 2:
                nilai1 = 4/3
                nilai2 = 3.14
                nilai3 = float(input("Input Jari-Jari Bola : "))
                hasil = Volume()
                hasil.bola()
                print("Lanjut?")
                print("Ketik ya untuk lanjut & tidak untuk berhenti")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break            
            elif pilihan == 3:
                nilai1 = 3.14
                nilai2 = float(input("Input Jari-Jari Lingkaran : "))
                nilai3 = float(input("Input Tinggi Tabung : "))
                hasil = Volume()
                hasil.tabung()
                print("Lanjut?")
                print("Ketik ya untuk lanjut & tidak untuk berhenti")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break            
            elif pilihan == 4:
                nilai1 = 3.14
                nilai2 = float(input("Input Jari-Jari Lingkaran : "))
                nilai3 = float(input("Input Tinggi Kerucut : "))
                hasil = Volume()
                hasil.kerucut()
                print("Lanjut?")
                print("Ketik ya untuk lanjut & tidak untuk berhenti")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break            
            elif pilihan == 5:
                break
            else:
                print("Perintah Tidak Ditemukan")

    elif pilihan == 3:
        break
    else:
        print("Perintah Tidak Ditemukan")