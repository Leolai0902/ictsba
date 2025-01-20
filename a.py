import os
name = input("Enter your name: ")
balance = int(input("Enter the blance: "))
os.system("cls")

seat = [[""] * 5 for i in range(5)]
for x in range(5):
    for y in range(5):
        seat[x][y] = str(y+1)
endbook = False
while not endbook:
    os.system("cls")
    print("User: " + name + "%20s" % "balance: $" + str(balance))
    print("%22s" % "S C R E E N")
    for x in range(5):
        print(chr(ord("A") + x) + " | ", end = "")
        for y in range(5):
            print(seat[x][y] + " | ", end = "")
        print("")
    row = input("Enter the row: ")
    rowno = ord(row) - ord("A")
    num = int(input("Enter the seat number: "))
    seat[rowno][num-1] = "X"
    balance = balance - 70
    if balance <= 0:
        print("Your balance is not enough!")
        a = input("Press <ENTER> to end.")
        endbook = True
os.system("cls")
print("Thank you for using our system.")