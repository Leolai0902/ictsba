import msvcrt
import os, time, sys
import calendar
from colorama import  Fore, Style #change colour
from datetime import datetime, date





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##############
# Main Menu  #
##############
def main_menu():
    print()
    print("                                                       (1).Login")
    print()
    print("                                                       (2).Signup")
    print()
    print("                                                       (Esc).Exit")
    while True:
       if msvcrt.kbhit(): #Returns a nonzero value if a keypress is waiting to be read
            char = msvcrt.getwch()
            if char == "1":
                return Login()
            elif char == "2":
                return register()
            elif char == chr(27):
                os.system("cls")
                sys.exit(0)
##############
# Main Menu  #
##############
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
        uname = input("                                                  Enter a username: ").strip()
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
                    char = msvcrt.getwch() 
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
                print("                                                   Should not contain space!")
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
        u_match = False
        p_match = False
        all_wrong = False
        ad_match = False
        i = 0
        uname = input("                                                         Username: ")
        print()
        pas = input("                                                         Password: ")
        while not u_match and not all_match and not p_match and not ad_match and i <= len(username) -1:
            u_match = False
            p_match = False
            all_wrong = False
            ad_match = False
            if uname == "Admin" and username[i] == "Admin" and password[i] == pas:
                ad_match = True
            elif username[i] == uname and password[i] == pas:
                all_match = True
            elif username[i] == uname and password[i] != pas:
                u_match = True
            elif username[i] != uname and password[i] == pas:
                p_match = True
            else:
                all_wrong = True
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
        else:
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
            char = msvcrt.getwch() 
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
    print("                                               (1).Schedule Assessments")
    print()
    print("                                               (2).Delete Assessments Scheduled")
    print()
    print("                                               (3).Delete Account")
    print()
    print("                                               (4).Change Password")
    print()
    print("                                               (Esc).Logout")
    while True:
       if msvcrt.kbhit():
            char = msvcrt.getwch() 
            if char == "1":
                return schedule()
            elif char == "2":
                return delete()
            elif char == "3":
                return del_ac()
            elif char == "4":
                return change_pas()
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
        print("                                                      | ", end = "")
        for y in range(4):
            print(classlist[x][y] + " | ", end = "")
        print("")
    print()
    return classlist
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def schedule():
    global m, d, class_ , n
    List = getdisplay_data()
    iput = False
    os.system("cls")
    while iput == False:
        classlist = a()
        class_ = input("                                                          Which class? ").strip()
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
                print("Press <ENTER> to confirm.")
                while True:
                   if msvcrt.kbhit():
                        char = msvcrt.getwch()
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
                    f4 = open("record.txt", "r")
                    g = f4.readlines()
                    for y in range(len(g)):
                         g[y] = g[y].replace("\n", "")
                    f4.close()
                    bubble_sort(List)
                    linear_search2(str(m) +"-" + str(d),class_, List)
                    os.system("cls") 
                    return alarm()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def alarm():
    global n, uname
    if n >= 3 and n < 5:
        print("                        "+Fore.YELLOW +"There are " + str(n) + " assessmants on that day.Do you still want to schedule assessment? " + Style.RESET_ALL)
        print()
        print("(Yes)Y                 (NO)N")
        while True:
            if msvcrt.kbhit():
                char = msvcrt.getwch()
                if (char == "Y" or char == "y"):
                    return subject()
                elif (char == "N" or char == "n"):
                    return content()
    elif n >= 5:
        print("                         "+Fore.RED +"There are too many assessments scheduled on that day.You cannot schedule!"+ Style.RESET_ALL)
        print()
        print("                                                 Press <ENTER> to back to menu.")
        while True:
            if msvcrt.kbhit():
                char = msvcrt.getwch()
                if char == chr(13):
                    if uname != "Admin":
                        return content()
                    else:
                        return admin_content()
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
        print("                                             ", end = "")
        for k in range(4):
            print("\t" + q[j*4 + k], end = " ")
        print()
    print()
