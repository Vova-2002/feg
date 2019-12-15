mylist = [4,5,4,3,5,5,5,5,2,2,3,4,4,2,4]
print(mylist)
for item in range(mylist.count(2)):
    mylist.remove(2)
print(mylist)
for item in range(mylist.count(4)):
    i =  mylist.index(4)
    mylist.remove(4)
    mylist.insert(i,5)
print(mylist)
for item in range(mylist.count(3)):
    i =  mylist.index(3)
    mylist.remove(3)
    mylist.insert(i,4)
    print(mylist)
      
        
    
