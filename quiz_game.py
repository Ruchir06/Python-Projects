questions = ("How many elements are there in the periodic table", 
             "Which animal lays the largest egg", 
             "What is the most abundant gas in the Earth's atmosphere", 
             "How many bones are there in human body", 
             "How many planets are in the solar system" )       
             

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Eagle", "B. Penguin", "C. Ostrich", "D. Whale Shark"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 205", "C. 208", "D. 210"),
    ("A. 7", "B. 8", "C. 9", "D. 10")
)

answers = ("C", "D", "A", "A", "B")
option = 0
score = 0
question = 0

for question in range(len(questions)):
    print("------------------------")
    print(questions[question])

    for option in options[question]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()

    if guess == answers[question]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print(f"The correct answer is {answers[question]}")