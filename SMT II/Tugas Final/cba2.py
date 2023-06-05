# import random
# import time
# import threading

# class MathGame:
#     def __init__(self):
#         self.score = 0
#         self.lives = 5
#         self.level = 1
#         self.time_limit = 10
#         self.timer_thread = None
#         self.is_timeout = False

#     def start_game(self):
#         print("Math Game - Let's Test Your Math Skills!")
#         print("You have 5 lives. Answer as many questions as you can within the time limit.")
#         print("Press enter to start...")
#         input()

#         while self.lives > 0:
#             print(f"\nLevel {self.level} | Score: {self.score} | Lives: {self.lives}")
#             print("Get ready for the next question...")
#             time.sleep(1)

#             self.is_timeout = False
#             self.start_timer()
#             self.generate_question()
#             user_answer = input("\nYour answer: ")

#             self.is_timeout = True
#             self.timer_thread.join()

#             if user_answer.isdigit():
#                 user_answer = int(user_answer)
#                 if user_answer == self.current_answer:
#                     print("Correct answer!")
#                     self.score += 1
#                     if self.score >= 7:
#                         self.level += 1
#                         self.score = 0
#                 else:
#                     print("Wrong answer!")
#                     self.lives -= 1
#             else:
#                 print("Invalid input!")

#         print("\nGame Over!")
#         print(f"Your final score is: {self.score}")

#     def start_timer(self):
#         self.timer_thread = threading.Thread(target=self.countdown)
#         self.timer_thread.start()

#     # def countdown(self):
#     #     time_left = self.time_limit
#     #     while time_left > 0 and not self.is_timeout:
#     #         print(f"\nTime Left: {time_left} seconds", end="\r")
#     #         time_left -= 1
#     #         time.sleep(1)
#     #     print("\nTime's up!")
#     #     self.lives -= 1

#     def countdown(self):
#         time_left = self.time_limit
#         while time_left > 0 and not self.is_timeout:
#             if time_left > 0:
#                 print(f"\nTime Left: {time_left} seconds", end="\r")
#             time_left -= 1
#             time.sleep(1)
#         print("\nTime's up!")
#         self.lives -= 1

#     def generate_question(self):
#         if self.level == 1:
#             operand1 = random.randint(1, 10)
#             operand2 = random.randint(1, 10)
#         elif self.level == 2:
#             operand1 = random.randint(10, 20)
#             operand2 = random.randint(10, 20)
#         else:
#             operand1 = random.randint(20, 30)
#             operand2 = random.randint(20, 30)

#         operator = random.choice(["+", "-", "*"])
#         self.current_answer = eval(f"{operand1} {operator} {operand2}")
#         print(f"What is {operand1} {operator} {operand2}?\n")

# game = MathGame()
# game.start_game()
import sys
print(sys.executable)