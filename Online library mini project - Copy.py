#Create library class
#Display book
#lend book(who owns book)
#add book
#return book
#Constructor will have (booklist , library name)
#dictionary (book:person)
#run infinite while loop in main fucnton to take input 

class unilibr:
    pass

    def sbname(self):
     return f" Book Name is {self.name}"

    def __init__(self,bname):
     self.name=bname

    def showbandn(self):
     return f"Name is {self.name} , Books owned are {self.book1},{self.book2},{self.book3}"

    def __init__(self,cusname,cusbookl):
     self.name=cusname
     self.booklist=cusbookl

    def displaybook(self):
     print(f"Books owned are {self.booklist}")
     return""

    def borrowbook(self):
       pass

    def lendbook():
     pass

    def returnbook():
     pass


DOAWK="Diary of a wimpy kid"
Driven="Driven"
DillaTime="DillaTime"   
TheMambaMentality="TheMambaMentality"

Erenlib=unilibr("Eren", "")

start=input("start\n")
while start=="borrow":
  print(Erenlib.borrowbook())
else:
  print("error")
  print(Erenlib.displaybook())
