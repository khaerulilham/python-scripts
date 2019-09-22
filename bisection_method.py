#!/bin/env python3

# Bisection Method with error tolerance
# 21-09-2019

from math import pow


# fungsi untuk melakukan perhitungan metode bisection
def bisection(func, a, b, nmax, emax):
    # jika hasil dari f(a) * f(b) adalah nol, maka tidak dapat dilanjutkan
    # penggunaan ini lebih efisien, karena tidak perlu periksa satu-persatu
    # antara f(a) dan f(b), karena nilai berapapun dikalikan dengan 0 akan
    # menghasilkan nol
    if (func(a) * func(b)) == 0:
        return False
    else:
        # nilai awal x (saat iterasi belum > 1
        # nilai tengah
        xbase = (a + b)/2

        # inisialisasi
        xold = xbase

        i = 1

        # iterasi berdasarkan nmax
        while i < nmax:
        # iterasi tanpa akhir, akan berakhir jika akar ditemukan
        # while True:
            # membuat variable xnew untuk menampung nilai x yang baru
            xnew = (a + b)/2

            # menghitung fungsi
            fa = func(a)
            fb = func(b)
            fx = func(xnew)
            fxb = func(xbase)

            # menghitung toleransi error menggunakan nilai absolut
            err = abs((xnew - xold) / xnew)

            # Jika iterasi sudah dilakukan lebih dari 1 kali
            if i > 1:
                # debuging
                print('\n---------------')
                print(f'iter: {i}')
                print('---------------')
                print(f'a: {a:.5f}')
                print(f'b: {b:.5f}')
                print(f'x: {xnew:.5f}')
                # print(f'xold: {xold:.5f}')
                print('---------------')
                print(f'fa: {fa:.5f}')
                print(f'fb: {fb:.5f}')
                print(f'fx: {fx:.5f}')
                print('---------------')
                print(f'err: {err:.5f}')

                # jika toleransi error lebih kecil dari max error
                # maka iterasi berakhir dan mengembalikan nilai x yang baru
                if err < emax:
                    return xnew
                # jika tidak, maka:
                else:
                    if (fa * fx) < 0:
                        # menyimpan xnew pada xold, agar value dari xnew
                        # tidak hilang
                        xold = xnew
                        b = xnew
                    else:
                        xold = xnew
                        a = xnew
            else:
                # jika f(a) x f(x) kurang dari 0
                # maka b = x
                if (fa * fxb) < 0:
                    b = xbase
                else:
                    a = xbase

            # increment
            i += 1
        else:
            return False


if __name__ == '__main__':
    # parameter 1 -> fungsi matematika
    #           2 -> interval awal
    #           3 -> interval akhir
    #           4 -> banyaknya iterasi
    #           5 -> error maksimal
    # x = bisection(func1, 5, 10, 15, 0.0001)

    # membuat fungsi
    def func1(x):
        return ((2 * pow(x, 3)) - (5 * pow(x, 2)) - (74 * x) - 112)

    def func2(x):
        return (1 * pow(x, 3)) - (3 * x) + 1

    # menjalankan fungsi bisection dengan memasukan fungsi2
    bsc = bisection(func2, 0, 1, 18, 0.0001)

    if not bsc:
        print(f'\nAkar tidak ditemukan')
    else:
        print(f'\nJadi akarnya adalah: {bsc}')
