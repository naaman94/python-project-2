from functools import reduce

class Person: 
    def __init__(self,Name,Address):
            self._name = Name
            self._address = Address
    def getName(self):
        return self._name
    def setName(self,name):
        self._name=name
        print (" New Name for Person is",self._name)
        
    def getAddress(self):
        return self._address
    def setAddress(self,newAdd):
        self._address=newAdd
        print ("New Address for Person is",self._address)
    def __del__(self):
        print (self._name,'has been deleted')
        
class Employee(Person):
    def __init__(self,EmNo,Name,Address,Salary,JobTilte,loans):
        self.EmployeeNo = int(EmNo)
        Person.__init__(self,Name,Address)
        self.__Salary = float(Salary)
        self.__JobTitle=str(JobTilte)
        self.__loans = loans
        
    def setSalary(self,S):
        self.__Salary=S
    def getSalary(self):
        return self.__Salary
    def setJobTitle(self,J):
        self.__JobTitle= J
    def getJobTitle(self):
        return self.__JobTitle
    
    def getLoans(self):
        return self.__loans
    def totlaLoans(self):
        return sum(self.__loans)
    def maxLoans(self):
         if not self.__loans:
            return "empty"
         else:
            return max(self.__loans)
        
    def minLoans(self):
        if not self.__loans:
            return "empty"
        else:
            return min(self.__loans)
    def setLoans(self,NewLoan):
        self.__loans.append(NewLoan)
    def infoEmployee(self):
        print( " Employee number:", self.EmployeeNo )
        print( " Name:", self.getName())
        print( " Address:", self.getAddress())
        print( " Salary:", self.getSalary())
        print( " Job Title:", self.getJobTitle())
        print( " Loans:", self.getLoans())
        print( " totlaLoans:", self.totlaLoans())
        print()
        
    def __del__(self):
        print ("Employee Object is Deleted")

class Student(Person):
   def __init__(self,Student_Number,Name,Address,Subject:str,Mark:dict):
       self.Student_Number=Student_Number
       self.__Subject=Subject
       self.__Mark=Mark
       Person.__init__(self,Name,Address)
   def setSubject(self,Subject):
       self.__Subject=Subject
   def getSubject(self):
      return self.__Subject
   def setMark(self,key,value):
       self.__Mark[key]=value
   def getMark(self):
       return self.__Mark
   def getavg(self):
       total=0
       for  avg in self.__Mark.values():
           total=total+(avg/len(self.__Mark))
       return total
   def getAmark(self):
       AMark={}
       for x,y in self.__Mark.items():
           if y>90:
               AMark[x]=y
       return AMark
   
   def infoStudent(self):
        print( " Student_Number:", self.Student_Number )
        print( " Name:", self.getName())
        print( " Address:", self.getAddress())
        print( " Subject:", self.getSubject())
        print( " Marks:", self.getMark())
        print( " AVG:", self.getavg())
        print()
        
   def __del__(self):
        print("Student Object is Deleted")
"""1""" 
EmployeesList=[]
Employee1= Employee(100,"Ahmed Yazan","Amman jordan",500,"HR Consultant",[434,200,1020])
EmployeesList.append(Employee1)
Employee2= Employee(2000,"Hselfala Rana","Aqaba jordan",750,"Department Manager",[150,3000,250])
EmployeesList.append(Employee2)
Employee3= Employee(3000,"Mariam Ali","Mafraq jordan",600,"HR s Consultant",[304,1000,250,300,500,235])
EmployeesList.append(Employee3)
Employee4= Employee(4000,"Yasmin Mohamed","Karak jordan",865,"Director",[])
EmployeesList.append(Employee4)

