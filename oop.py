# class Microwave:
#     def __init__(self, brand: str, power_range: str) -> None:
#         self.brand = brand
#         self.power_range = power_range
#         self.turned_on: bool = False

#     def turn_on(self) -> None:
#         if self.turned_on:
#             print(f'the {self.brand} microwave is already turned on')

#         else:
#             self.turned_on = True
#             print(f'the {self.brand} is turned on')

#     def turn_off(self) -> None:
#         if self.turned_on:
#             self.turned_on = False

#             print(f'The {self.brand} is turned off')

#         else:
#             print(f'The {self.brand} microwave is turning off')

#     def run(self, seconds: int) -> None:
#         if self.turned_on:
#             print(f'The {self.brand} is running for {seconds}s')

#         else:
#             print("A wheezing sound... turn on the microwave fisrt")

# huawei = Microwave(brand='huawei', power_range= 'D')

# huawei.turn_on()
# huawei.turn_on()
# huawei.run(35)

import random

choices = ('r', 'p', 's')
emoji = {
    'r': 'D',
    'p': 'H',
    's': 'X'
}

while True:
    user_choice = input('Rock, paper, scissors? (r/p/s): ')

    if user_choice not in choices:
        print("Invalid choice!")

        continue

    computer_choice = random.choice(choices)

    print(f'You chose {emoji[user_choice]}')
    print(f'computer chose {emoji[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie!')

    elif ((user_choice == 'r' and computer_choice == 's' or 
        user_choice == 'p' and computer_choice == 'r' or 
        user_choice == 's' and computer_choice == 'p')):
        print('You won')

    else:
        print('You lose')

        should_continue = input('to continue? (y/n): ')

        if should_continue == 'n':
            break

