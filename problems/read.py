import random
import time

def ques1():
    name = input("Enter your name: ")
    return name

def ques2():
    while True:
        num1 = random.randint(1, 100)
        num2 = int(input(f"What is the square of {num1}? "))

        if num2 == -1:
            return False

        if num1**2 == num2:
            print("You're right")
            return True
        else:
            print("You're wrong")
            return False

def perfect_square_number(min_value, max_value):
    num = random.randint(int(min_value * 0.5), int(max_value * 0.5))
    return num * num

def ques3():
    while True:
        num1 = perfect_square_number(1, 100)
        num2 = int(input(f"What is the square root of {num1}? "))

        if num2 == -1:
            return False

        if num1**0.5 == num2:
            print("You're right")
            return True
        else:
            print("You're wrong")
            return False

def main():
    name = ques1()
    correct_ans = 0
    exc = 5

    questions = [ques2,ques3]

    while True:
        selected_question = random.choice(questions)
        if selected_question():
            correct_ans+=1

        for i in range(exc):
            print("!",end=" ")    
        exc -= 1
        ans = str(input("\nDo you want to continue (yes/no) : ").strip().lower())

        if ans == 'no':
            break

    time.sleep(5)        
    
    print(f"{name}, YOU'RE A WINNER!" if correct_ans >= 2 else f"{name}, YOU'RE A LOSER")
    print("Your Score : ")
    for i in range(correct_ans):
        time.sleep(1)
        print("!" ,end=" ")


main()
