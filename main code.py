 #Written by Avirat Sharma
 #Use it 
# library management system
# Create a library class
#     display books
#     lend books (Who owns the book if is not available)
#     add books
#     return books
#
# dictionary - (books - nameOfPerson)
#
# create a main function and run an infinite while loop for asking user input

class Library:
    def __init__(self,bookList,lname): #l means Library
        self.booList = bookList
        self.lname = lname
        self.lendDict = {}

    def displaybook(self):
        print("The following books in our library.")
        for book in self.booList:
            print(book)

    def lendbook(self,book,user):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lend-Book data has been updated!. Now you can take the book")
        else:
            print(f"Sorry! this book is being used by {self.lendDict[book]} ")

    def addbook(self,book):
        self.booList.append(book)
        print("Thank you! Book has been added.")

    def returnbook(self,book):
        self.lendDict.pop(book)
        print("Return complete.. Thank you!!")

if __name__ == '__main__':
    books = Library(['Paulo Coelho','Harry Potter','Bounce','Python',
                     'C Basics'],"The Library Of Avirat")
    try:
        while(True):
            print(f"Welcome to {books.lname} .. Please chose what you want!")
            print("1.Display Books")
            print("2.Lend Books")
            print("3.Add Books")
            print("4.Return Books")
            user_input = input("Enter= ")
            if user_input not in ['1','2','3','4']:
                print("Please Enter the valid option")
                continue
            else:
                user_input = int(user_input)

            if user_input == 1:
                books.displaybook()

            elif user_input == 2:
                book = input("Enter the book you want to lend:")
                user = input("Enter your name:")
                books.lendbook(book,user)

            elif user_input == 3:
                book = input("Enter the book you want to add:")
                books.addbook(book)

            elif user_input == 4:
                book = input("Enter the book you want to return:")
                books.returnbook(book)

            user_input2 = ""
            while(user_input2!= "q" and user_input2!="c"):
                print("Press q to quit and c to continue")
                user_input2 = input("Enter= ")
                if user_input2 == "q":
                    exit()
                elif user_input2 == "c":
                    continue

    except Exception as e:
        
        print("Error!!",e)



