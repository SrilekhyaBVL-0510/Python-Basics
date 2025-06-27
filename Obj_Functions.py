from Student import StudentClass
from Student import Chef

# student1 = StudentClass("gokul","ECE",8.9,False)
# student2 = StudentClass("siri","CSE",8.9,False)

# if student1.on_Honor_roll():
#     print(student1.name+" is on honor roll\n")

# myChef = Chef()
# myChef.make_Biryani()

#inheritance
class ChineseChef(Chef):
    def make_friedRice(self):
        print("Chinese Chef makes fried rice")
    def make_Biryani(self):
        print("Chinese Chef makes Mutton Biryani")

myChineseChef = ChineseChef()
myChineseChef.make_Biryani()
myChineseChef.make_paneer()