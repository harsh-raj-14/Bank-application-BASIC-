import json #json stored data
import random
import string
from pathlib import Path as p

class Bank:
    database='data.json'
    data=[]
    try:
        if p(database).exists():
            with open(database,'r') as f:
                data=json.loads(f.read())
        else:
            print("no such file exits")        
    except Exception as e:
        print(f"an exception occured as {e}")

    @staticmethod # means not be used by everyone
    def update():
        with open(Bank.database,'w') as f:
            f.write(json.dumps(Bank.data))

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as f:
            f.write(json.dumps(Bank.data))
        
    @classmethod
    def __accountGenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices("!@#$%^&*",k=1)
        id=alpha+num+spchar
        random.shuffle(id)
        return "".join(id)

    def create(self):
        info={
            "name":input("tell your name:-"),
            "age":int(input("tell your age:-")),
            "email":input("tell your email:-"),
            "pin":int(input("tell your 4 digit pin:-")),
            "accountNo":Bank.__accountGenerate(),
            "balance":0
        }
        if info['age']<18 or len(str(info['pin']))!=4:
            print("sorry you cannot create an account.")
        else:
            print("your account is successfully created.")
            for i in info:
                print(f"{i}:{info[i]}")
            print("please note down your account number")
        Bank.data.append(info)    
        Bank.update()   

    def depositeMoney(self):
        accNo=input("please tell your account number")
        pin=int(input("please tell your pin aswell"))
        userdata=[i for i in Bank.data if i['accountNo']==accNo and i['pin']==pin]
        if userdata==False:
            print("sorry no data found")
        else:
            amount=int(input("enter amount to be deposite"))
            if amount>10000:
                print("sorry,amount is to much.Please deposite below 10000") 
            else:
                print(userdata)
                userdata[0]['balance']+=amount   
                Bank.__update()
                print("amount is successfully deposited")
   
    def withdraw(self):
        accNo=input("please tell your account number")
        pin=int(input("please tell your pin aswell"))
        userdata=[i for i in Bank.data if i['accountNo']==accNo and i['pin']==pin]
        if userdata==False:
            print("sorry no data found")
        else:
            amount=int(input("enter amount to be deposite"))
            if amount>userdata[0]['balance']:
                print("sorry, you have an insufficient balance") 
            else:
                print(userdata)
                userdata[0]['balance']-=amount   
                Bank.__update()
                print("amount is successfully deposited")
    
    def details(self):
        accNo=input("please tell your account number")
        pin=int(input("please tell your pin aswell"))
        userdata=[i for i in Bank.data if i['accountNo']==accNo and i['pin']==pin]
        for i in userdata[0]:
            print(f"{i}:{userdata[0][i]}")

    def updatedetails(self):
        accNo=input("please tell your account number")
        pin=int(input("please tell your pin aswell"))
        userdata=[i for i in Bank.data if i['accountNo']==accNo and i['pin']==pin]
        if userdata==False:
            print("sorry no data found")   
        else:
            print("you cannot change your age,balance,account number") 
            print("fill the details for change or leave it empty if no change")
            newdata={
                    "name":input("tell your new name or press enter to skip :-"),
                    "email":input("tell your new email or press enter to skip :-"),
                    "pin":int(input("tell your 4 digit new pin or press enter to skip :-"))
                     }
            if newdata["name"]=="":
                newdata["name"]=userdata[0]['name']
            if newdata["email"]=="":
                newdata["email"]=userdata[0]['email']
            if newdata["pin"]=="":
                newdata["pin"]=userdata[0]['pin']
            
            newdata["age"]=userdata[0]['age']  
            newdata["balance"]=userdata[0]['balance']
            newdata["accountNo"]=userdata[0]['accountNo']
            
            for i in newdata:
                if userdata[0][i]==newdata[i]:continue
                else:userdata[0][i]=newdata[i]
            Bank.__update()
            print("details update successfully")
    
    def Delete(self):
        accNo=input("please tell your account number")
        pin=int(input("please tell your pin aswell"))
        userdata=[i for i in Bank.data if i['accountNo']==accNo and i['pin']==pin]
        if userdata==False:
            print("sorry no data found")   
        else:
            check=input("press y if you actually want to delete an account")
            if check=='n' or check=='N':
                pass
            else:
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.__update()
                print("acount delete successfully")

user=Bank()
print("press 1 for creating an account")
print("press 2 for depositing the money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting the account")

check= int(input("enter your response:-"))

if check==1:
    user.create()

if check==2:
    user.depositeMoney()

if check==3:
    user.withdraw()  

if check==4:
    user.details()

if check==5:
    user.updatedetails()

if check==6:
    user.Delete()