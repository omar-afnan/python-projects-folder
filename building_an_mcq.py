class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

Questions_to_answer = [
    """Which of the following is the primary purpose of an algorithm?
    a) To store data
    b) To solve a problem
    c) To manage memory
    d) To format output""",
    
    """Which of the following data structures follows the Last In, First Out (LIFO) principle?
    a) Queue
    b) Stack
    c) Array
    d) Linked List""",
    
    """What does the acronym CPU stand for?
    a) Central Processing Unit
    b) Central Program Unit
    c) Computer Processing Unit
    d) Central Processor Unit""",
    
    """In which layer of the OSI model does routing occur?
    a) Physical Layer
    b) Data Link Layer
    c) Network Layer
    d) Transport Layer""",
    
    """What is the main function of an operating system?
    a) To compile programs
    b) To manage hardware resources
    c) To provide internet access
    d) To run applications""",
    
    """Which of the following is NOT a type of software?
    a) Operating System
    b) Database
    c) Processor
    d) Application Program"""
]

questions = [
    Question(Questions_to_answer[0], "b"),
    Question(Questions_to_answer[1], "b"),
    Question(Questions_to_answer[2], "a"),
    Question(Questions_to_answer[3], "c"),
    Question(Questions_to_answer[4], "b"),
    Question(Questions_to_answer[5], "c")
]

def test(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        answer = input("Your answer: ").strip().lower()
        if answer == question.answer:
            score += 1
    print(f"You have got {score} out of {len(questions)}")

# Run the quiz
test(questions)
