player_name=input("Enter your name: ").upper()
print(f"\nHello, {player_name}!! Welcome to the Quiz Game!\n")

quest_dict={
  "Which Indian state is known as the 'Land of Five Rivers'?":{
    "choices":["A. Punjab",
               "B. Haryana",
               "C. Uttar Pradesh",
               "D. Bihar"],
    "answer":"A",
    "Answer":"A. Punjab"
  },
  "Which of the following is the largest ocean in the world?":{
    "choices":["A. Atlantic Ocean",
               "B. Indian Ocean",
               "C. Pacific Ocean",
               "D. Arctic Ocean"],
    "answer":"C",
    "Answer":"C. Pacific Ocean"
  },
  "What is the capital of Brazil?":{
    "choices":["A. Rio de Janeiro",
               "B. Sao paulo",
               "C. Salvador",
               "D. Brasilia"],
    "answer":"D",
    "Answer":"D. Brasilia"
  },
  "What is the smallest country in the world by land area?":{
    "choices":["A. Monaco",
               "B. Vatican City",
               "C. Nauru",
               "D. San Marino"],
    "answer":"B",
    "Answer":"B. Vatican City"
  },
  "Which element is the most abundant in the Earth's atmosphere?":{
    "choices":["A. Carbon dioxide",
               "B. Argon",
               "C. Oxygen",
               "D. Nitrogen"],
    "answer":"D",
    "Answer":"D. Nitrogen"
  },
  "What is the largest planet in our solar system?":{
    "choices":["A. Earth",
               "B. Jupiter",
               "C. Saturn",
               "D. Neptune"],
    "answer":"B",
    "Answer":"B. Jupiter"
  }
}


score=10

question_no=1

questions=list(quest_dict.keys())

for question in questions:
  
  question_info=quest_dict[question]
  choices=question_info["choices"]
  correct_ans=question_info["answer"]
  
  print(f"\n{question_no}. {question}\n") #to display current que.
  for choice in choices: #to display it's choices 
    print(choice)
         
  user_ans=input("\nPlease enter your answer (A,B,C,D): ").upper()
  
  if user_ans==correct_ans:
    print("\n✅ Your answer is correct! 👏")
    print(f"\nHey,{player_name}! Your won Rs.{score}/- 💸")
    
    score*=10
    
    question_no+=1
    
  else:
    print("\n❌ Your answers is incorrect. The correct answer is: ", question_info["Answer"])
    
    
  proceed=input(f"\n{player_name}, Would you like to proceed to the next question? If yes press 'y'/'n' to no: ").lower()
  
  print("\n--------------------------------------------------------------------------------------")
  
  if proceed=="y":
    continue
  if proceed=="n":
    break
    
  else:
    print("\nInvalid input.")    
    proceed=input(f"\nHey, {player_name}! Please enter 'y' to continue or 'n' to quit: ").lower()
    if proceed!="n" or proceed!="y":
      print("\nInvalid input.")
      break
    