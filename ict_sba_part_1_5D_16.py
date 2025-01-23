import msvcrt
import os, time, sys
import calendar
from colorama import  Fore, Style #change colour






def main_menu():
    print()
    print("                                                       (1).Login")
    print()
    print("                                                       (2).Signup")
    print()
    print("                                                       (Esc).Exit")
    while True:
       if msvcrt.kbhit(): #Returns a nonzero value if a keypress is waiting to be read
            char = msvcrt.getch().decode('utf-8') 
            if char == "1":
                return Login()
            elif char == "2":
                return register()
            elif char == chr(27):
                os.system("cls")
                sys.exit(0)
#--------------------------------------------------------------------------------------------------------------------------------
def getData():
    f1 = open("username.txt", "r")
    f2 = open("password.txt", "r")
    u = f1.readlines()
    p = f2.readlines()
    for x in range(len(u)):
        u[x] = u[x].strip()
        p[x] = p[x].strip()
    f1.close()
    f2.close()
    return u , p
#-------------------------------------------------------------------------------------------------------------------------------
def register():
    username, password = getData()
    os.system("cls")
    length= False
    capital= False
    small= False
    num= False
    space= True
    while True:
        print("                                                           <Signup>")
        print()
        print()
        duplicate = False
        i = -1
        uname = input("                                                      Enter a username: ")
        while not duplicate and i < len(username) -1:
            i+= 1
            if uname == username[i]:
                duplicate = True
        if not duplicate:
            break
        else:
            os.system("cls")
            print("                                            The username has been used by others.")
            print()
            print("                                                  Please enter another one.")
            print()
    while not(length and capital and small and num and space):
        print()
        pas = str(input("                                                      Enter your password: "))
        if len(pas) >= 8:
            length= True
        for i in range(0,len(pas)):
            if pas[i] == " ":
                space = False
            if pas[i] >= "0" and pas[i] <= "9":
                num=True
            if pas[i] >="A" and pas[i] <= "Z":
                capital= True
            if pas[i] >="a" and pas[i] <= "z":
                small= True
        if length and capital and small and num and space:
            os.system("cls")
            print("                                                      Signup successful.")
            print()
            print("                                              Please restart the program to login.")
        else:
            os.system("cls")
            print("                                             Here is/are the problem(s) of your password: ")
            print()
            if not length:
                print("                                                      At least 8 characters!")
                print()
            if not capital:
                print("                                                      At least 1 capital letter!")
                print()
            if not small:
                print("                                                      At least 1 small letter!")
                print()
            if not num:
                print("                                                      At least 1 number!")
                print()
            if not space:
                print("                                                      Should contain no space!")
                print()
            length= False
            capital= False
            small= False
            num= False
            space= True
            print("")
    f1 = open("username.txt", "a")
    f2 = open("password.txt", "a")
    f1.write("\n" + uname)
    f2.write("\n" + pas)
    f1.close()
    f2.close()
    
#-----------------------------------------------------------------------------------------------------------------------------------
def Login():
    global username, password
    username, password = getData()
    os.system("cls")
    match = False
    while match == False:
        print("                                                           <Login>")
        print()
        i = 0
        uname = input("                                                         Username: ")
        print()
        pas = input("                                                         Password: ")
        while not match and i <= len(username) -1: 
            if username[i] == uname and password[i] == pas:
                match = True
            i += 1
        if match:
            os.system("cls")
            print("                                                Your login is successful.")
            print()
            print("                                                       Loading", end = "")
            for x in range(15):
                print(".", end = "",flush = True)
                time.sleep(0.1)
            return content()
        else:
            os.system("cls")
            print("                                                        Fail to login.")
            print()
        
#---------------------------------------------------------------------------------------------------------------------------    
def content():
     os.system("cls")
     print("                                                             <Menu>")
     print()
     print("                                                 (1).Schedule Assessments")
     print()
     print("                                                 (2).Display Assessments Scheduled")
     print()
     print("                                                 (3).Schedule Record")
     print()
     print("                                                 (Esc).Back")
     while True:
       if msvcrt.kbhit():
            char = msvcrt.getch().decode('utf-8') 
            if char == "1":
                return schedule()
            elif char == "2":
                return display()
            elif char == "3":
                return record()
            elif char == chr(27):
                os.system("cls")
                return title()
#-------------------------------------------------------------------------------------------------------------
def a():
    classlist = [[""] * 4 for i in range(6)]
    for x in range(6):
        for y in range(4):
            classlist[x][y] = str(x+1)+str(chr(65+y))
    print("%64s" % "C L A S S")
    for x in range(6):
        print("                　　　　　　　　　　　      　  "" | ", end = "")
        for y in range(4):
            print(classlist[x][y] + " | ", end = "")
        print("")
    print()
    return classlist
    
#---------------------------------------------------------------------------------------------------------------------------------------
def schedule():
    iput = False
    os.system("cls")
    while iput == False:
        classlist = a()
        class_ = input("                                                Which class(Big Letter)? ")
        class_exist = False
        for x in range(len(classlist)):
            for y in range(len(classlist[x])):
                if classlist[x][y] == class_:
                    class_exist = True
        if class_exist == False:
            os.system("cls")
            
            print("                                                      "+Fore.RED + "Wrong input!")
            print(Style.RESET_ALL)
        else:
            iput = True
            n = 1
            d = 1
            yy = 2025
            while True:
                os.system("cls")
                print(calendar.month(yy, n))
                print()
                print()
                print()
                print()
                print("(LEFT)A")
                print(d)
                print(n)
                while True:
                   if msvcrt.kbhit():
                        char = msvcrt.getch().decode('utf-8')
                        if char == "w" or char == "W":
                            n += 1
                        elif char == "s" or char == "S":
                            n = n - 1
                            
                        elif char == "a" or char == "A":
                            d -= 1
                        elif char == "d" or char == "D":
                            d += 1
                        break
                        
    ass = input("                                                     What you want to schedule? ")
    print()
    print()
    print()

    
    
    
        
    
#----------------------------------------------------------------------------------------------------------------------------------------
def display():
    os.system("cls")
    check = input("                                              Which class you want to check? ")
#----------------------------------------------------------------------------------------------------------------------------------------
def record():
    os.system("cls")
#----------------------------------------------------------------------------------------------------------------------------------------
def title():
    text = "Assessment Schedule System"
    padded_text = text.center(120)
    print(padded_text)
    main_menu()
title()