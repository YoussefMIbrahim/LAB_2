class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        if title in self.books:
            print('Sorry that\'s a duplicate')
        else:
            self.books.append(title)
    # 
    def __str__(self):
        titles = ', '.join(self.books) or 'No published books'
        return f'{self.name}. Books: {titles}'

def main():
    rowling = Author('jk rowling')
    rowling.publish('harry potter')
    rowling.publish('fantastic')
    rowling.publish('fantastic')
    print(rowling)

    me = Author('Youssef')
    print(me)

main()