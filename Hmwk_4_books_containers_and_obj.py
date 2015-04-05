class books_container (object):
        def __init__(self):#initializes the book array with zero books :(
                self.booksList = []
         
        def newBook(self,v,w,x,y,z="1"): #creates a new book with the following parameters: v=BookID, w=Book name, x=book Author, y=Price, z=Quantity
                self.booksList.append(books(v,w,x,y,z))

        def addBook(self,x,y=1):#Used to add a new book object to the list. If a book with the same Title is already in the list then the qty of the existing book will be increased by the qty "y" passed in.
                if x.bookID == "-1":
                        return
                else:
                        if self.listSize()==0:
                                x.quantity = str(y)
                                self.booksList.append(x)                        
                        else:
                                for j in range (0,self.listSize()):
                                        if self.booksList[j].booksName == x.booksName:
                                                self.booksList[j].quantity = str(int(self.booksList[j].quantity) + y)
                                                return
                                x.quantity = str(y)
                                self.booksList.append(x)
                        
        def returnBooksIndx(self,x):#returns a book object from the index "x" in the book array. This index is the same as the indexes in the disp_all output
                if x<self.listSize():
                        return self.booksList[x]
                else:
                        print("\n"+str(x)+ " references a non existant index.\n")
                        err = books("-1")
                        return err

        def returnBooksTitle(self,x):#returns the first book object from the book array with the title passed in.
                x = str(x)
                if self.listSize() != 0:
                        for j in range (0,self.listSize()):
                                if x == self.booksList[j].booksName:
                                        return self.booksList[j]
                        print("\n"+x+ " references a non existant title.\n")
                        err = books("-1")
                        return err
                else:
                        print("\nThe container has no books to give.\n")
                        err = books("-1")
                        return err
        
        def disp_info(self,x):#returns a string displaying all the info of the book in the "x" index of the book array
                string = self.booksList[x].bookID+"\t  "+self.booksList[x].booksName+self.booksList[x].NtabNum+self.booksList[x].booksAuthor+self.booksList[x].AtabNum+self.booksList[x].quantity+"\t$"+self.booksList[x].price
                return string
                  
        def disp_all(self):#Displays a formatted list of all books in the Inventory/Cart
                print("List No.\t Category Book Name\t\tAuthor\t\tQty.\tPrice")
                print("================================================================================")
                for self.x in range(0,self.listSize()):
                        print (str(self.x)+".\t\t",self.disp_info(self.x))
                print("\n\n")

        def updateBookInfo(self,x,y,z): #self, Title,booksValueToChange,newValue
                x = str(x)
                z = str(z)
                if y == 1:
                        for j in range(0,self.listSize()):
                                if self.booksList[j].booksName == x:
                                        self.booksList[j].bookID = z
                                        print("Book ID updated")
                elif y == 2:
                        for j in range(0,self.listSize()):
                                if self.booksList[j].booksName == x:
                                        self.booksList[j].booksName = z
                                        print("Book name updated")
                elif y == 3:
                        for j in range(0,self.listSize()):
                                if self.booksList[j].booksName == x:
                                        self.booksList[j].booksAuthor = z
                                        print("Book Author updated")
                elif y == 4:
                        for j in range(0,self.listSize()):
                                if self.booksList[j].booksName == x:
                                        self.booksList[j].quantity = z
                                        print("Book quantity updated")
                elif y == 5:
                        for j in range(0,self.listSize()):
                                if self.booksList[j].booksName == x:
                                        self.booksList[j].price = z
                                        print("Book price updated")
                else:
                    print(y," is not valid input. No changes were made to Item ", x)
        def getIndxFromTitle(self,x):#returns the index of the first book in the array which matches the passed in title.
                x = str(x)
                if self.listSize() != 0:
                        for j in range (0,self.listSize()):
                                if x == self.booksList[j].booksName:
                                        return j
                        print("\n"+x+ " references a non existant title.\n")
                        return -1
                else:
                        print("\nThe container has no books to give.\n")
                        return -2
 
        def listSize(self): #returns the length of the Book array
                return len(self.booksList)
        
        def getCat(self,x):#:3 Return Category
                return self.booksList[x].BookID
        
        def getTitle(self,x):# Return Title
                return self.booksList[x].booksName
        
        def getAuthor(self,x):# Return Author
                return self.booksList[x].booksAuthor
        
        def getQty(self,x):# Return qty in container
                 return self.booksList[x].quantity
                
        def getPrice(self,x):# Return price of single book
                return self.booksList[x].price
        
        def removeBook(self,x): #removes a book from the book array. It's gone.
                print ("removed "+self.disp_info(x))
                self.booksList.pop(x)
 
        def booksTotalPrice(self): #returns the total cost of all books in theBook array as a formatted string. Grab index 12 to the End of the returned string to get only the numerical price
                total = 0
                for x in range(0,self.listSize()):
                        total = total + (float(self.booksList[x].quantity)*float(self.booksList[x].price))
                return str("Total cost $"+"{0:.2f}".format(total))
                
        def booksTotalQty(self):
                total = 0
                for x in range(0,self.listSize()):
                        total = total + (int(self.booksList[x].quantity))
                return str("Qty. total "+str(total)+" items")
                
