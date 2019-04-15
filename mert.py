#!/usr/bin/python

import os
import sys, traceback

def main():
	try:
		print ('''
Varto-lu
''')
		def inicio1():
			while True:
				print ('''
1) Kali havuzları ekle & Güncelle
2) Kategorileri Görüntüle
3) Classic menu göstergesini yükle
4) Kali menüsünü yükle
5) Yardım

			''')

				opcion0 = raw_input("\033[1;36mkat > \033[1;m")

				while opcion0 == "1":
					print ('''
1) Kali linux depoları ekle
2) Güncelleştirme
3) Tüm kali linux depolarını kaldır
4) Sources.list dosyasının içeriğini görüntüleyin

					''')
