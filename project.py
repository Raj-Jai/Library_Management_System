
#IMPORTING REQUIRED MODULES
import csv
import os
from prettytable import PrettyTable as pt

from datetime import date

today = date.today()

#FUNTION FOR ADDING A BOOK
def addaBook(bookTitle,bookGenre):
	file = open("bookList.csv","a",newline="")
	writer = csv.writer(file)
	
	writer.writerow([bookIdGen(),bookTitle,bookGenre,1])
	print("\n \t BOOK SUCESSFULLY ADDED ! \n")
	waitnig  = input("Press Any Key To Continue.... \n  \n")
	file.close()
	
#FUNTION TO GENERATE BOOK ID
def bookIdGen():
        file = open("bookList.csv","r")
        reader = csv.reader(file)
        container = []
        for data in reader:
                container.append(data)
        lastId=container[-1][0]
        newId = str(int(lastId) + 1)
        return newId
        
#FUNTION TO DISPLAY ALL BOOK LIST
def displayBook():
        file = open("bookList.csv","r")
        reader = csv.reader(file)
        table = pt(["BOOK ID","BOOK TITLE","GENRE","STATUS"])
        for d in reader:
                if d[3] == "1":
                        status = "Available"
                else:
                        status = "Issued"
                        
                table.add_row([d[0],d[1],d[2],status])
        print(table)
        waitnig  = input("Press Any Key To Continue.... \n  \n")
        file.close()

#FUNTION TO ISSUE BOOK TO STUDENT        
def issueBook(bookId,studName):
        file= open("bookList.csv","r")
        tempF= open("temp.csv","w",newline="")
        writer = csv.writer(tempF)
        reader = csv.reader(file)
        errorType = 2
        for data in reader:
                if data[0] == bookId and data[3] == "1" :
                        data[3] = studName
                        errorType = 0 
                elif data[0] == bookId and data[3] != "1":
                        issueData = data
                        errorType = 1
                date = today.strftime("%d %B, %Y")        
                data.append(date)     
                writer.writerow(data)
        
        if errorType == 1:
                print(" \n \t Book Already Issued To",issueData[3],"on",issueData[4],"\n")
        elif errorType == 2 :
                print("\n\t Book With Given ID Do Not Exist \n")
        else:
                print("\n \t BOOK SUCEESFULLY ISSUED ! \n ")
        file.close()
        tempF.close()
        os.remove("bookList.csv")
        os.rename("temp.csv","bookList.csv")
        waitnig  = input("Press Any Key To Continue.... \n  \n")
        
#FUNTION TO RETURN BOOK TO LIBRARY
def returnBook(bookId):
        file= open("bookList.csv","r")
        tempF= open("temp.csv","w",newline="")
        writer = csv.writer(tempF)
        reader = csv.reader(file)
        errorType= 0
        for data in reader:
                if data[0] == bookId:
                        data[3] = 1
                        errorType = 1
                        
                writer.writerow(data)

        if errorType == 0:
                print(" \n BOOK WITH GIVEN ID DO NOT EXIST \n ")
        else:
                print("\n BOOK SUCCESSFULLY RETURNED ! \n ")
        file.close()
        tempF.close()
        os.remove("bookList.csv")
        os.rename("temp.csv","bookList.csv")
        waitnig  = input("Press Any Key To Continue.... \n  \n")

#FUNTION TO REMOVE BOOK FROM LIBRARY        
def removeBook(bookId):
        file= open("bookList.csv","r")
        tempF= open("temp.csv","w",newline="")
        writer = csv.writer(tempF)
        reader = csv.reader(file)
        errorType= 0
        for data in reader:
                if data[0] == bookId:
                        errorType = 1
                        continue
                        
                writer.writerow(data)

        if errorType == 0:
                print(" \n BOOK WITH GIVEN ID DO NOT EXIST \n ")
        else:
                print("\n BOOK SUCCESSFULLY REMOVED ! \n ")
        file.close()
        tempF.close()
        os.remove("bookList.csv")
        os.rename("temp.csv","bookList.csv")
        waitnig  = input("Press Any Key To Continue.... \n  \n")

        

#NAVIGATION MENU
query = 0
while query!= "6" :
        print("\t \t --------LIBRARY MANAGEMENT PROGRAM------")
        print()
        print("#Choose Required Action :- \n \n 1) ADD A BOOK \n 2)DISPLAY ALL BOOK \n 3) ISSUE A BOOK \n 4) RETURN A BOOK \n 5)REMOVE A BOOK \n 6) EXIT " )
        query = input()
        if query == "1" :
        
                bookTitle = input("ENTER BOOK TITLE --> ")
                choice=0
                while choice != "1" and choice!="2" :
                        print("SELECT BOOK GENRE:- \ 1)FICTION \ 2)NON-FICTION")
                        choice = input()
                        if choice == "1":
                                bookGenre="FICTION"
                        elif choice == "2":
                                bookGenre="NON-FICTION"
                        else:
                                print("OUT OF THE BOX CHOICE .ENTER AGAIN!! \n")
                
                addaBook(bookTitle,bookGenre)
        elif query == "2" :
                displayBook()
        elif query == "3":
                bookId = input("ID of Book To be Issued -->")
                studName = input("Student Name --> ")
                issueBook(bookId,studName)
        elif query == "4":
                bookId = input("ID of Book To Return -->")
                returnBook(bookId)
        elif query == "5":
                bookId = input("ID of Book To Remove -->")
                removeBook(bookId)
        else:
                print("\t \t ---------SEE YOU SOON :) ---------")

