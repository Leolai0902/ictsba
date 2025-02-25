import msvcrt
def get_data():
    f = open("record.txt", "r")
    List = f.readlines()
    f.close()
    for i in range(len(List)):
        List[i] = List[i].strip("\n")
    for j in range(len(List)):
        List[j] = List[j].split("\t\t")
    return List
List = get_data()
x = msvcrt.getwch()
target = input("Enter something: ")
for i in range(len(List)):
    if List[i][int(x)-1] == target:
        for j in range(len(List[i])):
            print(List[i][j], end = "\t")
        print()