class books (object):#this is a book object. It has five things. BookID, book name, qty of this book, price of book, and number of tabs required to make the name fit in the display list.
                def __init__(self, bookID = "Empty_Category", booksName = "Empty_Name",booksAuthor = "Empty_Author", price = "1", quantity = "0"):
                        self.bookID = str(bookID)
                        self.booksName = str(booksName)
                        self.booksAuthor = str(booksAuthor)
                        self.quantity = str(quantity)
                        self.price = str(price)
                        #maybe make this thing a dynamic loop later...not now. The disp_all will need to find the largest tabNum as well for formatting.
                        if len(self.booksName)>10:
                                self.NtabNum = "\t"
                        elif len(self.booksName)>5:
                                self.NtabNum = "\t\t"
                        else:
                                self.NtabNum = "\t\t\t"
                        if len(self.booksAuthor)>10:
                                self.AtabNum = "\t"
                        elif len(self.booksAuthor)>5:
                                self.AtabNum = "\t\t"
                        else:
                                self.AtabNum = "\t\t\t"



################TEST CASES################
Inventory = books_container()
Cart = books_container()
Inventory.returnBooksTitle("Penthouse").bookID
Inventory.newBook("2343","Books","Ann. Author","0.65")
Inventory.newBook("5634","Binders","Ann. Author","1.65")
Inventory.newBook("0923","Pens","Ann. Author","5.65")
Inventory.newBook("4567","Chocolate","Ann. Author","5.65")
Inventory.newBook("2653","Staples","Ann. Author","3.65")
Inventory.newBook("3097","Pencils","Ann. Author","9.65")
Inventory.newBook("2022","Towels","Ann. Author","1.30")
Inventory.newBook("3421","Paper","Ann. Author","6.65")
Inventory.newBook("0455","Detergent","Ann. Author","3.65")
Inventory.disp_all()
Cart.addBook(Inventory.returnBooksIndx(3),2)
Cart.addBook(Inventory.returnBooksIndx(1),3)
Cart.addBook(Inventory.returnBooksIndx(5),9)
Cart.addBook(Inventory.returnBooksIndx(6),1)
Cart.addBook(Inventory.returnBooksIndx(23),3)
Cart.addBook(Inventory.returnBooksIndx(3),4)
Cart.addBook(Inventory.returnBooksTitle("Binders"),3)
Cart.addBook(Inventory.returnBooksIndx(4),5)
Cart.addBook(Inventory.returnBooksIndx(47),3)
Cart.addBook(Inventory.returnBooksTitle("Paper"),3)
Cart.addBook(Inventory.returnBooksIndx(3),4)
Cart.addBook(Inventory.returnBooksIndx(6))
Cart.addBook(Inventory.returnBooksTitle("Penthouse"),3)
Cart.addBook(Inventory.returnBooksTitle("Detergent"),4)
Cart.addBook(Inventory.returnBooksIndx(8),1)
Cart.disp_all()
print(Cart.booksTotalQty())
print(Cart.booksTotalPrice())

#####################Output########################
#
#The container has no books to give.
#
#List No.	 Category Book Name		Author		Qty.	Price
#================================================================================
#0.		 2343	  Books			Ann. Author	1	$0.65
#1.		 5634	  Binders		Ann. Author	1	$1.65
#2.		 0923	  Pens			Ann. Author	1	$5.65
#3.		 4567	  Chocolate		Ann. Author	1	$5.65
#4.		 2653	  Staples		Ann. Author	1	$3.65
#5.		 3097	  Pencils		Ann. Author	1	$9.65
#6.		 2022	  Towels		Ann. Author	1	$1.30
#7.		 3421	  Paper			Ann. Author	1	$6.65
#8.		 0455	  Detergent		Ann. Author	1	$3.65
#
#
#
#
#23 references a non existant index.
#
#
#47 references a non existant index.
#
#
#Penthouse references a non existant title.
#
#List No.	 Category Book Name		Author		Qty.	Price
#================================================================================
#0.		 4567	  Chocolate		Ann. Author	10	$5.65
#1.		 5634	  Binders		Ann. Author	6	$1.65
#2.		 3097	  Pencils		Ann. Author	9	$9.65
#3.		 2022	  Towels		Ann. Author	2	$1.30
#4.		 2653	  Staples		Ann. Author	5	$3.65
#5.		 3421	  Paper			Ann. Author	3	$6.65
#6.		 0455	  Detergent		Ann. Author	5	$3.65
#
#
#
#Qty. total 39 items
#Total cost $208.65
