#/bin/python
import Hmwk_4_books_containers_and_obj as obj

def buildDBfromFile(filename):
    file = open(filename)
    db = obj.books_container()
    category = False
    price = False
    for line in file:
        if line[0] == "-": # book entry
            [author, title] = line[2:].split(", ", 1) # drop "- ", then split at the comma
            title = title[:title.find("[S1]")].strip() # remove [S1] and whitespace - users must be able to type the full title in current implementation
            if not category:
                raise ValueError("Database file could not be parsed.")
            else:
                db.newBook(category, title, author, price)
        else: # we are reading a section heading
            category = line[:line.find(" Books")]
            price = int(line[line.find("$")+1:].split(" ")[0]) # ugly hack based on db file layout - goes from after the first '$' to the following space
    return db