#--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def subject():
    global assessment, work, uname
    List = getdisplay_data()
    OK = False
    subject_list()
    while OK == False:
        assessment = input("                                                      What subject? ").strip()
        assessment = assessment.upper()
        found_result = search(assessment)
        if  found_result:
            print("                                                      What assessment? ")
            print()
            print("                                                            1.Dictation")
            print()
            print("                                                            2.Quiz")
            print()
            print("                                                            3.Test")
            print()
            print("                                                            4.Exam")
            choose = False
            while choose == False:
                if msvcrt.kbhit():
                        char = msvcrt.getwch()
                        if char == "1":
                            print()
                            work = "Dictation"
                            choose = True
                        elif char == "2":
                            print()
                            work = "Quiz"
                            choose = True
                        elif char == "3":
                            print()
                            work = "Test"
                            choose = True
                        elif char == "4":
                            print()
                            work = "Exam"
                            choose = True
            OK = True
            print("                                                        Loading", end = "")
            for x in range(15):
                print(".", end = "",flush = True)
                time.sleep(0.1)
            os.system("cls")
            txt_record(List)
            print("                                                 Assessment scheduled.")
            print()
            print("                                                 Press <ENTER> to back to menu.")
            while True:
                if msvcrt.kbhit():
                        char = msvcrt.getwch()
                        if char == chr(13) and uname != "Admin":
                            return content()
                        else:
                            return admin_content()
        else:
            print("                                                        Loading", end = "")
            for x in range(15):
                print(".", end = "",flush = True)
                time.sleep(0.1)
            print()
            os.system("cls")
            subject_list()
            print("                                                        "+Fore.RED + "Wrong input!")
            print(Style.RESET_ALL)
            print("                                                        Input agian.")
            print()
    return q
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def txt_record(l):
    global class_, assessment, m, d, uname, work
    time = datetime.now().time().strftime("%X")
    date = datetime.now().date()
    done = [str(date), str(time), str(class_),  (str(m)+ "-"+str(d)), str(assessment), str(work), str(uname)]
    l = l + [done]
    f4 = open("record.txt","w")
    for i in range(len(l)):
        if i < len(l):
            f4.write(l[i][0] + "\t" + l[i][1] + "\t" + l[i][2] + "\t" + l[i][3] + "\t" + l[i][4] + "\t" + l[i][5] + "\t" + l[i][6] + "\n")
        else:
            f4.write(l[i][0] + "\t" + l[i][1] + "\t" + l[i][2] + "\t" + l[i][3] + "\t" + l[i][4] + "\t" + l[i][5] + "\t" + l[i][6])
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
def getdisplay_data():
    f = open("record.txt", "r")
    List = f.readlines()
    f.close()
    for i in range(len(List)):
        List[i] = List[i].strip("\n")
    for j in range(len(List)):
        List[j] = List[j].split("\t")
    return List
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def display():
    global check, var
    os.system("cls")
    iput = False
    os.system("cls")
    while iput == False:
        print("                                              What you want to check? ")
        print()
        print("                                                  1.Class")
        print()
        print("                                                  2.Assessment Date")
        print()
        print("                                                  3.Subject")
        print()
        print("                                                  4.Assessment")
        print()
        print("                                                  5.Teacher")
        choosen = False
        while choosen == False:
            if msvcrt.kbhit():
                        char = msvcrt.getwch()
                        if char == "4":
                            choosen = True
                            os.system("cls")
                            print("                                                  1.Dictation")
                            print("                                                  2.Quiz")
                            print("                                                  3.Test")
                            print("                                                  4.Exam")
                            while True:
                                if msvcrt.kbhit():
                                    char = msvcrt.getwch()
                                    if char == "1":
                                        check = "Dictation"
                                    elif char == "2":
                                        check = "Quiz"
                                    elif char == "3":
                                        check = "Test"
                                    elif char == "4":
                                        check = "Exam"
                                    var = 5
                                    return result(var, check)

                        elif char == "1":
                            choosen = True
                            classlist = a()
                            os.system("cls")
                            iput = False
                            while iput == False:
                                check = input("                                                 Which class? ").strip()
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
                                    var = 2
                                    return result(var, check)

                        elif char == "2":
                            choosen = True
                            os.system("cls")
                            print("                                                  1.Specific Date")
                            while True:
                                if msvcrt.kbhit():
                                    char = msvcrt.getwch()
                                    if char == "1":
                                        m = 1
                                        d = 1
                                        while True:
                                            os.system("cls")
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
                                            print("Press <ENTER> to confirm.")
                                            while True:
                                                if msvcrt.kbhit():
                                                    char = msvcrt.getwch()
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
                                                check = str(m) +"-" + str(d)
                                                var = 3
                                                return result(var, check)
                            
                            
                        elif char == "3":
                            choosen = True
                            subject_list()
                            os.system("cls")
                            iput = False
                            while iput == False:
                                check = input("                                              Which subject? ").strip()
                                check = check.upper()
                                found_result = search(check)
                                if not found_result:
                                    os.system("cls") 
                                    print("                                                      "+Fore.RED + "Wrong input!" + Style.RESET_ALL)
                                else:
                                    iput = True
                                    var = 4
                                    return result(var, check)
                                               
                            
                        elif char == "5":
                            choosen = True
                            f = open("username.txt", "r")
                            username = f.readlines()
                            for x in range(len(username)):
                                username[x] = username[x].strip()
                            f.close()
                            os.system("cls")
                            exist = False
                            while exist == False:
                                i = 0
                                check = input("                                                Which teacher(Username)? ").strip()
                                while i <= len(username) -1:
                                    if username[i] == check:
                                        exist = True
                                        var = 6
                                        return result(var, check)
                                    else:
                                        os.system("cls") 
                                        print("                                                      "+Fore.RED + "Not exist!" + Style.RESET_ALL)
                                    i += 1
                            
                            
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def result(var, check):
    os.system("cls")
    print("Result:")
    List = getdisplay_data()
    print("                       SCHEDULE DATE          CLASS       ASSESSMENT DATE          SUBJECT            TEACHER       ")
    bubble_sort(List)
    linear_search(check , List, var)
    print()
    print()
    print()
    print("                                                      <ESC>Back To Menu")
    while True:
        if msvcrt.kbhit():
            char = msvcrt.getwch()
            if char == chr(27):
                return content()
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
def linear_search(c,l, v):
    global n
    found = False
    for i in range(len(l)):
        if l[i][v] == c:
            print("                    " + g[y][0] + " " + g[y][1] + "\t\t" + g[y][2] + "\t\t" + g[y][3] + "\t\t" + g[y][4] + " " + g[y][5] + "\t\t" + g[y][6])
            found = True
    if found == False:
        os.system("cls")
        print("Result: ")
        print("                                                      "+Fore.RED + "No result!" + Style.RESET_ALL)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
