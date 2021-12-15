import mysql.connector
from os import system
#--------------------sign in menu-----------------------
loginCheck=0
while loginCheck ==0:
    userName = input("Enter your Username please : \n")
    password = input("Enter your password please : \n")
    userName = userName
    password = password


    try:
        mydb = mysql.connector.connect(
            host="localhost",
            database="library",
            user=userName,
            password=password
        )
        loginCheck = 1
    except:
        system('cls')
        print("Incorrect username or password")
        loginCheck=0
#----------------------------------------------------------
#--------------------Add Book-----------------------
def newBook():
    bookName = input("Please enter book Name : \n")
    shabak = input("Please enter Shabak : \n")
    price = input("Please enter price : \n")
    subject = input("Please enter subject : \n")
    number = input("How many books do you have ? \n")

    mycursor = mydb.cursor()
    sql = "INSERT INTO `books`(`BookName`, `Shabak`, `Price`, `Subject`, `Count`) VALUES (%s, %s , %s , %s , %s)"
    val = (bookName, shabak, price, subject, number)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
#----------------------------------------------------------
#--------------------Add customer-----------------------
def newCustomer():
    firstName = input("Please enter your first name : \n")
    lastName = input("Please enter your last name : \n")
    national = input("Please enter your national code : \n")
    phone = input("Please enter your phone number : \n")
    user = input("Please enter your username code : \n")
    pas = input("Please enter your password : \n")

    mycursor = mydb.cursor()
    sql = "INSERT INTO`members`(`FirstName`, `LastName`, `National`, `phone`, `Username`, `PassWord`) VALUES (%s, %s , %s , %s , %s , %s)"
    val = (firstName, lastName, national, phone, user, pas)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
# ----------------------------------------------------------
#--------------------Book list-----------------------
def ShowListOfBokks():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM books")

    myresult = mycursor.fetchall()

    for x in myresult:
      print("*"*100)

      print(x)
      print("*" * 100)
# ----------------------------------------------------------
#--------------------Borrow-----------------------
def borrow():
    ShowListOfBokks()
    bID=input("please enter id of the book \n")
    code=input("please enter your national code \n")
    mycursor = mydb.cursor()

    sql3 = "SELECT Count FROM books WHERE BookID =" + bID
    mycursor.execute(sql3)
    result = mycursor.fetchall()
    count = int(result[0][0])
    newCount = int(result[0][0]) - 1
    if count>0:
        sql = "SELECT MemberId FROM members WHERE National ="+code
        mycursor.execute(sql)
        memberID = mycursor.fetchall()

        sql2 = "INSERT INTO borrowed (BookID, MemberID) VALUES (%s, %s)"
        val2 = (bID, memberID[0][0])
        mycursor.execute(sql2, val2)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")



        sql4 = "UPDATE books SET count ="+str(newCount) +" WHERE BookID =" +bID
        mycursor.execute(sql4)
        mydb.commit()
    else:
        print("This book is not available now please try later")
# ----------------------------------------------------------
#--------------------Main menu-----------------------------
menuBtn = 5
while menuBtn != 0:
    menuBtn = int(input(" Enter 1 for adding new book \n Enter 2 for adding new customer \n Enter 3 to show list of books  \n Enter 4 to borrow books  \n Enter 0 to EXIT \n"))
    if menuBtn == 1:
        newBook()
    if menuBtn == 2:
        newCustomer()
    if menuBtn == 3:
        ShowListOfBokks()
    if menuBtn == 4:
        borrow()
    else:
        print("Invalid key please try again \n")
# ----------------------------------------------------------
