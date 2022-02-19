print('    KONVERSI MASEHI KE JULIAN DAY')
print('=====================================')

D = int(input('Masukkan tanggal: '))
M = input('Masukkan bulan: ')
Y = int(input('Masukkan tahun: '))

if M == 'Januari':
  Bln = 13
  Th = Y-1

elif M == 'Februari':
  Bln = 14
  Th = Y-1

elif M == 'Maret':
  Bln = 3
  Th = Y

elif M == 'April':
  Bln = 4
  Th = Y

elif M == 'Mei':
  Bln = 5
  Th = Y

elif M == 'Juni':
  Bln = 6
  Th = Y

elif M == 'Juli':
  Bln = 7
  Th = Y

elif M == 'Agustus':
  Bln = 8
  Th = Y

elif M == 'September':
  Bln = 9
  Th = Y

elif M == 'Oktober':
  Bln = 10
  Th = Y

elif M == 'November':
  Bln = 11
  Th = Y

elif M == 'Desember':
  Bln = 12
  Th = Y

else:
	None

A = int(Y/100)
B = 2 + int(A/4) - A

JD = 1720994.5 + int(365.25*Th) + int(30.60001*(Bln+1)) + B + D

print('\nJadi',D,M,Y,'=','JDE',JD)
