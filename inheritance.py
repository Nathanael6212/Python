class employee:
    raise_amt=1.04 # defult
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+"."+last+ "@gmail.com"
        self.pay=pay
        
    def full_name(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amt)
        
class developer(employee):
    pass #to increase pay raise in only developers we can add raise_amt=1.1... here

    def __init__(self, first, last, pay,program_lang):
        super().__init__(first, last, pay)  #or we can say employee.__init__(.....)
        self.program_lang=program_lang
        
class manager(employee):
    def __init__(self, first, last, pay,employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emp(self):
        for emp in self.employees:
            print(f">>>  {emp.full_name()}")         

em1=developer("natty","tamirat",400000,"phyton")
em2=developer("brooks","ina",500000,"java")
mang1=manager("natnael","tamirat",700000,[em2])
print(em1.pay)
em1.apply_raise()
print(em1.pay)
print(em1.program_lang)
mang1.print_emp()
print(mang1.email)
print(isinstance(mang1, developer ))
print(issubclass(developer, employee))
 
 
