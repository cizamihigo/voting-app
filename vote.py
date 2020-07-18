def votesearch(values,x ):
    idx0 = 0
    idxn = (len(values) - 1)

    while idx0 <= idxn and x >= values[idx0] and x <= values[idxn]:
        mid = idx0 +\
          int(((float(idxn - idx0)/( values[idxn] - values[idx0]))
               * ( x - values[idx0])))

# Compare the value at mid point with search value
        if values[mid] == x:
            return "Found "+str(x)+" at index "+str(mid)

        if values[mid] < x:
            idx0 = mid + 1
    return "Searched element not in the list"
def ident_voters():
    print("welcome voter. to vote is your right and your duty")
    print("*"*51)
    fvote=open(r"id/voterid.txt","a+")
    Vname=input("Enter voter name: ")
    Vbd=input("Enter birth day (23/03/1890: )")
    Vbirthplace=input("Enter birth place(BUKAVU): ")
    Vaddress=input("Enter your current address: ")
    Vorigin=input("Enter voter Origin: ")
    VFname=input("Enter father's name: ")
    VMname=input("Enter Mother's name: ")
    NN=input("Enter your NN number: ")
    ddd=str(fvote)
    votesearch(ddd, Vname)
    fvote.write(Vname+","+Vbd+","+Vbirthplace+","+Vaddress+","+Vorigin+","+VFname+","+VMname+","+NN+"\n")
    Fvopen=fvote.read()

def registered():
    try:
        fv=open(r"id/voterid.txt")
        fvs=fv.read()
        print(fvs)
        fv.close()
    except():
        print("an error occured. we are unable to register this voter!")



print("\t\t\t\t\t\t\tREPUBLIC OF CODING")
print("\t\t\t\t\t\t\t Vote commission")
print("\t\t\t\t\t  Welcome to our voting system")
print("\t-"*16)
pass
########MAIN MENU#
print("\n\n")
print("Press a number to choose the service you are looking for")
print("_"*57)
pass
print("\n\n")
print("\t\t\t 1: Identification \n\t\t\t 2: Vote \n\t\t\t 3: Results  ")
pass
try:
    choice = int(input("\n \t\t\t1 2 or 3: \t"))
except (TypeError,ValueError):
    print("you should just use numbers. you have to restart the app")

if choice == 1:
    print("\t\t\t 1: Voters \n\t\t\t 2: Candidates \n\t\t\t 3: Commission worker ")

    try:
        id = int(input("\n\t\t\t 1 2 or 3: \t"))
    except (TypeError, ValueError):
        print("you should just use numbers. you have to restart the app")
    if id == 1:
        ident_voters()
    elif choice == 2:
        pass
    elif id == 3:
        pass
    else:
        print("This choice is not recognized. use either 1,2 or 3. switch off and restart the app")
elif choice == 2:
    pass
elif choice == 3:
    pass
else:
    print("You should not use a choice going beyond 3.\n you have either to choose 1,2,3")

