
import requests,re,os
import time
import sys
from os import system
from platform import platform
from time import sleep
import os
puk = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]
os.system("title CAMERA-HACK")
os.system("color a")

if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'

os.system(delet)
time.sleep(1)

print("loading modules...")
time.sleep(0.05)
os.system(delet)
print("lOading modules...")
time.sleep(0.05)
os.system(delet)
print("loAding modules...")
time.sleep(0.1)
os.system(delet)
print("loaDing modules...")
time.sleep(0.1)
os.system(delet)
print("loadIng modules...")
time.sleep(0.1)
os.system(delet)
print("loadiNg modules...")
time.sleep(0.1)
os.system(delet)
print("loadinG modules...")
time.sleep(0.1)
os.system(delet)
print("loading modules...")
time.sleep(0.1)
os.system(delet)
print("loading mOdules...")
time.sleep(0.1)
os.system(delet)
print("loading moDules...")
time.sleep(0.1)
os.system(delet)
print("loading modUles...")
time.sleep(0.1)
os.system(delet)
print("loading moduLes...")
time.sleep(0.1)
os.system(delet)
print("loading modulEs...")
time.sleep(0.1)
os.system(delet)
print("loading moduleS...")
time.sleep(0.1)
os.system(delet)
print("loading modules...")
time.sleep(0.1)
os.system(delet)
print("Loading modules...")
time.sleep(0.1)
os.system(delet)
print("lOading modules...")
time.sleep(0.1)
os.system(delet)
print("loAding modules...")
time.sleep(0.1)
os.system(delet)
print("loaDing modules...")
time.sleep(0.1)
os.system(delet)
print("loadIng modules...")
time.sleep(0.1)
os.system(delet)
print("loadiNg modules...")
time.sleep(0.1)
os.system(delet)
print("loadinG modules...")
time.sleep(0.1)
os.system(delet)
print("loading Modules...")
time.sleep(0.1)
os.system(delet)
print("loading mOdules...")
time.sleep(0.1)
os.system(delet)
print("loading moDules...")
time.sleep(0.1)
os.system(delet)
print("loading modUles...")
time.sleep(0.1)
os.system(delet)
print("loading moduLes...")
time.sleep(0.1)
os.system(delet)
print("loading modulEs...")
time.sleep(0.1)
os.system(delet)
print("loading moduleS...")
time.sleep(0.1)
os.system(delet)
print("loading modules...")
time.sleep(0.3)
os.system(delet)
print("""
 _    _ ___________ _   _   ___  _____  _   __ 
| |  | |  ___| ___ \ | | | / _ \/  __ \| | / / 
| |  | | |__ | |_/ / |_| |/ /_\ \ /  \/| |/ /  
| |/\| |  __|| ___ \  _  ||  _  | |    |    \  
\  /\  / |___| |_/ / | | || | | | \__/\| |\  \ 
 \/  \/\____/\____/\_| |_/\_| |_/\____/\_| \_/ 
______  __   __  
| ___ \ \ \ / /  
| |_/ /  \ V /    
| ___ \   \ /       
| |_/ /   | |       
\____/    \_/  
 _____  _   _ _____ _   _  __   _______   ______ _   _  _____   
/  __ \| | | |_   _| \ | | \ \ / /_   _| |___  /| | | ||  ___| 
| /  \/| |_| | | | |  \| |  \ V /  | |      / / | |_| || |__     
| |    |  _  | | | | . ` |   \ /   | |     / /  |  _  ||  __|    
| \__/\| | | |_| |_| |\  |   | |  _| |_  ./ /___| | | || |___   
 \____/\_| |_/\___/\_| \_/   \_/  \___/  \_____/\_| |_/\____/   
""")
time.sleep(5)
os.system(delet)
print('------Version 1.2------\n')
time.sleep(5)
os.system(delet)
print("""
Follow Me On GitHub! 
https://github.com/iamhellaweiri
------Version 1.2------
""")
time.sleep(4)
os.system(delet)
print(r"""
 _____   ___  ___  ___ ___________  ___             _   _   ___  _____  _   __
/  __ \ / _ \ |  \/  ||  ___| ___ \/ _ \           | | | | / _ \/  __ \| | / /
| /  \// /_\ \| .  . || |__ | |_/ / /_\ \  ______  | |_| |/ /_\ \ /  \/| |/ / 
| |    |  _  || |\/| ||  __||    /|  _  | |______| |  _  ||  _  | |    |    \ 
| \__/\| | | || |  | || |___| |\ \| | | |          | | | || | | | \__/\| |\  \
 \____/\_| |_/\_|  |_/\____/\_| \_\_| |_/          \_| |_/\_| |_/\____/\_| \_/
""")
print("Welcome to camera-hack!")
print("Please select country to hack :")
print("""
1. Russian Federation                        
2. United States                           
3. Japan                                        
4. Canada                                     
5. New Zealand                           
6. Ukraine                       
7. Germany                       
8. Austria                       
9. Spain                       
10. Turkey 
11. Hong Kong
12. Greece
13. Portugal
14. Singapure
15. Columbia
----Project by Chin Yi Zhe----
Follow Me On GitHub! 
https://github.com/iamhellaweiri
------Version 1.2------                      
""")
num = int(input("country : "))
if num == 1:
        print("\n")		
        os.system(delet)
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,82):
			
                url = ("https://www.insecam.org/en/bycountry/RU/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("1",hasil)

                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()

                     count += 1
        except:
            print ("") 
if num == 2:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,720):
			
                url = ("https://www.insecam.org/en/bycountry/US/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("1",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")
if num == 3:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,232):
			
                url = ("https://www.insecam.org/en/bycountry/JP/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("1",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")
if num == 4:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,38):
			
                url = ("https://www.insecam.org/en/bycountry/CA/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("1",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")             
if num == 5:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,5):
			
                url = ("https://www.insecam.org/en/bycountry/NZ/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("1",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")             
if num == 6:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,2):
			
                url = ("https://www.insecam.org/en/bycountry/UK/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("1",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ") 
if num == 7:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,107):
			
                url = ("https://www.insecam.org/en/bycountry/DE/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("1",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")
if num == 8:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,48):
			
                url = ("https://www.insecam.org/en/bycountry/AT/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("1",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                     count += 1
        except:
            print (" ")           
if num == 9:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,39):
			
                url = ("https://www.insecam.org/en/bycountry/ES/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")  
if num == 10:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,54):
			
                url = ("https://www.insecam.org/en/bycountry/TR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")             
if num == 11:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,7):
			
                url = ("https://www.insecam.org/en/bycountry/HK/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("1",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")  
if num == 12:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,8):
			
                url = ("https://www.insecam.org/en/bycountry/GR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("1",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")           
if num == 13:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,7):
			
                url = ("https://www.insecam.org/en/bycountry/PT/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("1",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")        
if num == 14:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,7):
			
                url = ("https://www.insecam.org/en/bycountry/SG/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("1",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()

                     count += 1
        except:
            print (" ")      
if num == 15:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,6):
			
                url = ("https://www.insecam.org/en/bycountry/CO/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("1",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ") 


