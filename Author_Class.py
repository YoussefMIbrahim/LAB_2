class Author:
    def __init__(self, name):
        self.name = name
        self.books = []
    #publish function to add a book to the list
    def publish(self, title):
        if title in self.books:
            print('Sorry that\'s a duplicate')
        else:
            self.books.append(title)
    # string output when you print class
    def __str__(self):
        titles = ', '.join(self.books) or 'No published books'
        return f'{self.name}. Books: {titles}'

def main():
    # examples using my Author class
    rowling = Author('jk rowling')
    rowling.publish('harry potter')
    rowling.publish('fantastic')
    rowling.publish('fantastic')
    print(rowling)

    me = Author('Youssef')
    print(me)

main()