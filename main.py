import Hmwk_4_books_containers_and_obj

print("Welcome to the Data Base book ordering system")
print("There are 6 things you can do:")

# Initialization of the order and store inventory containers
inventory = Hmwk_4_books_containers_and_obj.books_container()
inventory.newBook("Cat1","Books","Ann. Author","0.65") # This is for testing
order     = Hmwk_4_books_containers_and_obj.books_container()

def displayFromCategory():
	category = input("What category do you want displayed(Science Fiction, Travel, Software Engineering)? ")
	print("\nBooks of Category ", category)
	rList = inventory.returnCategoryList(category)
	for j in range (0,len(rList)):
		print(rList[j].booksName+rList[j].NtabNum+rList[j].booksAuthor+rList[j].AtabNum+rList[j].price)
	
def addBookToOrder():
	title      = input("Enter the title that you wish to add to your order: ")
	foundTitle = False;
	titleIdx   = -1;
	
	for i in range(0, inventory.listSize()):
		if inventory.getTitle(i) == title:
			foundTitle = True
			titleIdx   = i
			break
			
	if foundTitle:
		order.addBook(inventory.returnBooksIndx(titleIdx),1)
		print("Book added to order")
	else:
		print("Could not find title")
	
def removeBookFromOrder():
	title = input("Enter the title that you wish to remove from your order: ")
	foundTitle = False;
	titleIdx   = -1;
	
	for i in range(0, inventory.listSize()):
		if inventory.getTitle(i) == title:
			foundTitle = True
			titleIdx   = i
			break
			
	if foundTitle:
		order.removeBook(titleIdx)
	else:
		print("Could not find title")
		
		
def printOrder():
	order.disp_all()

while True: 
	print("1) Display all books in a category (Science Fiction, Travel, Software Engineering)")
	print("2) Add a book to the order")
	print("3) Remove a book from the order")
	print("4) Print Order")
	print("5) Exit")
	
	actionStr = input("Select your action: ")
	action    = int(actionStr)
	
	if action == 1:
		displayFromCategory()
	elif action == 2:
		addBookToOrder()
	elif action == 3:
		removeBookFromOrder()
	elif action == 4:
		printOrder()
	elif action == 5:
		break
	else:
		print("Incorrect input, try again")
		
		
