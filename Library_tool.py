class library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print (f'we have books as: {self.name}')
        for book in self.booklist:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print('Hey, The book you want is available and can be issue')
        else:
            print(f'Sorry this book is already being issued by {self.lendDict[book]}')

    def addBook(self,book):
        self.booklist.append(book)
        print('Your book is added to the list')

    def returnBook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    ved = library(['The Immortals of MELUHA', 'Why You Want to Be Rich',
                    'The Dalai Lama' 'Meditation according to Yoga-Vedanta',
                    'Steve Jobs Mantra', 'The 5 am Club', 'The warren Buffet Stock portfolio',
                    '7 Habits of Highly Effective People', '8th Habbit',
                    'Invest like a Girl'],"Naresh Library")
while (True):
    print(f'Welcome to {ved.name}library. Please select your choice')
    print (' 1. Display Books\n 2. Lend Book\n 3. Add Book\n 4. Return a Book\n')

    user_choice = int(input())

    if user_choice not in (1,2,3,4):
        print('Please enter valid option')
        continue
    if user_choice == 1:
        ved.displayBooks()

    elif user_choice == 2:
        Book = input('Enter The name of the book :- ')
        user = input('Enter Your Full Name')
        ved.lendBook(user,Book)

    elif user_choice == 3:
        Book = input('Enter the name of the book to add in the library:- ')
        ved.addBook(Book)

    elif user_choice == 4:
        Book = input('Enter the name of the book to return:-')
        ved.returnBook(Book)

    else:
        print("Not a Valit option, Please try Again")

    print('Enter Q to quit and C to continue')
    user_choice2 = " "
    while (user_choice2 != 'C' and user_choice2 != 'Q'):
        user_choice2 = input()
        if user_choice == 'Q':
            exit()
        elif user_choice2 == 'C':
            continue





