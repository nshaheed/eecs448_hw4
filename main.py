import Hmwk_4_books_containers_and_obj as obj
from readfile import buildDBfromFile
import readline # makes input builtin nicer

print("Welcome to the Data Base book ordering system")
print("There are 6 things you can do:")

# Initialization of the order and store inventory containers
inventory = buildDBfromFile("bookdatabase.txt")
order     = obj.books_container()

def displayFromCategory():
	category = input("What category do you want displayed(Science Fiction, Travel, Software Engineering)? ")
	print("\nBooks of Category ", category)
	rList = inventory.returnCategoryList(category)
	for j in range (0,len(rList)):
		print(rList[j].booksName+rList[j].NtabNum+rList[j].booksAuthor+rList[j].AtabNum+rList[j].price)
	
# Add a book to the order
def addBookToOrder():
	title      = input("Enter the title that you wish to add to your order: ")
	foundTitle = False;
	titleIdx   = -1;
	
	# Look for the title in the inventory
	for i in range(0, inventory.listSize()):
		if inventory.getTitle(i) == title:
			foundTitle = True
			titleIdx   = i
			
			# If title is found, exit the loop
			break
			
	if foundTitle:
		order.addBook(inventory.returnBooksIndx(titleIdx),1)
		print("Book added to order")
	else:
		print("Could not find title")
	
# Remove a book from the order
def removeBookFromOrder():
	title = input("Enter the title that you wish to remove from your order: ")
	foundTitle = False;
	titleIdx   = -1;
	
	for i in range(inventory.listSize()):
		if inventory.getTitle(i) == title:
			foundTitle = True
			titleIdx   = i
			
			# If title is found, exit loop
			break
			
	if foundTitle:
		order.removeBook(titleIdx)
	else:
		print("Could not find title")
		
		
# Prints the current order
def printOrder():
	order.disp_all()
	
	sfCounter  = 0
	tvlCounter = 0
	soeCounter = 0
	
	# Increments the counters for the three categories if they are found in the order
	for i in range(order.listSize()):
		x = order.getCat(i)
		if x == "Science Fiction":
			sfCounter = sfCounter + 1
		elif x == "Travel":
			tvlCOunter = tvlCounter + 1
		elif x == "Software Engineering":
			soeCounter = soeCounter + 1
			
	# Outputs warning if you two book from each category haven't been added to the order
	if sfCounter < 2 or tvlCounter < 2 or soeCounter < 2:
		print("Warning: you have not purchased at least two books in each category")

# Main user input loop
while True: 
	print("1) Display all books in a category (Science Fiction, Travel, Software Engineering)")
	print("2) Add a book to the order")
	print("3) Remove a book from the order")
	print("4) Print Order")
	print("5) Exit")

	actionStr = input("Select your action: ")
	try:
		action    = int(actionStr)

		# process different inputs
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
	except ValueError:
		print("Could not read input, try again")

