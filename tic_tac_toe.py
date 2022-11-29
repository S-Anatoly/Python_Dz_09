class TicTacToeBoard:
    def __init__(self):
        self.field = []
        for row in range(3):
            r = []
            for col in range(3):
                r.append('-')
            self.field.append(r)
        self.move_x = True
        self.end_of_game = False
        self.winner = None
        self.win = ''
        self.first_move = True

    def new_game(self):  # – для создания новой игры;
        self.field = []
        for row in range(3):
            r = []
            for col in range(3):
                r.append('-')
                self.field.append(r)
        self.move_x = True
        self.end_of_game = False
        self.winner = None
        self.win = ''
        self.first_move = True

    def get_field(self):  # – для получения поля (список списков);
        return self.field

    def check_field(self):  # – для проверки, есть ли победитель, который возвращает X, если победил первый игрок,
        if self.win == 'ничья':  # 0, если второй, D, если ничья и None, если можно продолжать игру;
            return 'D'
        elif self.win == 'X':
            return 'X'
        elif self.win == '0':
            return 0
        else:
            return None

    # make_move устанавливает значение текущего хода в ячейку поля с координатами row, col,
    #  если это возможно, «переключает» ход игрока,
    #  а также возвращает сообщение «Победил игрок X» при победе крестиков,
    #  «Победил игрок 0» при победе ноликов, «Ничья» в случае ничьей и «Продолжаем играть»,
    #  если победитель после данного хода неопределён.

    def make_move(self, row, col):
        if self.end_of_game and not self.first_move:
            return 'Игра завершена'
        else:
            if self.field[row - 1][col - 1] != '-':
                return f'Клетка {row},{col} занята!'
            else:
                if self.move_x:
                    self.field[row - 1][col - 1] = 'X'
                    self.move_x = False
                    self.first_move = False
                else:
                    self.field[row - 1][col - 1] = '0'
                    self.move_x = True
                    self.first_move = False

                for j in range(len(self.field)):
                    for i in range(len(self.field)):
                        if self.field[i].count(self.field[i][j]) == 3 and self.field[i][j] != '-':
                            self.end_of_game = True
                            self.win = self.field[i][j]
                            return f'Победил игрок {self.field[i][j]}'
                        elif self.field[0].count('-') == 3 and self.field[1].count('-') == 3 and self.field[2].count('-') == 3:
                            self.end_of_game = True
                            self.win = 'ничья'
                            return 'ничья'
                        else:
                            return 'Продолжаем играть'


board = TicTacToeBoard()

print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")

