import os
import sys
import time
os.system('clear')

''' perkalian , pembagian , pengurangan , penambahan
dengan python 2.7 '''

BM = '\x1b[1;96m' # BIRU MUDA
NC = '\x1b[0m'    # WARNA MATI

# _fungsi untuk gaya gaya :v
banner="""
________ _______ __________________
___  __ \___    |___  ____/____  _/ \t-={ creat by : Rafi }=-
__  /_/ /__  /| |__  /_     __  /\t _____rafi tools_____
_  _, _/ _  ___ |_  __/    __/ /   
/_/ |_|  /_/  |_|/_/       /___/   \t\x1b[1;96mcalculator sederhana\n\t\t\t\t\tdengan python \x1b[1;91m2.7\x1b[1;97m

[ \x1b[1;92msilahkan pilih sesuai menu yang tersedia !\x1b[1;97m ]
______________________________________________________________
                                   """
# _input angka                              
print(banner)                                   
a = input("[-] masukan angka : ")
b = input("[-] masukan angka : ")
print

# _menu yang tersedia
print ' %s1%s perkalian '%(BM,NC)
print ' %s2%s pembagian '%(BM,NC)
print ' %s3%s penambahan'%(BM,NC)
print ' %s4%s pengurangan '%(BM,NC)

print
# _hasil
hasil = raw_input("[?] choose : ")
if hasil =='1':
	hasil = a*b
	print
	print("hasilnya adalah = ")
	print(BM)
	print(hasil)
	print(NC)

elif hasil =='2':
	hasil = a/b
	print
	print("hasilnya adalah = ")
	print(BM)
	print(hasil)
	print(NC)
	
elif hasil =='3':
	hasil = a+b
	print
	print("hasilnya adalah = ")
	print(BM)
	print(hasil)
	print(NC)
	
elif hasil =='4':
	hasil = a-b
	print
	print("hasilnya adalah = ")
	print(BM)
	print(hasil)
	print(NC)
	
else:
	print
	print('menu tidak tersedia ! ')
	time.sleep(1)
	os.system('python2 calculator.py')
	