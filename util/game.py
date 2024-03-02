class TaijiGame:
    def __init__(self):
        self.board = [[' ' for _ in range(9)] for _ in range(9)]
        self.current_player = 'Light'
        self.light_score = 0
        self.dark_score = 0

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 19)

    def is_valid_move(self, row, col):
        return 0 <= row < 9 and 0 <= col < 9 and self.board[row][col] == ' '

    def place_taijitu(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.update_scores()
            return True
        return False

    def update_scores(self):
        self.light_score = self.calculate_score('Light')
        self.dark_score = self.calculate_score('Dark')

    def calculate_score(self, player):
        max_group_sizes = [0, 0]  # Stores sizes of the two largest groups
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == player:
                    # Check horizontally
                    count = 1
                    for k in range(j + 1, 9):
                        if self.board[i][k] == player:
                            count += 1
                        else:
                            break
                    max_group_sizes[0] = max(max_group_sizes[0], count)
                    # Check vertically
                    count = 1
                    for k in range(i + 1, 9):
                        if self.board[k][j] == player:
                            count += 1
                        else:
                            break
                    max_group_sizes[1] = max(max_group_sizes[1], count)
        return sum(sorted(max_group_sizes, reverse=True)[:2])

    def is_game_over(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def switch_player(self):
        self.current_player = 'Light' if self.current_player == 'Dark' else 'Dark'
