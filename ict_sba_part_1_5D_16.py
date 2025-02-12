import msvcrt
import os, time, sys
import calendar
import maskpass
from colorama import  Fore, Style #change colour
from datetime import datetime, date





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def getData_login():
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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def register():
    username, password = getData_login()
    os.system("cls")
    length= False
    capital= False
    small= False
    num= False
    space= True
    while True:
        print("                                                      <Signup>")
        print()
        duplicate = False
        empty = False
        i = -1
        uname = input("                                                  Enter a username: ")
        while not duplicate and i < len(username) -1:
            i+= 1
            if uname == username[i]:
                duplicate = True
            elif uname == "":
                empty = True
        if not duplicate and not empty:
            break
        elif empty:
            os.system("cls")
            print("                                           The username cannot be  empty!")
            print()
        else:
            os.system("cls")
            print("                                        The username has been used by others.")
            print()
            print("                                              Please enter another one.")
            print()
    while not(length and capital and small and num and space):
        print()
        pas = str(input("                                                  Enter your password: "))
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
            f1 = open("username.txt", "a")
            f2 = open("password.txt", "a")
            f1.write("\n" + uname)
            f2.write("\n" + pas)
            f1.close()
            f2.close()
            os.system("cls")
            print("                                                      Signup successful.")
            print()
            print("                                                 Please press <ENTER> to login.")
            while True:
                if msvcrt.kbhit():
                    char = msvcrt.getch().decode('utf-8') 
                    if char == chr(13):
                        return title()
        else:
            os.system("cls")
            print("                                          Here is/are the problem(s) of your password: ")
            print()
            if not length:
                print("                                                   At least 8 characters!")
                print()
            if not capital:
                print("                                                   At least 1 capital letter!")
                print()
            if not small:
                print("                                                   At least 1 small letter!")
                print()
            if not num:
                print("                                                   At least 1 number!")
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
    
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Login():
    global username, password, uname
    username, password = getData_login()
    os.system("cls")
    all_match = False
    while all_match == False:
        print("                                                          <Login>")
        print()
        i = 0
        uname = input("                                                         Username: ")
        print()
        pas = maskpass.askpass(prompt="                                                         Password: ", mask="*")
        while not all_match and i <= len(username) -1:
            u_match = False
            p_match = False
            all_wrong = False
            ad_match = False
            if uname == "Admin" and pas == "1":
                ad_match = True
            elif username[i] == uname and password[i] == pas:
                all_match = True
            elif username[i] == uname and password[i] != pas:
                u_match = True
            elif username[i] != uname and password[i] == pas:
                p_match = True
            else:
                all_wrong =True
            i += 1
        if ad_match:
            os.system("cls")
            print("                                                Your login is successful.")
            print()
            print("                                                       Loading", end = "")
            for x in range(15):
                print(".", end = "",flush = True)
                time.sleep(0.1)
            return admin_content()
        elif all_match:
            os.system("cls")
            print("                                                Your login is successful.")
            print()
            print("                                                       Loading", end = "")
            for x in range(15):
                print(".", end = "",flush = True)
                time.sleep(0.1)
            return content()
        elif u_match:
            os.system("cls")
            print("                                                      Wrong password!")
            print()
        elif p_match:
            os.system("cls")
            print("                                                      Wrong username!")
            print()
        elif all_wrong:
            os.system("cls")
            print("                                                       Fail to login!")
            print()
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
def content():
     os.system("cls")
     print("                                                           <Menu>")
     print()
     print("                                                 (1).Schedule Assessments")
     print()
     print("                                                 (2).Display Assessments Scheduled")
     print()
     print("                                                 (3).Schedule Record")
     print()
     print("                                                 (Esc).Logout")
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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def admin_content():
    os.system("cls")
    print("                                                         <Admin Menu>")
    print()
    print("                                               (1).Delete Assessments Scheduled")
    print()
    print("                                               (2).")
    print()
    print("                                                (Esc).Logout")
    while True:
       if msvcrt.kbhit():
            char = msvcrt.getch().decode('utf-8') 
            if char == "1":
                return delete()
            elif char == chr(27):
                os.system("cls")
                return title()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def a():
    classlist = [[""] * 4 for i in range(6)]
    for x in range(6):
        for y in range(4):
            classlist[x][y] = str(x+1)+str(chr(65+y))
    print("%68s" % "C L A S S")
    for x in range(6):
        print("                　　　　　　　　 　　　         　  "" | ", end = "")
        for y in range(4):
            print(classlist[x][y] + " | ", end = "")
        print("")
    print()
    return classlist
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def schedule():
    global m, d, class_
    iput = False
    os.system("cls")
    while iput == False:
        classlist = a()
        class_ = input("                                                          Which class? ")
        class_ = class_.upper()
        class_exist = False
        for x in range(len(classlist)):
            for y in range(len(classlist[x])):
                if classlist[x][y] == class_:
                    class_exist = True
        if class_exist == False:
            os.system("cls")
            
            print("                                                          "+Fore.RED + "Wrong input!")
            print(Style.RESET_ALL)
        else:
            iput = True
            m = 1
            d = 1
            yyyy = 2025
            while True:
                os.system("cls")
                print(calendar.month(yyyy, m))
                print()
                print()
                print()
                print("                                                         (NEXT MONTH)W")
                print()
                print("                                       (PREVIOUS DATE)A                 (NEXT DATE)D")
                print()
                print("                                                       (PREVIOUS MONTH)S")
                print("Month: "+str(m))
                print("Date: "+str(d))
                print("Press <ENTER> to comfirm.")
                while True:
                   if msvcrt.kbhit():
                        char = msvcrt.getch().decode('utf-8')
                        if (char == "w" or char == "W") and m!= 12:
                            m += 1
                            d = 1
                        elif (char == "s" or char == "S") and m!= 1:
                            m = m - 1
                            d = 1
                        elif (char == "a" or char == "A") and d!= 1:
                            d -= 1
                        elif (char == "d" or char == "D") and (((m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and d != 31) or ((m == 2) and d != 28) or (m == 4 or m == 6 or m == 9 or m == 11) and d != 30 ):
                            d += 1
                        break
                if char == chr(13):
                    return subject()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def subject_list():
    global q
    os.system("cls")
    f3 = open("subject.txt", "r")
    q = f3.readlines()
    for p in range(len(q)):
        q[p] = q[p].strip()
    f3.close()
    for j in range(4):
        print("           　　　　　　　　 　　　         　  ", end = "")
        for k in range(4):
            print("\t" + q[j*4 + k], end = " ")
        print()
    print()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def subject():
    global assessment
    OK = False
    subject_list()
    while OK == False:
        assessment = input("           　　　　  　　　　 　   　　            　   What subject? ")
        assessment = assessment.upper()
        found_result = search(assessment)
        if  found_result:
            OK = True
            print("           　　　　  　　　　 　   　　            　   Loading", end = "")
            for x in range(15):
                print(".", end = "",flush = True)
                time.sleep(0.1)
            os.system("cls")
            txt_record()
            print("           　　　　  　　　　 　   　　          Assessment scheduled.")
            print()
            print("           　　　　  　　　　 　   　　          Press <ENTER> to back to menu.")
            while True:
                if msvcrt.kbhit():
                        char = msvcrt.getch().decode('utf-8')
                        if char == chr(13):
                            return content()
        else:
            print("           　　　　  　　　　 　   　　            　   Loading", end = "")
            for x in range(15):
                print(".", end = "",flush = True)
                time.sleep(0.1)
            print()
            os.system("cls")
            subject_list()
            print("           　　　　  　　　　 　   　　            　   "+Fore.RED + "Wrong input!")
            print(Style.RESET_ALL)
            print("           　　　　  　　　　 　   　　            　   Input agian.")
            print()
    return q
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def txt_record():
    global class_, assessment, m, d, uname
    time = datetime.now().time().strftime("%X")
    date = datetime.now().date()
    f4 = open("record.txt","a")
    f4.write("\n" + str(date) + " " + str(time) + " " + str(class_) + " " + str(m) +"-"+str(d) + " " + str(assessment) + " " + str(uname))
    f4.close()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def search(ass):
    global q
    x = 0
    found = False
    while not (found) and x < len(q):
        if ass == q[x]:
            found = True
        x += 1
    return found   
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def display():
    global g, check
    os.system("cls")
    iput = False
    os.system("cls")
    while iput == False:
        classlist = a()
        check = input("                                              Which class you want to check? ")
        check = check.upper()
        class_exist = False
        for x in range(len(classlist)):
            for y in range(len(classlist[x])):
                if classlist[x][y] == check:
                    class_exist = True
        if class_exist == False:
            os.system("cls") 
            print("                                                      "+Fore.RED + "Wrong input!" + Style.RESET_ALL)
        else:
            iput = True
            f4 = open("record.txt", "r")
            g = f4.readlines()
            for y in range(len(g)):
                g[y] = g[y].replace("\n", "")
            f4.close()
            bubble_sort(g)
            linear_search(check , g)
    print()
    print()
    print()
    print("                                                      <ESC>Back To Menu")
    while True:
        if msvcrt.kbhit():
            try:
                char = msvcrt.getch().decode('utf-8')
                if char == chr(27):
                    return content()
            except UnicodeDecodeError:
                pass
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j +1]:
                swap(j , j + 1, arr)
                
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def swap(a, b, arr2):
    temp = arr2[a]
    arr2[a] = arr2[b]
    arr2[b] = temp
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def linear_search(c,l):
    x = 0
    found = False
    while x < len(l):
        index = l[x].find(c)
        if index != -1:
            found = True
            print(l[x])
        x = x + 1
    if found == False:
        print("No result!")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def record():
    global g
    os.system("cls")
    f4 = open("record.txt", "r")
    g = f4.readlines()
    for x in range(len(g)):
        g[x] = g[x].strip()
    f4.close()
    
    print("                                                          RECORD")
    for y in range(len(g)):
        print ("                                              " + g[y])
    print()
    print()
    print()
    print("                                                      <ESC>Back To Menu")
    while True:
        if msvcrt.kbhit():
            try:
                char = msvcrt.getch().decode('utf-8')
                if char == chr(27):
                    return content()
            except UnicodeDecodeError:
                pass
                
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def delete():
    print()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def title():
    os.system("cls")
    text = "Assessment Schedule System"
    padded_text = text.center(122)
    print(padded_text)
    main_menu()
title()
