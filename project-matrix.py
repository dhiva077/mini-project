print("Operasi Matriks")
while True:
    print("\n1. Penjumlahan Matriks")
    print("2. Pengurangan Matriks")
    print("3. Perkalian Matriks")
    print("4. Pembagian Matriks")
    print("5. Invers Matriks")
    print("6. Keluar")
    pilihan_operasi = int(input("Pilihan operasi (1-6): "))

    if pilihan_operasi == 1: 
        baris = int(input("Masukkan jumlah baris (max 4):  "))
        kolom = int(input("Masukkan jumlah kolom (max 4):  "))
        print("Masukkan elemen matriks pertama: ")
        mat1 = []
        for i in range(baris):
            mat1.append(list(map(int, input(f"Baris {i+1}: ").split())))
        print("Masukkan elemen matriks kedua:")
        mat2 = []
        for i in range(baris):
            mat2.append(list(map(int, input(f"Baris {i+1}:").split())))
        print("Hasil Penjumlahan Matriks:")
        for i in range(baris):
            print(" ".join(str(mat1[i][j] + mat2[i][j]) for j in range(kolom)))

    elif pilihan_operasi == 2:
        baris = int(input("Masukkan jumlah baris (max 4):  "))
        kolom = int(input("Masukkan jumlah kolom (max 4):  "))
        print("Masukkan elemen matriks pertama: ")
        mat1 = []
        for i in range(baris):
            mat1.append(list(map(int, input(f"Baris {i+1}: ").split())))
        print("Masukkan elemen matriks kedua:")
        mat2 = []
        for i in range(baris):
            mat2.append(list(map(int, input(f"Baris {i+1}:").split())))
        print("Hasil Penjumlahan Matriks:")
        for i in range(baris):
            print(" ".join(str(mat1[i][j] + mat2[i][j]) for j in range(kolom)))

    elif pilihan_operasi == 3:
        baris1 = int(input("Masukkan jumlah baris (max 4):  "))
        kolom1 = int(input("Masukkan jumlah kolom (max 4):  "))
        print("Masukkan elemen matriks pertama: ")
        mat1 = []
        for i in range(baris1):
            mat1.append(list(map(int, input(f"Baris {i+1}: ").split())))
        baris2 = int(input("Masukkan jumlah baris matriks kedua: "))
        kolom2 = int(input("Masukkan jumlah kolom matriks kedua: "))
        print("Masukkan elemen matriks kedua: ")
        mat2 = []
        for i in range(baris2):
            mat2.append(list(map(int, input(f"Baris {i+1}: ").split())))
            if kolom1 != baris2:
                print("Matriks tidak dapat dikalikan.")
            else:
                print("Hasil Perkalian Matriks")
                hasil = []
                for i in range(baris1): 
                    baris = []
                    for i in range(kolom2):
                        total = sum(mat1[i][k] * mat2[k][j] for k in range(kolom1))
                        baris.append(total)
                    hasil.append(baris)
                for baris in hasil:
                    print(" ".join(map(str, baris)))

    elif pilihan_operasi == 4:
        n = int(input("Masukkan ukuran matriks persegi (n x n, max 4): "))
        print("Masukkan elemen matriks: ")
        matrix = []
        for i in range(n):
            matrix.append(list(map(int, input(f"Baris {i+1}: ").split())))
        def determinan(matrix, n):
            if n == 1:
                return matrix[0][0]
            if n == 2:
                return matrix [0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            det == 0
            for col in range(n):
                minor = [[matrix[i][j] for j in range(n) if j != col] for i in range(1, n)]
                det += ((-1) ** col) * matrix[0][col] * determinan(minor, n-1)
            return det
        print(f"Determinan matrix: {determinan(matrix, n)}")

    elif pilihan_operasi == 5:
        n = int(input("Masukkan ukuran matrix persegi (n x n, max 4): "))
        print("Masukkan elemen matrix:")
        matrix = []
        for i in range(n):
            matrix.append(list(map(int, input(f"Baris {i+1}: ").split())))
        def determinan(matrix, n):
            if n == 1:
                return matrix[0][0]
            if n == 2:
                return matrix [0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            det = 0
            for col in range(n):
                minor = [[matrix[i][j] for j in range(n) if j != col] for i in range(1, n)]
                det += ((-1) ** col) * matrix[0][col] * determinan(minor, n-1)
            return det
        det = determinan(matrix, n)
        if det == 0:
            print("Matrix tidak memiliki invers karena determinan = 0.")
        else:
            adj = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    minor = [[matrix[baris][col] for col in range(n) if col != j] for row in range(n) if row != i]
                    adj = [[0] * n for _ in range(n)]
                print("Matrix Invers:")
                for i in range(n):
                    print(" ".join(f"{adj[i][j] / det:.2f}" for j in range(n)))

    elif pilihan_operasi == 6:
        print("Keluar dari program,")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")