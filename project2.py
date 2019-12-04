from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as tkst
import json

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
        return {"EmployeeNo":self.EmployeeNo,
              "Name":self.getName(),
              "Address":self.getAddress(),
              "Salary":self.getSalary(),
              "JobTitle":self.getJobTitle(),
              "Loans":self.getLoans(),
              "totlaLoans":self.totlaLoans()}
       
        
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
        return {"Student_Number":self.Student_Number,
              "Name":self.getName(),
              "Address":self.getAddress(),
              "Subject":self.getSubject(),
              "Marks":self.getMark(),
              "AVG":self.getavg()}
         
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

root = Tk()
screen_width=root.winfo_screenwidth()/2
screen_height=root.winfo_screenheight()/2
root.geometry("400x150+"+str(int(screen_width-300/2))+"+"+str(int(screen_height-150/2)) )
root.title('Project 2')

def notdone():
    messagebox.showinfo('Not implemented', 'Not yet available')

def _about():
    messagebox.showinfo('About us', 'Coding Academy Orange JO')

def Add_Employee():
    def Add_Employee_submit ():
        global EmployeesList
        list_loans=[int (i) for i in loans.get().split(",") ]
        state_Add=0
        for value in  EmployeesList:
            if value.EmployeeNo == int(EmNo.get()):
                state_Add=1
        if not state_Add:
            Employee1= Employee(int(EmNo.get()),Name.get(),Address.get(),int(Salary.get()),JobTilte.get(),list_loans)
            EmployeesList.append(Employee1)
            print(EmployeesList)
            messagebox.showinfo("Add Employee", "Successful Add")
        else:
            messagebox.showinfo("Add Employee", "Wrong Number check agane")
            
    add_em_sc = Toplevel(root)
    add_em_sc.title("Add Employees")
    add_em_sc.geometry("250x150+400+400")
    EmNo= StringVar()
    Name= StringVar()
    Address=StringVar()
    Salary=StringVar()
    JobTilte=StringVar()
    loans=StringVar()
    employee1 = Label(add_em_sc, text = "Employee Number").grid(row=0, column = 0)
    e1 = Entry(add_em_sc, textvariable= EmNo).grid(row = 0, column =1)
    employee2 = Label(add_em_sc, text = "Employee Name").grid(row=1, column = 0)
    e2 = Entry(add_em_sc, textvariable= Name).grid(row = 1, column =1)
    employees3 = Label(add_em_sc, text = "Employee Address").grid(row=2, column = 0)
    e3= Entry(add_em_sc, textvariable=Address).grid(row = 2, column =1)
    employees4 = Label(add_em_sc, text = "Employee Salary").grid(row=3, column = 0)
    e4= Entry(add_em_sc, textvariable=Salary).grid(row = 3, column =1)
    employees5 = Label(add_em_sc, text = "Employee JobTilte ").grid(row=4, column = 0)
    e5= Entry(add_em_sc, textvariable=JobTilte).grid(row = 4, column =1)
    employees6 = Label(add_em_sc, text = "Employee loans").grid(row=5, column = 0)
    e6= Entry(add_em_sc, textvariable=loans).grid(row = 5, column =1)
    submit = Button(add_em_sc, text="Add", command= Add_Employee_submit).grid(row = 7, column = 0)


