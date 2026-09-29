import db
ques=db.get_questions()
def start():
 name = input("Enter your name: ")
 print("Start Quiz selected") 
 ques = db.get_questions()
 if not ques:
  print("No ques available.")
  return
 score = 0
 for number, q in enumerate(ques, start=1):
  print(f"\nQuestion {number}: {q['question']}")
  for i, option in enumerate(q['options'], start=1):
   print(f"{i}. {option}")
  answer = input("Enter your answer (1-4): ")
  if answer.isdigit() and 1 <= int(answer) <= 4:
   if int(answer) - 1 == q['answer']:
    score += 1
    print("Correct ans")
   else:
    print("Wrong ans:")
  else:
   print("Invalid input. Please enter a number between 1 and 4.")
 print(f"\n{name}, your score: {score}/{len(ques)}")
 db.save_score(name, score, len(ques))
def view_scores():
  print("My Scores selected")
  scores = db.get_scores()
  name = input("Enter your name: ").strip()
  found = False
  for player, score, total, played_at in scores:
   if player == name:
    print(f"{score}/{total}  ({played_at})")
   found = True
  if not found:
   print(f"No scores found for {name}.")
def student():
    while True:
     print("\n1. Start Quiz  2. My Scores  3. Logout")
     choice = input("Enter code from 1-3: ")
        
     if choice == "1":
        start()
     elif choice == "2":
          view_scores()
     elif choice == "3":
            print("Logged out.")
            return
    else:
          print("Invalid choice, try again.")