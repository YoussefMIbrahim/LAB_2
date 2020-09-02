from dataclasses import dataclass

@dataclass
class Student:
    name: str
    college_id: int
    gpa: float

def main():

    quinn = Student('quinn',123145,4)
    bob = Student('bob',1234565,2.3)
    
    print(quinn)
    print(bob)

main()