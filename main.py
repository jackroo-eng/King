import os 
import sys 
from time import sleep 
import random

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.06) 
def inco():
    jalan("Wrong Password ")     
def funca():
    p=input("password:")
    if p=="g":
        print("Right Password")
    else:
        inco()
        Help()
def funcb():
    p=input("password:")
    if p=="z":
        print("Right Password")
    else:
        inco()
        Help()            
def funcc():
    p=input("password:")
    if p=="p":
        print("Right Password")
    else:
        inco()
        Help()            
def funcd():
    p=input("password:")
    if p=="q":
        print("Right Password")
    else:
        inco()
        Help()            
def funce():
    p=input("password:")
    if p=="d":
        print("Right Password")
    else:
        inco()
        Help()            
def funcf():
    p=input("password:")
    if p=="f":
        print("Right Password")
    else:
        inco()
        Help()            
def funcg():
    p=input("password:")
    if p=="j":
        print("Right Password")
    else:
        inco()
        Help()            
def funch():
    p=input("password:")
    if p=="l":
        print("Right Password")
    else:
        inco()
        Help()            
def funci():
    p=input("password:")
    if p=="a":
        print("Right Password")
    else:
        inco()
        Help()           
def funcj():
    p=input("password:")
    if p=="k":
        print("Right Password")
    else:
        inco()
        Help()           
def funck():
    p=input("password:")
    if p=="o":
        print("Right Password")
    else:
        inco()
        Help()            
def funcl():
    p=input("password:")
    if p=="c":
        print("Right Password")
    else:
        inco()
        Help()            
def funcm():
    p=input("password:")
    if p=="x":
        print("Right Password")
    else:
        inco()
        Help()            
def funcn():
    p=input("password:")
    if p=="e":
        print("Right Password")
    else:
        inco()
        Help()            
def funco():
    p=input("password:")
    if p=="y":
        print("Right Password")
    else:
        inco()
        Help()            
def funcp():
    p=input("password:")
    if p=="u":
        print("Right Password")
    else:
        inco()
        Help()            
def funcq():
    p=input("password:")
    if p=="s":
        print("Right Password")
    else:
        inco()
        Help()           
def funcr():
    p=input("password:")
    if p=="r":
        print("Right Password")
    else:
        inco()
        Help()            
def funcs():
    p=input("password:")
    if p=="v":
        print("Right Password")
    else:
        inco()
        Help()            
def funct():
    p=input("password:")
    if p=="m":
        print("Right Password")
    else:
        inco()
        Help()            
def funcu():
    p=input("password:")
    if p=="h":
        print("Right Password")
    else:
        inco()
        Help()            
def funcv():
    p=input("password:")
    if p=="i":
        print("Right Password")
    else:
        inco()
        Help()            
def funcx():
    p=input("password:")
    if p=="g":
        print("Right Password")
    else:
        inco()
        Help()            
def funcx():
    p=input("password:")
    if p=="j":
        print("Right Password")
    else:
        inco()
        Help()           
def funcy():
    p=input("password:")
    if p=="b":
        print("Right Password")
    else:
        inco()
        Help()            
def funcz():
    p=input("password:")
    if p=="a":
        print("Right Password")
    else:
        inco()
        Help()

a="hunter"
b="killer"
c="expert"
d="vaumea"
e="abznx"
f="zjxn"
z="zjosn"
J="hacker"
k="ak"
m="sakisj"
s="jtha"
y="robot"
u="blackhat"

def xe_header():
    headers=[a,b,c,d,e,f,m,s,k,z,y,u]
    return random.choice(headers)

kl=xe_header()
 
