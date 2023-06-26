import os.path
import random
def signup():
    username=input("Please enter UserName: ")
    if check_member(username)==True:
        print("This Account already exists")
    else:
        password=input("Please enter Password: ")
        account=username+' '+password
        File_exist=os.path.exists("member.txt")# check mikonad ke aya file ijad shode ast ya kheir
        if File_exist==False:
            with open("member.txt",'a+') as file:
                file.writelines(account)
                file.write('\n')
                file.close
                print("Account creation was successful!!!")
        else:
            with open("member.txt", "a+") as file:
                file.writelines(account)
                file.write("\n")
                file.close()
                print("Account creation was successful!!!")                   
def check_member(acc):
     with open("member.txt", 'r') as file:
        content = file.read()
        if content.find(acc)==-1:
           return False
        else:
           return True       
def login():
    username=input("Please enter UserName: ")
    password=input("Please enter Password: ")
    account=username+' '+password
    if check_member(account)==True:
        print("Welcome %s To The Game"%username)
        return username
    else:
        print("this account does Not exist!!!")
        return False
def Play(user):
    score_user=0
    score_computer=0
    while(score_computer<2 and score_user<2):
        print(" In which hand is the target: ")
        print("1-Right")
        print("2-Left")
        player1=int(input("Select :" ))
        player2=random.randint(1, 2)
        if player1==player2:
            score_user+=1
            print('You Win')
        else:
            score_computer+=1    
            print('Computer Win')

    if score_computer<score_user:
        print("User: %s win with result %i - %i"%(user,score_user,score_computer))
    elif score_computer>score_user:
        print("Computer win with result %i - %i"%(score_computer,score_user))

while True:
    print("To start the game please LOGIN or SIGNUP")
    print("1.LOGIN")
    print("2-SIGNUP")
    print("3-EXIT")

    s=int(input("SELECT an OPTION: "))
    if s==1:
        log=login()
        if log!=False:
            Play(log)
    if s==2:
        signup()
    if s==3:
        break                
