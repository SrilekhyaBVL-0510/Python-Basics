class StudentClass:
    def __init__(self,name,major,gpa,isOnProbation):#initialise function
        self.name = name
        self.major = major
        self.gpa = gpa
        self.isOnProbation = isOnProbation
    
    #function inside the class
    def on_Honor_roll(self):
        if self.gpa > 6.5:
            return True
        else:
            return False
        
class Chef:
    def make_chicken(self):
        print("Chef can cook chicken")
    def make_paneer(self):
        print("Chef can cook paneer") 
    def make_Biryani(self):
        print("Chef can cook Biryani")  