from random import randint


class Game:

    def __init__(self):
        self.choices = "Rock", "Paper", "Scissors"
        self.player_wins = 0
        self.computer_wins = 0
        self.draw = 0

    def get_user_item(self):
        while True:
            try:
                option = int(input('Choose an option between Rock (1), Paper (2), Scissors (3): '))

                if 1 <= option <= 3:
                    break
                else:
                    print('You can only enter a number between 1 and 3.')
            except ValueError:
                print('The value entered is invalid. You can only enter numeric values.')

        return option

    def get_computer_item(self):

        return randint(1, 3)

    def get_game_result(self):
        if self.player_wins == self.computer_wins:
            return 'Draw.'
        elif self.player_wins > self.computer_wins:
            return 'You won the set.'
        else:
            return 'Computer wins the set.'

        # if user_item == computer_item:
        #     return "Draw"
        # elif user_item == "r":
        #     if computer_item == "p":
        #         return "You lose"
        #     elif computer_item == "s":
        #         return "You win"
        # elif user_item == "p":
        #     if computer_item == "r":
        #         return "You win"
        #     elif computer_item == "s":
        #         return "You lose"
        # elif user_item == "s":
        #     if computer_item == "r":
        #         return "You lose"
        #     elif computer_item == "p":
        #         return "You win"

    def play(self):
        for i in range(5):
            player = self.get_user_item()
            computer = self.get_computer_item()
            print(f"You chose {self.choices[player - 1]}.")
            print(f"The computer chose {self.choices[computer - 1]}.")

            if player == computer:
                print('You drew!\n')
                self.draw += 1
            elif (player - computer) % 3 == 1:
                print('You won.\n')
                self.player_wins += 1
            else:
                print('You lost.\n')
                self.computer_wins += 1

            print(self.get_game_result())


    # def get_user_menu_choice(self):
    #     while True:
    #         try:
    #             print('Welcome to Rock , Paper , Scissors')
    #             print('-' * 10, '\n')
    #             print('1. Play a new game')
    #             print('2. Show scores')
    #             print('3. Quit')
    #             choice = int(input('\nEnter an option: '))
    #         except ValueError:
    #             print('The value entered is invalid. You can only enter numeric values.')
    #
    #         if choice == 1:
    #
    #             self.play()
    #             break
    #         elif choice == 2:
    #
    #
    #         elif choice == 3:
    #             exit()
    #         else:
    #             print("You have entered a number that isn't in the list.")


start = Game()
start.play()
