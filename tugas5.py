daftar = {}
while True:
    print("")
    a = input("L)ihat, T)ambah, U)bah, H)apus, C)ari, K)eluar: ")
    if a.lower() == 'k':
        break
    
    elif a.lower() == 'l':
        print("Daftar Nilai")
        print("===================================================================")
        print("| No |   Nama         |    NIM    |Tugas  |  UTS  |  UAS  | Akhir |")
        print("===================================================================")
        no = 0
        for tabel in daftar.values():
            no += 1
            print("| {0:2} | {1:14} | {2:9} | {3:5} | {4:5} | {5:5} | {6:5} |"
                  .format (no, tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5]))
            print("===================================================================")
    elif a.lower() == 't':
        print("Tambah Data")
        nama = input("Nama       : ")
        nim = input("NIM        : ")
        uts = int(input("Nilai UTS  : "))
        uas = int(input("Nilai UAS  : "))
        tugas = int(input("Nilai Tugas: "))
        akhir = float(uts*.30) + float(uas*.35) + float(tugas*.35)
        daftar[nama]=[nama, nim, uts, uas, tugas, akhir]
    elif a.lower() == 'u':
        print("ubah daftar nilai")
        nama = input("Masukan nama yang ingin diubah datanya: ")
        if nama in daftar.keys():
            print("Nama mahasiswa: ")
            data = input("(Semua), (Nama), (NIM), (Tugas), (UTS), (UAS) : ")
            if data.lower()=="semua":
                daftar[nama][1] = input("Edit NIM:")
                daftar[nama][2] = int(input("Ubah Nilai Tugas: "))
                daftar[nama][3] = int(input("Ubah Nilai UTS: "))
                daftar[nama][4] = int(input("Ubah Nilai UAS: "))
            elif data.lower() == "nim":
                    daftar[nama][1] = input("NIM:")
            elif data.lower() == "tugas":
                    daftar[nama][2] = int(input("Nilai Tugas: "))
            elif data.lower() == "uts":
                    daftar[nama][3] = int(input("Nilai UTS: "))
            elif data.lower() == "uas":
                    daftar[nama][4] = int(input("Nilai UAS: "))
            else: print("Data tidak ditemukan.")
        else:
            print("Daftar {0} tidak ditemukan".format(nama))

    elif a.lower() == 'h':
        print("Masukan Nama yang Ingin dihapus dari daftar")
        nama = input("Nama Mahasiswa: ")
        if nama in daftar.keys():
            del daftar[nama]
            print("Data '{}' telah dihapus.".format(nama))
        else:
            print("Data tidak ditemukan".format(nama))
    elif a.lower() == 'c':
        print("Mencari Daftar Nilai")
        nama = input("Masukan nama mahasiswa untuk mencari daftar nilai : ")
        if nama in daftar.keys():
            print("Nama {0}, dengan NIM : {1}\n" "Nilai Tugas: {2}, UTS: {3}, dan UAS: {4}\n" "dan nilai akhir {5}".format(nama, daftar[nama][1], daftar[nama][2], daftar[nama][3], daftar[nama][4], daftar[nama][5]))
        else:
            print("Daftar '{}' tidak ditemukan.".format(nama))
    else:
        print("Pilih menu yang tersedia")
