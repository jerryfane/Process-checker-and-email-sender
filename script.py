import subprocess
import requests
import urllib.request

process_name = 'firefox.exe'          #Modifica qui
seconds = 3600                        #Modifica qui
domain = 'Your mailgun domain'        #Modifica qui
api = 'Your mailgun domain API'       #Modifica qui
email = 'your receiving email'        #Modifica qui ---> your email needs to be verified my mailgun!

my_ip = urllib.request.urlopen('http://ip.42.pl/raw').read()

def send_simple_message_not_running(to):
    url = 'https://api.mailgun.net/v3/{}/messages'.format(domain)
    auth = ('api', api)
    data = {
        'from': 'Mailgun User <mailgun@{}>'.format(domain),
        'to': to,
        'subject': process_name+' is not running at: '+str(my_ip),
        'text': "I'm sorry to disturb you dear Boss, but "+process_name+" is not running at: "+str(my_ip)+', please fix it asap.',
    }

    response = requests.post(url, auth=auth, data=data)
    response.raise_for_status()
				  
def send_simple_message_not_responding(to):
    url = 'https://api.mailgun.net/v3/{}/messages'.format(domain)
    auth = ('api', api)
    data = {
        'from': 'Mailgun User <mailgun@{}>'.format(domain),
        'to': to,
        'subject': process_name+' is not responding at: '+str(my_ip),
        'text': "I'm sorry to disturb you dear Boss, but "+process_name+' is not responding at: '+str(my_ip)+', please fix it asap.',
    }

    response = requests.post(url, auth=auth, data=data)
    response.raise_for_status()

import os
def isresponding(name):
    os.system('tasklist /FI "IMAGENAME eq %s" /FI "STATUS eq not responding" > tmp.txt' % name)
    tmp = open('tmp.txt', 'r')
    a = tmp.readlines()
    tmp.close()
    #true = print('True')
    #false = print('False')
    if a[-1].split()[0] == name:
        return True
    else:
        return False
		
def isrunning(name):
    os.system('tasklist /FI "IMAGENAME eq %s" /FI "STATUS eq running" > tmp.txt' % name)
    tmp = open('tmp.txt', 'r')
    a = tmp.readlines()
    tmp.close()
    #true = print('True')
    #false = print('False')
    if a[-1].split()[0] == name:
        return True
    else:
        return False

import time


while True:
    if isresponding(process_name) is True:
        print(process_name+' is not responding, sending email...')
        send_simple_message_not_responding('Youremail@gmail.com')
    else:
        print(process_name+' is responding')

    if isrunning(process_name) is False:
        print(process_name+' is not running, sending email...')
        send_simple_message_not_running('Youremail@gmail.com')
    else:
       print(process_name+' is running')
    time.sleep(seconds)
