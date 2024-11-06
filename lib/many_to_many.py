class Author:
    all_authors = []

    def __init__(self, name): 
        self.name = name
    
    def contracts(self):
        return [contract for contract in Contract.all_contracts if self is contract.author]
    
    def books(self):
        return list({contract.book for contract in self.contracts()})
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
    
class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        type(self).all_books.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all_contracts if self is contract.book]
    
    def authors(self):
        return list({contract.author for contract in self.contracts()})

    

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties): 
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        type(self).all_contracts.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception()
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception()
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception()
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception()
        
    @classmethod 
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date is date]

# author = Author("Name")
# book1 = Book("Title")
# book2 = Book("Wow")
# contract = Contract(author, book1, '01/01/2001', 50000)
# contract = Contract(author, book1, '01/01/2001', 50000)
# import ipdb; ipdb.set_trace()
        