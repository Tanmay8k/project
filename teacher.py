import db
def add_ques():
    print("ADD_QUESTION:")
    question = input("Enter the question: ")
    options = []
    for i in range(1, 5):
        option = input(f"Enter option {i}: ")
        options.append(option)
        ans = input("Enter the correct option number (1-4): ")
        db.add_question(question, options, int(ans) - 1)
        print("Question added successfully.")
        more = input("Do you want to add more questions? (y/n): ")
        if more.lower() != 'y':
            break
def remove_que():
    print("Remove_Questions:")
    number = input("Enter question number: ")
def teachers():
 while True:
  print("\n1. Add Question  2. Remove Question  3. Logout")
  choice = input("Enter code from 1-3: ") 
  if choice == "1":
   add_ques()
  elif choice == "2":
   remove_que()
  elif choice == "3":
   print("Logged out.")
  return
 else:
  print("Invalid choice, try again.")