def kam():
    os.system("clear")      
    fn=input("\x1b[1;93mFast Name : ")
    ln=input("\x1b[1;93mLast Name : ")       
    un=(fn+kl)
    if fn=='':
        jalan("\x1b[1;92mInput Fast Name or Last Name ")
        kam()
    print("\x1b[1;92mYour Username :", un)
    sleep(2)
    try :
        os.system("clear")
        jm=("\x1b[1;92mchecking loging info....")        
        os.system("clear") 
        with open("log.txt") as b:
            if ("arfatkhanisthebuliderofthistool") in b:
                os.system("bash extra.sh")
                exit()
    except :
        pass
    print('"\x1b[1;96m"""""""""Tool Login Manu""""""""""""""')
    
    print("\x1b[1;92myour username: ", fn+kl)
    print('"""""""""""""""""""""""""')
    l=1   
    for un1 in un:
        print("input Password No.",l,"Example: a ")        
        l+=1
        if l==9:
            sleep(2)
            
            with open("log.txt","w") as a:
                    f=("arfatkhanisthebuliderofthistool")
                    a.write(f)
                    a.close                                                           
                    print("")
                    print("Login succesful ")
                    sleep(2)        
                    break    
        if un1 =="a":
            funca()
        elif un1=="b":
            funcb()
        elif un1=="c":
            funcc()
        elif un1=="d":
            funcd()
        elif un1=="e":
            funce()
        elif un1=="f":
            funcf()
        elif un1=="g":
            funcg()
        elif un1=="h":
            funch()
        elif un1=="i":
            funci()
        elif un1=="j":
            funcj()
        elif un1=="k":
            funck()
        elif un1=="l":
            funcl()
        elif un1=="m":
            funcm()
        elif un1=="n":
            funcn()
        elif un1=="o":
            funco()
        elif un1=="p":
            funcp()
        elif un1=="q":
            funcq()
        elif un1=="r":
            funcr()
        elif un1=="s":
            funcs()
        elif un1=="t":
            funct()
        elif un1=="u":
            funcu()
        elif un1=="v":
            funcv()
        elif un1=="w":
            funcw()
        elif un1=="x":
            funcx()
        elif un1=="y":
            funcy()
        elif un1=="z":
            funcz()
        else:
            print("incorrect password")
            print("1.Back ")
            print("2.Help")
            j=int(input("localhost@root_# "))
            if j==1:
                kam()
            elif j==2:
                Help()
            else:
                Help()
    kam()    
def Help():
    os.system("clear")
    print("\x1b[1;93m")
    os.system("figlet FB Sploit")
    jalan("**********Welcome to FB-Sploit**********\n\n\n")
    jalan("\x1b[1;96mAuthor : Arfat_Khan")
    jalan("Website : https://www.technicalak-bd.blogspot.com\n")
    jalan('Facebook : https://www.facebook.com/akbullethz0.2\n')
    jalan("Github : https://github.com/arfatkhanbd\n")
    jalan("▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
    jalan('\n\n\x1b[1;92m1.Help')
    jalan('2.How To Use This Tool')
    jalan('3.Watch Video')
    jalan('4.My FB Account')
    jalan('5.My YouTube Channel')
    jalan('6.My Github Account ')
    jalan("7.My Website")
    jalan('8.Login In to This Tool')
    jalan('9.Create Account for this Tool')
    jalan('10.Exit\n\n\n')
    a=int(input("localhost@fb-slpoit_# "))
    if a==1:
        os.system("xdg-open https://technicalak-bd.blogspot.com/2020/04/FB-Sploit.html?m=1")
        Help()
    elif a==2:
        os.system("xdg-open https://technicalak-bd.blogspot.com/2020/04/FB-Sploit.html?m=1")
        Help()
    elif a==3:
        os.system("xdg-open https://www.youtube.com/playlist?list=PLmOKWLpvfbAcvS7DOlzASm35XBdaxlkR1")
        Help()
    elif a==4:
        os.system("xdg-open https://www.facebook.com/akbullethz0.2")
        Help()
    elif a==5:
        os.system("xdg-open https://www.youtube.com/channel/UC33rTm0ry9X2REsU9WsjgvA")
        Help()
    elif a==6:
        os.system("xdg-open https://www.github.com/arfatkhanbd")
        Help()
    elif a==7:
        os.system("xdg-open https://technicalak-bd.blogspot.com")
        Help()
    elif a==8:
        kam()
    elif a==9:
        os.system("xdg-open https://technicalak-bd.blogspot.com/2020/04/FB-Sploit.html?m=1")
        Help()
    elif a==10:
        exit()
Help()
        
