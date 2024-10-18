class student():
    """STUDENT CLASS"""    
    # def __init__(self):
    #     pass
    def __init__(self):
        pass
    
    a = 5
    
    # try:
    def display_int(self):
        print(f"a: {self.a}")
    # except SyntaxError:
    #     print("Syntax Error: display_int() missing colones")
    # def display_name(self):
    #     print(f"Student: {self.name}")
        
class department(student):
    
    
    def __init__(self):
        self.a = 6
    
    # def display_student_name(self):
        
    #     print(f"Department: {self.name}")
        
s1 = student()
s1.display_int()
d1 = department()
# d1.a = 6
d1.display_int()
s1.display_int()
# d1 = department()
# d1.