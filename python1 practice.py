//code
grade=input('enter grade')
age=int(input('enter age'))
exp=int(input('enter experience' ))
while grade=='W' or grade=='X' or grade=='Y' or grade=='Z':
    if grade=='W':
        BS=10000
        PI=700
        RP=BS+exp*PI
        print('running pay is ',RP)
        break
    elif grade=='X':
        BS=12900
        PI=910
        RP=BS+exp*PI
        print('running pay is' ,RP)
        break
    elif grade=='Y':
        BS=21700
        PI=1500
        RP=BS+exp*PI
        print('running pay is',RP)
        break
    elif grade=='Z':
        BS=32600
        PI=2800
        RP=BS+exp*PI
        print('running pay is',RP)
        break
        print("you entered invalid grade")
        grade=input('enter grade again')
       
print("---------")
print("Allowance")
HRA=RP*45/100
print("HRA is :",HRA)
SSB=BS*30/100
print("SSB is :",SSB)
if grade=='W' and age>40:
    ARA=3000
    print('ARA is ',ARA)
else:
    ARA=1500
    print('ARA is ', ARA)
    
GP=RP+HRA+SSB+ARA
print('GP IS ',GP)
charity= GP%100
gp=GP-charity


print("gp is ",gp)
print('-------')
print("DEDUCTION")

AI=gp*12
print('annual income is' ,AI)
if AI>0 and AI<=400000:
    print('IT is 0')
elif AI > 400001 and AI <=650000:
    IT=gp*2.5/100
    print('IT is ', IT)
elif AI > 650001 and AI <=1000000:
    IT=gp*4.47/100
    print('IT is',IT)
elif AI > 1000001 and AI <=1500000:
    IT=gp*7/100
    print('IT is', IT)
elif AI > 1500001 :
    IT=gp*11.5/100
    print('IT is ', IT)
MGP= gp/12
print('Monthly gross pay ', MGP)
GPF= MGP*10/100
print(' General provident fund is ', GPF)
Td=IT+GPF
print('total deduction is ',Td)
Np=gp-Td
print('Net pay is ',Np)





























     

 