def linear_search2(c,class_,l):
    global n
    n = 0
    found = False
    for i in range(len(l)):
        if l[i][2] == c and l[i][1] == class_:
            n += 1
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def record():
    global g
    os.system("cls")
    f4 = open("record.txt", "r")
    g = f4.readlines()
    for x in range(len(g)):
        g[x] = g[x].strip()
    for k in range(len(g)):
        g[k] = g[k].split("\t")
    f4.close()
    print("                                                             <RECORD>")
    print()
    print("                       SCHEDULE DATE          CLASS       ASSESSMENT DATE          SUBJECT            TEACHER       ")
    print()
    for y in range(len(g)):
        print("                    " + g[y][0] + " " + g[y][1] + "\t\t" + g[y][2] + "\t\t" + g[y][3] + "\t\t" + g[y][4] + " " + g[y][5] + "\t\t" + g[y][6])
        print("                    ------------------------------------------------------------------------------------------     ")
    print()
    print()
    print()
    print("                                                      <ESC>Back To Menu")
    while True:
        if msvcrt.kbhit():
            char = msvcrt.getwch()
            if char == chr(27):
                return content()


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def delete():
    global g
    os.system("cls")
    f4 = open("record.txt", "r")
    g = f4.readlines()
    for x in range(len(g)):
        g[x] = g[x].strip()
    for k in range(len(g)):
        g[k] = g[k].split("\t")
    f4.close()
    n = 0
    os.system("cls")
    print("                                                            Delete")
    print()
    print("                       SCHEDULE DATE          CLASS       ASSESSMENT DATE          SUBJECT            TEACHER       ")
    print()
    for y in range(len(g)):
        n += 1
        print("                    " + str(n) + "."  + g[y][0] + " " + g[y][1] + "\t" + g[y][2] + "\t\t" + g[y][3] + "\t\t" + g[y][4] + " " + g[y][5] + "\t\t" + g[y][6])
        print("                    --------------------------------------------------------------------------------     ")
    print()
    correct = False
    if n == 0:
        os.system("cls")
        print("                                            No assessment you can delete.")
        print()
        print()
        print()
        print("                                                   <ESC>Back To Menu")
        while True:
            if msvcrt.kbhit():
                char = msvcrt.getwch()
                if char == chr(27):
                    return admin_content()
    else:
        while correct == False:
            num = input("                                             Which record do you want to delete? ")
            if num.isnumeric() == True:
                if num < str(1):
                    print("                                                        "+Fore.RED +"Wrong input!" + Style.RESET_ALL)
                elif num > str(len(g)):
                    print("                                                     "+Fore.RED +"Index out of range!" + Style.RESET_ALL)
                else:
                    correct = True
                    del g[n -1]
                    f = open("record.txt", "w")
                    for y in range(len(g)):
                        f.write(g[y] + "\n")
                    f.close()
                    os.system("cls")
                    n = 0
                    print("                                                   Record deleted!")
                    print()
                    print()
                    print()
                    print("                                                   <ESC>Back To Menu")
                    while True:
                        if msvcrt.kbhit():
                            char = msvcrt.getwch()
                            if char == chr(27):
                                return admin_content()
            elif num.isnumeric() == False:
                print("                                                        "+Fore.RED +"Wrong input!" + Style.RESET_ALL)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def del_ac():
    global num
    username, password = getData_login()
    os.system("cls")
    all_match = False
    while all_match == False:
        print("                                                        <Delete Account>")
        print()
        u_match = False
        p_match = False
        wrong = False
        admin_found = False
        i = 0
        while admin_found == False:
            uname = input("                                                    Enter account username: ")
            if uname == "Admin":
                print("                                                    " +Fore.RED +"Cannot delete admin account!" + Style.RESET_ALL)
            else:
                admin_found = True
        print()
        pas = input("                                                    Enter account password: ")
        while not u_match and not p_match and not all_match and i <= len(username) - 1:
            u_match = False
            p_match = False
            wrong = False
            if username[i] == uname and password[i] == pas:
                all_match = True
                num = i
            else:
                wrong = True
            i += 1
        if all_match:
            os.system("cls")
            return del_main()
        elif wrong:
            os.system("cls")
            print("                                                    " +Fore.RED +"Wrong password or username!" + Style.RESET_ALL)
            print()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def del_main():
    u_del = ""
    pas_del = ""
    global num
    username, password = getData_login()
    print("                                   Are you sure you want to delete this account? ")
    print()
    print()
    print()
    print("                                         (YES)Y                        (NO)N")
    while True:
        if msvcrt.kbhit():
            char = msvcrt.getwch()
            if char == "Y" or char == "y":
                del username[num]
                del password[num]
                os.system("cls")
                f1 = open("username.txt", "w")
                f2 = open("password.txt", "w")
                for x in range(len(username)):
                    f1.write(username[x] + "\n")
                for y in range(len(password)):
                    f2.write(password[y] + "\n")
                f1.close()
                f2.close()
                print("                                    " + Fore.YELLOW + "Account deleted!" + Style.RESET_ALL)
                print()
                print()
                print()
                print("                                                   <ESC>Back To Menu")
                while True:
                    if msvcrt.kbhit():
                        char = msvcrt.getwch()
                        if char == chr(27):
                            return admin_content()
            elif char == "N" or char == "n":
                os.system("cls")
                print("Delete account cancelled")
                print()
                print()
                print()
                print("                                                   <ESC>Back To Menu")
                while True:
                    if msvcrt.kbhit():
                        char = msvcrt.getwch()
                        if char == char(27):
                            return admin_content()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def change_pas():
    username, password = getData_login()
    length= False
    capital= False
    small= False
    num= False
    space = True
    same = False
    same_pas = False
    os.system("cls")
    pas_input = False
    while pas_input == False:
        old_pas = input("                                                Enter the original password: ")
        if old_pas == password[0]:
            pas_input = True
            os.system("cls")
            while not(length and capital and small and num and space and same):
                n_pas1 = input("                                                Enter new password: ")
                if len(n_pas1) >= 8:
                    length= True
                for i in range(0,len(n_pas1)):
                    if n_pas1 != old_pas:
                        same = True
                    if n_pas1[i] == " ":
                        space = False
                    if n_pas1[i] >= "0" and n_pas1[i] <= "9":
                        num=True
                    if n_pas1[i] >="A" and n_pas1[i] <= "Z":
                        capital= True
                    if n_pas1[i] >="a" and n_pas1[i] <= "z":
                        small= True
                if length and capital and small and num and space and same:
                    while same_pas == False:
                        n_pas2 = input("                                                Enter new password again: ")
                        if n_pas2 == n_pas1:
                            same_pas = True
                            password[0] = n_pas1
                            n_pas1 += "\n"
                            f = open("password.txt", "w")
                            for x in range(len(password)):
                                if x < len(password) -1:
                                    f.write(password[x] + "\n")
                                else:
                                    f.write(password[x] + "\n")
                            f.close()
                            os.system("cls")
                            print("                                                   " + Fore.BLUE + "Password changed!" + Style.RESET_ALL)
                            print()
                            print()
                            print()
                            print("                                               Please press <ENTER> to login.")
                            while True:
                                if msvcrt.kbhit():
                                    char = msvcrt.getwch()
                                    if char == chr(13):
                                        return title()
                        else:
                            os.system("cls")
                            print("                                                        "+Fore.RED +"Wrong input!" + Style.RESET_ALL)
                        
                else:
                    os.system("cls")
                    print("                                          Here is/are the problem(s) of your password: ")
                    print()
                    if not same:
                        print("                                                   Cannot same as the original one!")
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
                        print("                                                   Should not contain space!")
                        print()
                    length= False
                    capital= False
                    small= False
                    num= False
                    space= True
                    same = False
                    print("")
            
        else:
            os.system("cls")
            print("                                                        "+Fore.RED +"Wrong input!" + Style.RESET_ALL)
    
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###############
#    Title    #
###############
def title():
    os.system("cls")
    print("          _                                   _     ___     _           _      _       ___         _             ")
    print("         /_\   ______ ___ _______ __  ___ _ _| |_  / __| __| |_  ___ __| |_  _| |___  / __|_  _ __| |_ ___ _ __  ")
    print("        / _ \ (_-<_-</ -_|_-<_-< '  \/ -_) ' \  _| \__ \/ _| ' \/ -_) _` | || | / -_) \__ \ || (_-<  _/ -_) '  \ ")
    print("       /_/ \_\/__/__/\___/__/__/_|_|_\___|_||_\__| |___/\__|_||_\___\__,_|\_,_|_\___| |___/\_, /__/\__\___|_|_|_|")
    print("                                                                                           |__/                  ")
    main_menu()
title()
###############
#    Title    #
###############

