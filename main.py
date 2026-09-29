print("welcome to the Quiz portal")
import db
from teacher import teachers
from student import student
def t():
 db.init_db()
while True:
   print("\n 1.Teacher ,2.Student , 3.EXIT")
   choice= input ("Enter choice:")
   if choice == "1":
    teachers()
   elif choice =="2":
    student()
   elif choice =="3":
    print("thank you for coming ")
    break
   else:
    print("INVALID CHOICES PLEASE SELECT FROM 1-3")
if __name__=="__main__":
 t()
 