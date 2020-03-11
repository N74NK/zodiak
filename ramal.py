# Code by NY (njank yuti)
import os
from datetime import date
from bs4 import BeautifulSoup as ny_bs

"""
Dibuat oleh Njank Yuti dengan ilmu pengetahuan bumi dan langit
Recode kontolnya pecah!
"""

try:
	import requests
except ModuleNotFoundError:
	os.system('pip install requests bs4')

def ny_menu0():
	ny_date = date.today().strftime('%B %d, %Y')
	'''
	Njank Yuti, buyut Subanglarang
	'''
	print(f'''\n
       . v1
  ---./|\.---    
  '._/ | \_.'    Ramalan Zodiak
_.-'_'.|.'_'-._  
 '-._.'|'._.-'   author: Njank Yuti 
  .' \ | / '.    info: Ramal Zodiakmu hari ini
  ---'\|/'---    date: {ny_date}
       ' 
Silahkan pilih Zodiakmu untuk melihat ramalan hari ini
 
 1) Aries    4) Cancer   7) Libra     10) Capricorn
 2) Taurus   5) Pisces   8) Scorpio   11) Sagittarius
 3) Gemini   6) Virgo    9) Leo       12) Aquarius
 
 i) Info Lengkap
 x) Keluar
''')
	ny_zod0=input('Zodiak: ')
	if ny_zod0 == '1':
		ny_zod1 = 'aries'
	elif ny_zod0 == '2':
		ny_zod1 = 'taurus'
	elif ny_zod0 == '3':
		ny_zod1 = 'gemini'
	elif ny_zod0 == '4':
		ny_zod1 = 'cancer'
	elif ny_zod0 == '5':
		ny_zod1 = 'pisces'
	elif ny_zod0 == '6':
		ny_zod1 = 'virgo'
	elif ny_zod0 == '7':
		ny_zod1 = 'libra'
	elif ny_zod0 == '8':
		ny_zod1 = 'scorpio'
	elif ny_zod0 == '9':
		ny_zod1 = 'leo'
	elif ny_zod0 == '10':
		ny_zod1 = 'capricorn'
	elif ny_zod0 == '11':
		ny_zod1 = 'sagittarius'
	elif ny_zod0 == '12':
		ny_zod1 = 'aquarius'
	elif ny_zod0 == 'i' or ny_zod0 == 'I':
		print('''

Info script:
Script dibuat oleh NjankYuti.
Untuk melihat ramalan bintang/zodiak hari ini menurut peta alam semesta pada lokasi tertentu di waktu tertentu.
Ini dipakai untuk memprediksi kejadian berdasarkan asumsi bahwa ada hubungan antara fenomena benda langit dengan kejadian yang dialami manusia.


Link author:
https://github.com/N74NK
https://facebook.com/njnk.xnxx
https://facebook.com/njnk.real
https://instagram.com/n74nk420
https://youtube.com/NjankSoekamti
https://solozstring.blogspot.com
https://n74nk.github.io

		''')
	elif ny_zod0 == 'x' or ny_zod0 == 'X':
		exit('Program dihentikan')
	else:
		exit('Error: input tidak benar')
	try:
		return ny_zod1
	except Exception as ny_er:
		exit()
		

def ny_menu1(ny_zod1):
	'Njank Yuti, buyut Subanglarang'
	ny_url = requests.get(f'http://gemintang.com/ramalan-bintang-setiap-hari/ramalan-{ny_zod1}-hari-ini/').text
	ny_soup = ny_bs(ny_url,'html.parser')
	for ny_contol in ny_soup.find_all('td',{'align':'center','colspan':'2'})[1:2]:
		'''
		Kepo banget sih lu goblog
		sampe stalking ke bawah
		takut logger?
		ini gak need login kontol
		'''
		__ny = ny_contol.text.replace('(adsbygoogle = window.adsbygoogle || []).push({});','').replace('''\n''','').replace('. ','''.\n''')
		print("\nRamalan zodiak "+ny_zod1+" hari ini:\n"+__ny)

if __name__ == '__main__':
	os.system('clear')
	try:
		ny_zod1 = ny_menu0()
		ny_menu1(ny_zod1)
	except Exception as ny_er:
		print(f'Error: {ny_er}')