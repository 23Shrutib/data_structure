data=[]

def add():
    n=int(input("How many elements do you want to add "))

    for i in range(n):
        num=input("Enter element ")
        if num.isdigit():
            new_num=int(num)
            data.append(new_num)
        else:
            print("Enter numeric value ")
            add()
    

def delete():
    if len(data)>0:
        num=input("Enter element to delete ")
        if num.isdigit():
            new_num=int(num)
            if new_num in data:
                data.remove(new_num)
            else:
                print("element does not exists!")
        else:
            print("enter numeric values ")
            delete()
    else:
        print("please enter element in data")

def update():
    num=input("Enter element to update ")
    if num.isdigit():
        new_num=int(num)
        if new_num in data:
            ele=input("Enter new element ")
            if ele.isdigit():
                new_ele=int(ele)
                i=data.index(new_num)
                data[i]=new_ele
                print("Updated!")

        else:
            print("element does not exists!")
    else:
        print("Enter numeric values ")
        update()

def read():
    print(data)

def clear():
    data.clear()

while True:
    print("1.Add \n2.Delete \n3.Update \n4.Read \n5.Clear \n6.Exit")
    option=int(input("Enter Option "))

    if option==1:
        add()
    elif option==2:
        delete()
    elif option==3:
        update()
    elif option==4:
        read()
    elif option==5:
        clear()
    elif option==6:
        break
    else:
        print("Invalid Option!")
