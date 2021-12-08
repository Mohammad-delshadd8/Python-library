import mysql.connector
from os import system
#--------------------sign in menu-----------------------
loginCheck=0
while loginCheck ==0:
    userName = input("Enter your Username please : \n")
    password = input("Enter your password please : \n")

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
#--------------------Main menu-----------------------
menuBtn = 5
while menuBtn != 0:
    menuBtn = int(input("Enter 1 for adding new book \n Enter 2 for adding new customer \n Enter 0 to EXIT \n"))
    if menuBtn == 1:
        newBook()
    if menuBtn == 2:
        newCustomer()
# ----------------------------------------------------------