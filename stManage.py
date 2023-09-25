class  Student:
    def __init__(self,name,rollno,m1,m2):
        self.name=name
        self.rollno=rollno
        self.m1=m1
        self.m2=m2

    def accept(self,name,rollno,marks1,marks2):
        ob=Student(name,rollno,marks1,marks2)
        ls.append(ob)

    def display(self,ob):
        print("Name: ",ob.name)
        print("Rollno: ",ob.rollno)
        print("Marks1: ",ob.m1)
        print("Marks2: ",ob.m2)
        print("\n")

    def search(self,rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno==rn):
                return i

    def delete(self,rn):
        i=obj.search(rn)
        del ls[i]

    def update(self,rn,No):
        i=obj.search(rn)
        roll=No
        ls[i].rollno=roll

ls=[]
obj=Student('',0,0,0)

print("\nOperation used, ")
print("\n1.Aceept Student Details \n2. Display Student Details \n3. Search Detail of a student \n4. Delete Detail of a student \n5. Update Student Details \n6. Exit")

#ch=int(input("Enter choice: "))
#if(ch==1):
obj.accept("A",1,100,100)
obj.accept("B",2,90,90)
obj.accept("C",3,80,80)

#elif(ch==2):
print("\n")
print("\nList of Student\n")
for i in range(ls.__len__()):
    obj.display(ls[i])

#elif(ch==3):
print("\nStudent found,")
s=obj.search(2)
obj.display(ls[s])

#elif(ch==4):
obj.delete(2)
print(ls.__len__())
print("list after deletion")

for i in range(ls.__len__()):
    obj.display(ls[i])

#elif(ch==5):
obj.update(3,2)
print(ls.__len__())
print("List after updation")
for i in range (ls.__len__()):
    obj.display(ls[i])

#else:
print("Thank You!")
