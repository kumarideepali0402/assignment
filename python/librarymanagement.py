list = [[101,"Rich Dad Poor Dad", "Robert Kiyosaki",5],[102,"The Girl in The Room 105",'Chetan Bhagat',10],[103,'A bunch of old letters','Jawahar Lal Nehru',5],[104,'Do Epic Shit','Ankur Warikoo',7]]
print(f" List of {len(list)} books present in the library")
print()

for i in list:
    print(i)
print()
        
print("For Manager of Library type --> Manager in any case : ")
print("As a user of Library Books Type your Name : ")

def add_books():
    print("Manager can add only one book at a time....")
    book_id = int(input("Enter Book ID : "))
    book_name = input("Enter Book name : ")
    book_writer = input("Enter name of the book writer : ")
    book_quantity = int(input("Enter the qunatity of BOOKS : "))
    new_book = [book_id,book_name,book_writer,book_quantity]
    list.append(new_book)
    print("The set of books available in the library currently is : \n")
    print()
    for j in list:
        print(j)
    print()
    user()


def  user():
    userinput = input("Enter Who are You ? --- ")
    userinput = userinput.lower()
    if(userinput=='manager'):
        print("You are using the library as Manager.")
        print("You can add books to the library now for the user.")
        print("Type in Yes or No to add Books")
        input_by_manager = input("Do you want to add books to the library : ")
        input_by_manager = input_by_manager.lower()
        if(input_by_manager=='yes'):
            add_books()
        else:
            print("Call the reader to read book ----- ")
            user()

    else:
        global user
        userinput = userinput.capitalize()
        user =userinput
        print("You are using the Library as Book reader.\nList of book is as folow in the library :\n")
        
        print(f"Your name is {user} and you are here to use Library Books") 
        print("Basic Instructions Regarding Library Books :\n3 Books are allowed per user.\nBook taken by the reader from the library need to be submitted within 14 days.\n")
        for j in list:
            print(j)
        print()
        book_taken_by_user()


def book_taken_by_user():
    book_taken_count = 0
    flag = 1
    number_of_books_that_user_want = int(input("Enter The number of books that you want : "))
    if(number_of_books_that_user_want<=3 and number_of_books_that_user_want>=1):
        for j in range(number_of_books_that_user_want):
            for i in range(len(list)):
                book_id_taken = int(input("Enter The book id : "))
                if(book_id_taken == list[i][1] and list[i][3]>0):
                    print("Congratulation your book is available and you can take it.")
                    flag = 0
                    book_taken_count+=1
                    list[i][3]-=1
                if(flag==0):
                    break

                else:
                    if(book_id_taken == list[i][1]):
                        print("Sorry, Quantity of this book Id is 0")
                        for j in list:
                            print(j)
                        print()
                        book_taken_by_user()

                    else:
                        print("Sorry, No Book found !\nTry Aagain")
                        for j in list:
                            print(j)
                        print()
                        book_taken_by_user()
    else:
        print(" Only 3 books are allowed for one user ... ")
        book_taken_by_user()
        
            
            



user()