def Add_Student():
    def Add_Student_submit ():
        global StudentsList
        e=json.loads(Mark.get())
        state_Add=0
        for i,value in enumerate (StudentsList):
            if value.Student_Number == int(Student_Number.get()):
                state_Add=1
        if not state_Add:
            Student1= Student(int(Student_Number.get()),Name.get(),Address.get(),Subject.get(),e)
            StudentsList.append(Student1)
            print(StudentsList)
            messagebox.showinfo("Add Students", "Successful Add")
        else:
            messagebox.showinfo("Add Students", "Wrong Number check agane")
    add_st_sc = Toplevel(root)
    add_st_sc.title("Add_Student")
    add_st_sc.geometry("250x150+400+400")
    Student_Number= StringVar()
    Name= StringVar()
    Address=StringVar()
    Subject=StringVar()
    Mark=StringVar()
    Student1=Label(add_st_sc, text = "Student_Number").grid(row=0, column = 0)
    e1=Entry(add_st_sc, textvariable= Student_Number).grid(row = 0, column =1)
    Student2=Label(add_st_sc, text = "Student_Name").grid(row=1, column = 0)
    e2=Entry(add_st_sc, textvariable= Name).grid(row = 1, column =1)
    Student3=Label(add_st_sc, text = "Student_Address").grid(row=2, column = 0)
    e3=Entry(add_st_sc, textvariable=Address).grid(row = 2, column =1)
    Student4=Label(add_st_sc, text = "Subject").grid(row=3, column = 0)
    e4=Entry(add_st_sc, textvariable=Subject).grid(row = 3, column =1)
    Student5=Label(add_st_sc, text = "Student_Mark").grid(row=4, column = 0)
    e5=Entry(add_st_sc, textvariable=Mark).grid(row = 4, column =1)
    submit = Button(add_st_sc, text="Add", command=Add_Student_submit).grid(row = 7, column = 0)
    
def view_Employee():
    
   global EmployeesList
   view_em_sc = Toplevel(root)
   view_em_sc.title("View Employees")
   view_em_sc.geometry("600x600+"+str(int((screen_width-300)/4))+"+"+str(int((screen_height-150)/4)) )
   frame1 = Frame(master = view_em_sc,bg = 'red')
   frame1.pack(fill='both', expand='yes')
   textArea = tkst.ScrolledText(
    master = frame1,
    wrap   = WORD,
    width  = 200,
    height = 100)
   textArea.pack(padx=10, pady=10, fill=BOTH, expand=True)
   for item in EmployeesList:
       ls = item.infoEmployee()
       print (ls)
       for key,value in ls.items():
           textArea.insert(END,key)
           textArea.insert(END," : ")
           textArea.insert(END,value)
           textArea.insert(END,"   ")
       textArea.insert(END,"\n\n")



def view_Student():
   global StudentsList
   view_em_sc = Toplevel(root)
   view_em_sc.title("View Student")
   view_em_sc.geometry("600x600+"+str(int((screen_width-300)/4))+"+"+str(int((screen_height-150)/4)) )
   frame1 = Frame(master = view_em_sc,bg = 'red')
   frame1.pack(fill='both', expand='yes')
   textArea = tkst.ScrolledText(
    master = frame1,
    wrap   = WORD,
    width  = 200,
    height = 100)
   textArea.pack(padx=10, pady=10, fill=BOTH, expand=True)
   for item in StudentsList:
       ls = item.infoStudent()
       print (ls)
       for key,value in ls.items():
           textArea.insert(END,key)
           textArea.insert(END," : ")
           textArea.insert(END,value)
           textArea.insert(END,"   ")
       textArea.insert(END,"\n\n")   
       
       
def del_Employees():
   
    def delete_emp_fn ():
        global EmployeesList
        state_del = 0 
        for i,value in enumerate (EmployeesList):
            if value.EmployeeNo == int(number.get()):
                state_del=1
                del EmployeesList[i]
                print ("sta",state_del)
        if state_del:
            z = messagebox.showinfo("Delete Employee", "Successful Deleted")
            print(EmployeesList)
            if z == "ok":
              del_em_sc.destroy()
        else:
              z=messagebox.showinfo("Delete Employee", "Wrong Number check agane")
        
    del_em_sc = Toplevel(root)
    del_em_sc.title("Delete Employees")
    del_em_sc.geometry("200x100+400+400") 
    number = StringVar()
    employees_num = Label(del_em_sc, text = "Employee Number").grid(row=0, column = 0)
    e1 = Entry(del_em_sc, textvariable= number).grid(row = 0, column =1)
    submit = Button(del_em_sc, text="Delete", command= delete_emp_fn).grid(row = 4, column = 0)

