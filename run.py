import requests,random,json,os,time
from time import sleep
from bs4 import BeautifulSoup
from multiprocessing import Pool
cwd = os.getcwd()
random_angka = random.randint(100,999)
random_angka_dua = random.randint(10,99)


def sign_up(k):
    file_list_akun = "code_ref.txt"
    myfile_akun = open(f"{cwd}/{file_list_akun}","r")
    code_ref = myfile_akun.read()
    header = {"accept-encoding": "gzip, deflate",
         "content-type": "application/json; charset=utf-8",
        
            "cookie": '_ga=GA1.1.418201028.1641224508; _fbp=fb.1.1641224509340.1058958369; _ga_6C93RLFG30=GS1.1.1641224507.1.1.1641224515.0; _ga_H6Q8L0FGFB=GS1.1.1641224508.1.1.1641224515.0; _ga_YJTZ96DES0=GS1.1.1641224508.1.1.1641224515.0; _ga_QW2R1VMDSF=GS1.1.1641224508.1.1.1641224515.0; _ga_Q61Z137B5R=GS1.1.1641224508.1.1.1641224515.0; _ga_9DE6ZQVNSE=GS1.1.1641224508.1.1.1641224515.0',
            
            "content-type": "application/json",
        
            "referer": f"https://vconomics.io/en/sign-up?ref={code_ref}",
            
            "user-agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            "Host": "vconomics.io",
            "Origin": "https://vconomics.io"

    }
    k = k
    file_list_akun = "prefix.txt"
    myfile_akun = open(f"{cwd}/{file_list_akun}","r")
    prefix = myfile_akun.read()
    
    prefix_email = prefix.split("@")
    get_mail = prefix_email[1]
    get_user = prefix_email[0]
    email = get_user+f"{k}"+"@"+get_mail
    file_list_akun = "password.txt"
    myfile_akun = open(f"{cwd}/{file_list_akun}","r")
    password = myfile_akun.read()
     
    
    n = 1
    while True:
        if n == 100:
            print(f"[*] [{email}] Internal Server Error: Finish!") 
            status = False
            break
    
        status = True
        r = requests.post('https://vconomics.io/identity/accounts/register/4', json={"userName": f"{email}","password": f"{password}","rePassword": f"{password}","fromReferralId": f"{code_ref}","fullName": f'{random.choice(["Bellamy","Nurman","Herman","Michael","Michelle","Jeniffer","Robby"])} {random.choice(["Bellamy","Nurman","Herman","Michael","Michelle","Jeniffer","Robby"])} {random.choice(["Bellamy","Nurman","Herman","Michael","Michelle","Jeniffer","Robby"])}'},headers=header)
 
        soup = BeautifulSoup(r.text, 'html.parser')
       
        try:
            res = json.loads(soup.text)
             
        except:
            pass
        if str(soup) == "Internal Server Error":
            print(f"[*] [{email}] Internal Server Error: Reload!")  
        
        elif res["message"] == "UN_DETECTED_ERROR":
            print(f"[*] [{email} CHANGE IP!!! "+res["message"]) 
            quit()
        else:
            break
    n=1
    while True:
        if status == False:
            break
        if n == 100:
            print("[*] Verification Failed!")
            break
        URL = f'https://getnada.com/api/v1/inboxes/{email}'
        r = requests.get(URL).json()
        #getting the latest message
        
        try:
            global uid
            sleep(1)
            uid = r['msgs'][0]['uid']
        
            mes = requests.get(f'https://getnada.com/api/v1/messages/html/{uid}')
            mes1 = BeautifulSoup(mes.content,'html.parser')
            get_data = mes1.prettify()
           
            text = get_data.split(r'<p style="color: #fa7800; font-weight: bold; text-align: center; font-size: 40px;">')
            text = text[1].split(r"</p>")
            get_code = text[0]
            print(f"[*] [{email}] Code: {get_code.strip()}")
            with open('ress.txt','w') as f:
                f.write(f"{email}|{get_code}\n")
            break
        except IndexError:
            
            print(f"[*] [{email} Your Email doesn't have a new message, Reload!")
            n = n+1
     

if __name__ == '__main__':
    global prefix
    global password
    print("[*] Auto Creator Vconomics!")
    prefix = input("[*] Main Email (Using domain @tafmail.com): ")
    password = input("[*] Password: ")
    jumlah = input("[*] Multiprocessing: ")
    with open('password.txt','w') as f:
        f.write(password)
    code_ref = input("[*] Code Reff: ")    
    with open('code_ref.txt','w') as f:
        f.write(code_ref)
    loop_input = int(input("[*] How Much Account: "))
    with open('loop.txt','w') as f:
        f.write('')
    with open('prefix.txt','w') as f:
        f.write(prefix)
    for i in range(1, loop_input+1):
        with open('loop.txt','a+') as f:
            f.write(f'{i}\n')
    file_list_akun = "loop.txt"
    myfile_akun = open(f"{cwd}/{file_list_akun}","r")
    akun = myfile_akun.read()
    list_accountsplit = akun.split()
    k = list_accountsplit
    start = time.time()
    with Pool(int(jumlah)) as p:  
        p.map(sign_up, k)
        
    
    end = time.time()
    print("[*] Time elapsed: ", start - end)
