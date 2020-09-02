from dataclasses import dataclass

@dataclass
class Student:
    # fields will take any value of the set datatype
    #seems like you can't initilize a field here without giving it a value when you add data to the class
    name: str
    college_id: int
    gpa: float

def main():
    #example data
    quinn = Student('quinn',123145,4)
    bob = Student('bob',1234565,2.3)
    
    print(quinn)
    print(bob)

main()