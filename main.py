from util.game import TaijiGame
from util.players import TaijiAI, ComputerAI

def main():
    game = TaijiGame()
    ai = TaijiAI('Dark')  # AI player will play as 'Dark'
    computer = ComputerAI('Light')  # Computer player will play as 'Light'

    while not game.is_game_over():
        game.print_board()
        if game.current_player == ai.player:
            print("AI's turn:")
            row, col = ai.get_move(game)
        elif game.current_player == computer.player:
            print("Computer's turn:")
            row, col = computer.get_move(game)
        else:
            print("Your turn (Light):")
            row = int(input("Enter row (0-8): "))
            col = int(input("Enter column (0-8): "))

        if game.place_taijitu(row, col):
            print("\nMove accepted!\n")
        else:
            print("\nInvalid move! Try again.\n")

        game.switch_player()

    game.print_board()
    print("Game Over!")
    print("Light Player's score:", game.light_score)
    print("Dark Player's score:", game.dark_score)
    if game.light_score > game.dark_score:
        print("Light Player wins!")
    elif game.light_score < game.dark_score:
        print("Dark Player wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
