import time
from datetime import datetime as dt


#setting up the script
hosts_temp = 'C:\Users\HP\Documents\GitHub\Python_projects\Website_blocker_app\hosts'
hosts_path = 'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
website_list = ['www.facebook.com', 'facebook.com', 'mail.google.com',
               'www.mail.google.com', 'livescore.com', 'www.livescore.com']

#set up the infinite loop
while True:
    if dt(dt.now().year, dt.now().month,dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 15):
        print('Working hours...')
        with open(hosts_temp, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+ "\n")
    else:
        with open(hosts_temp, 'r+') as file:
            content=file.readline()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print('Fun hours...')
    time.sleep(5)
'''changing hosts_temp to hosts_temp and restarting you browser will these codes affect you browserin real time.'''