"""2""" 
StudentsList=[]
Student1= Student(20191000,"Khalid ali","Irbid jordan","History",{"English":80,"Arabic":90,"Art":95,"managment":75})
StudentsList.append(Student1)
Student2= Student(20182000,"Reem Hani","Zaraqa jordan","Softwere Eng",{"English":80,"Arabic":90,"managment":75,"Calculus":85,"OS":73,"Programming":90})
StudentsList.append(Student2)
Student3= Student(20161001,"Nawras Abdallah","Amman jordan","Art",{"English":83,"Arabic":92,"Art":90,"managment":70})
StudentsList.append(Student3)
Student4= Student(20172030,"Reem Hani","Zaraqa jordan","Softwere Eng",{"English":83,"Arabic":92,"managment":70,"Calculus":80,"OS":79,"Programming":91})
StudentsList.append(Student4)

print("""Q 3""")
print("Total Number of Employees is ",len(EmployeesList))

print("""Q 4""")
print("Total Number of Students is ",len(StudentsList))

print("""Q 5""")

for x in EmployeesList:
    x.infoEmployee()
    
    
print("""Q 6""")

for x in StudentsList:
    x.infoStudent()
    
print("""Q 7""")
def hiesistStudentAvg():
    listMax=[]
    for x in StudentsList:
        listMax.append(x.getavg())
    return max(listMax)
print(hiesistStudentAvg())

print("""Q 8""")
def minLoan():
    listmin=[]
    for x in EmployeesList:
       if isinstance(x.minLoans(),(float, int)):
           listmin.append(x.minLoans())
    return min(listmin)
print(minLoan())

print("""Q 9""")

def maxLoan():
    listmax=[]
    for x in EmployeesList:
       if isinstance(x.maxLoans(),(float, int)):
           listmax.append(x.maxLoans())
    return max(listmax)
print(maxLoan())

print("""Q 10""")
print()

def printListOfLoans():
    allloans=[]
    totaLoans={}
    for x in EmployeesList:
        for y in x.getLoans():
            allloans.append(y)
        totaLoans[x.getName()]=x.totlaLoans()
    print(allloans)
    print()
    print(totaLoans)
    print()
    print(sum(list(totaLoans.values())))
    print()
printListOfLoans()

print("""Q 11""")

def loanDictionary():
    loanDic={}
    for x in EmployeesList:
        loanDic[x.EmployeeNo]=x.getLoans()
    return loanDic
print(loanDictionary())

print("""Q 12""")
def DicofLoarns():
   loanDic={}
   for x in EmployeesList:
       if not x.getLoans():
           loanDic[x.EmployeeNo]="no loarns"
       else:
        maxLoarn=reduce(lambda a,b: a if a > b else b ,x.getLoans())
        minLoarn=reduce(lambda a,b: a if a < b else b,x.getLoans())
        loanDic[x.EmployeeNo]={"min loan":minLoarn,"max Loarn":maxLoarn}
   return loanDic
print(DicofLoarns())

print("""Q 13""")
def moreThanA ():
    for x in StudentsList:
      for key,value in x.getMark().items():
          if value >=90:
              print ( "name :",x.getName(),"Subject :",x.getSubject(),"the mark :",key,value)
moreThanA()

print("""Q 14""")
def maxEmployessSalary():
    salary=[]
    for x in EmployeesList:
        salary.append(x.getSalary())
    return max(salary)
print(maxEmployessSalary())
print("""Q 15""")
def minEmployessSalary():
    salary=[]
    for x in EmployeesList:
        salary.append(x.getSalary())
    return min(salary)
print(minEmployessSalary())

print("""Q 16""")
def totalEmployessSalary():
    salary=[]
    for x in EmployeesList:
        salary.append(x.getSalary())
    return sum(salary)
print(totalEmployessSalary())

print("""Q 17""")
def delAll():
    global EmployeesList
    global StudentsList
    global Employee1 
    global Employee2
    global Employee3
    global Employee4
    global Student1
    global Student2
    global Student3
    global Student4
    del EmployeesList
    del StudentsList
    del Employee1 
    del Employee2
    del Employee3
    del Employee4
    
    del Student1
    del Student2
    del Student3
    del Student4
    print ("All Was Deletes")
delAll()   
# =============================================================================
#     for item in EmployeesList+StudentsList:
#         del item
# =============================================================================
