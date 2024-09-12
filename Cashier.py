def admin():
    global DB
    print("Our Data")
    for x in DB:
        print(x)

    ipt = int(input("Menu : \n1. Add Product\n2. Delete Product\n""3. Rename Product\n9. Back\n=> "))

    if ipt == 1:
        print("Add Product")
    elif ipt == 2:
        print("Delete Product")
    elif ipt == 3:
        print("Rename Product")
    elif ipt == 9:
        Dashboard()
    else:
        -1

def user():
    x = xx = Total = 0
    global DB
    while x < 1:
        code = int(input("Code Product: "))
        if code == 0:
            break
        if code == 1:
            print(Total)
            break
        else:
            while code != DB[xx][0] and xx < len(DB):
                xx += 1
            if code == DB[xx][0]:
                Total += DB[xx][1]

def Dashboard():
    print("-"*5,"Cashier","-"*5)
    ipt = int(input("Menu : \n1. Admin Dashboard \n2. User Dashboard \n\n=> "))

    if ipt == 1:
        admin()
    elif ipt == 2:
        user()
    else:
        print("Invalid input")
        -1

DB = ((10001, 200000), (11111, 100000), (22222, 50000), (33333, 25000))

Dashboard()