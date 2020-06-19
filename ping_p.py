import os
import subprocess
import sys
import ipaddress
from sys import argv

DNULL = open(os.devnull, 'w')
cmd = " "
#---------------------------------------------------------------------------
def sys_():
	global cmd
	os = sys.platform
	if (os == "linux"):
		 cmd = "-c"
	else:
		cmd = "-n"
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
def check(ip_check):
	c = ip_check.split('/')
	ip = c[0].split('.')
	if (int(ip[0]) > 255 or int(ip[1]) > 255 or int(ip[2]) > 255 or int(ip[3]) > 255):
			print(" ip адрес введен не верно!")
			print(" ")
			return False
	elif int(c[1]) > 32:
		print ("Маска введена не верно!")
		return False
	else:
		return True
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
def request(ip_r):
	status = subprocess.call (["ping",cmd,"1",ip_r], stdout = DNULL)
	if status == 0:
   		print("Связь c " + ip_r + " установлена!")
	else:
   		print("Связь с " + ip_r + " не установлена!")
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
def ping(ip):
	try:
		range_ = ipaddress.ip_network(ip)
		for ip in range_:
			request(str(ip))
	except ValueError:
		ip = input("В адресе установлены биты хоста! Пожалуйста, введите другое значение: ")
		if check(ip):
			ping(ip)
		else:
			main()

#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
def main(ip_range):
	try:
		if check(ip_range):
			ping(ip_range)
		else:
			ip_range = input("Введите диапазон ip адресов  в формате 1.1.1.1/0: ")
			main(ip_range)
	except KeyboardInterrupt:
		print ("Программа остановленна!")
		sys.exit()
#---------------------------------------------------------------------------


#---------------------------------------------------------------------------
sys_()
ip_range = argv[1]
main(ip_range)
input("Нажмите любую клавишу для выхода из программы....")