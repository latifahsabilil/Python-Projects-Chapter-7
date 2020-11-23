print('-----------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('-----------------------------')

jumlah = 0
data = 0
while True : 
    try :
        bil = int(input('Masukkan bilangan bulat: '))
        tanya = input('Lagi (y/n)? : ')
        jumlah += bil
        data += 1
        if (tanya == 'y') :
            True
        elif (tanya == 'n') :
            False
            break
        else :
            print('Input tidak valid')
            continue
    except ValueError:
        print('Bukan bilangan bulat')
rata_rata = jumlah/data
print('Rata-ratanya adalah ', rata_rata)

        
