from module import *
while True:
    print("Funktsioonid".center(50,"+"))
    v=input("arithmetic- A")
    if v.upper()=="A":
        a=float(input("Arv 1:"))
        b=float(input("Arv 2:"))
        c=input("Tehe:")
        rezult=arithmetic(a,b,c)
        print(rezult)
    elif v.upper()=="B":
        year=int(input("Sisesta aasta:"))
        result=is_year_leap(year)
        print(result)
    elif v.upper()=="C":
        kv=int(input("Sisestage ruudu külg: "))
        result=square(kv)
        print(result)