def del_Students():
   
    def delete_stu_fn ():
        global StudentsList
        state_del = 0 
        for i,value in enumerate (StudentsList):
            if value.Student_Number == int(number.get()):
                state_del=1
                del StudentsList[i]
                print ("sta",state_del)
        if state_del:
          z = messagebox.showinfo("Delete Students", "Successful Deleted")
          if z == "ok":
            del_Stu_sc.destroy()
        else:
            messagebox.showinfo("Delete Students" "Wrong Number check agane")
        
    del_Stu_sc = Toplevel(root)
    del_Stu_sc.title("Delete Students")
    del_Stu_sc.geometry("200x100+400+400") 
    number = StringVar()
    Students_num = Label(del_Stu_sc, text = "Student Number").grid(row=0, column = 0)
    e1 = Entry(del_Stu_sc, textvariable= number).grid(row = 0, column =1)
    submit = Button(del_Stu_sc, text="Delete", command=delete_stu_fn).grid(row = 4, column = 0)

def get_total_emp():
    print("Total Number of Employees is ",len(EmployeesList))
    return "Total Number of Employees is "+str(len(EmployeesList))
def get_total_std():
    print("Total Number of Students is ",len(EmployeesList))
    return "Total Number of Students is "+str(len(StudentsList))
def hiesistStudentAvg():
    listMax=[]
    for x in StudentsList:
        listMax.append(x.getavg())
    return "hiesistStudentAvg "+str(max(listMax))
def minLoan():
    listmin=[]
    for x in EmployeesList:
       if isinstance(x.minLoans(),(float, int)):
           listmin.append(x.minLoans())
    return "Minimum loran cross all "+str(min(listmin))
def maxLoan():
    listmax=[]
    for x in EmployeesList:
       if isinstance(x.maxLoans(),(float, int)):
           listmax.append(x.maxLoans())
    return "Maximum loran cross all "+str(max(listmax))
def maxEmployessSalary():
    salary=[]
    for x in EmployeesList:
        salary.append(x.getSalary())
    return "Maximum Employees Salary is "+str(max(salary))
print(maxEmployessSalary())

def minEmployessSalary():
    salary=[]
    for x in EmployeesList:
        salary.append(x.getSalary())
    return "Minimum Employees Salary "+str(min(salary))

def report():
    report_sc = Toplevel(root)
    report_sc.title("reports")
    report_sc.geometry("400x400+400+400")   
    
    number = StringVar()    
    report1 = Label(report_sc, font=("Helvetica", 16),text = get_total_emp(),padx=10,pady=10).grid(row=0, column = 0)
    report2=  Label(report_sc, font=("Helvetica", 16),text = get_total_std(),padx=10,pady=10).grid(row=1, column = 0)
    report3 = Label(report_sc, font=("Helvetica", 16),text = hiesistStudentAvg(),padx=10,pady=10).grid(row=2, column = 0)
    report4 = Label(report_sc, font=("Helvetica", 16),text =  minLoan(),padx=10,pady=10).grid(row=3, column = 0)
    report5 = Label(report_sc, font=("Helvetica", 16),text =  maxLoan(),padx=10,pady=10).grid(row=4, column = 0)
    report6 = Label(report_sc, font=("Helvetica", 16), text =  minEmployessSalary(),padx=10,pady=10).grid(row=4, column = 0)
    report7 = Label(report_sc, font=("Helvetica", 16),text =  maxEmployessSalary(),padx=10,pady=10).grid(row=4, column = 0)
label=tk.Label(root,text="Project 2",font=('times',20,'bold'),padx=10,pady=10)
label.pack()
top = Menu(root)
root.config(menu=top)
file = Menu(top,tearoff=0)
file.add_command(label='Reports', command=report)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)
top.add_cascade(label='File', menu=file)

Employees = Menu(top,tearoff= 0)
Employees.add_command(label='Add', command=Add_Employee)
Employees.add_command(label='View', command=view_Employee)
Employees.add_command(label='Delete', command=del_Employees)
top.add_cascade(label='Employees', menu=Employees)

Students = Menu(top,tearoff= 0)
Students.add_command(label='Add', command=Add_Student)
Students.add_command(label='View', command=view_Student)
Students.add_command(label='Delete', command=del_Students)
top.add_cascade(label='Students', menu=Students)

Help = Menu(top,tearoff= 0)
Help.add_command(label='About', command=_about)
top.add_cascade(label='Help', menu=Help)
root.mainloop()




