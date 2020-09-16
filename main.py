
def getdate():
    import datetime
    return datetime.datetime.now()

import datetime
def gettime():
    return datetime.datetime.now()

def take(k):
    if k == 1:
        c=int(input("Enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input('type here\n')
            with open ("dharmesh_ex.txt", "a") as f:
                f.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
        elif(c==2):
            value=input('type here\n')
            with open ("dharmesh_food.txt", "a") as f:
                f.write(str([str(gettime())])+":" +value+"\n")
            print("successfully written")
    if k == 2:
        c=int(input("Enter 1 for excersise and 2 for food"))
        if (c==1):
            value=input('type here\n')
            with open("yash_ex.txt", "a") as f:
                f.write(str([str(gettime())])+ ":" +value+"\n")
            print("successfully written")
        elif(c==2):
            value=input("type here\n")
            with open("yash_food.txt", "a") as f:
                f.write(str([str(gettime())])+ ":" +value+"\n")
            print("successfully written")
    if k == 3:
        c=int(input("Enter 1 for excersise and 2 for food"))
        if (c==1):
            value=input('type here\n')
            with open("raj_ex.txt", "a") as f:
                f.write(str([str(gettime())])+":" +value+"\n")
            print("successfully writen")
        elif(c==2):
            value= input("type here\n")
            with open("raj_food.txt", "a") as f:
                f.write(str([str(gettime())])+"+"+value+"\n")
            print("successfully written")
    else:
        print("Enter valid input (1(dharmesh),2(yash),3(raj)")
def retrieve(k):
    if k==1:
        c=int(input("Enter 1 for excersise and 2 for food"))
        if (c==1):
            with open('dharmesh_ex.txt') as f:
                for i in f:
                    print(i,end=" ")
        elif(c==2):
            with open("dharmesh_food.txt") as f:
                for i in f:
                    print(i,end=" ")
    elif k==2:
        c=int(input("Enter 1 for excersise and 2 for food"))
        if ( c==1):
            with open("yash_ex.txt") as f:
                for i in f:
                    print(i,end=" ")
        elif(c==2):
            with open("yash_food.txt") as f:
                for i in f:
                    print(i,end="")
    elif k==3:
        c=int(input("Enter 1 for excersise and 2 for food"))
        if (c==1):
            with open("raj_ex.txt") as f:
                for i in f:
                    print(i,end=" ")
        elif(c==2):
            with open("raj_food") as f:
                for i in f:
                    print(i, end=" ")
    else:
        print("Enter valid input(dharmesh,yash,raj)")
print("Health management system: ")
a=int(input("press 1 for log the value and 2 for retrieve"))
if a==1:
    b=int(input("press 1 for dharmesh 2 for yash 3 for raj"))
    take(b)
else:
    b= int(input("press 1 for dharmesh 2 for yash 3 for raj"))
    retrieve(b)
