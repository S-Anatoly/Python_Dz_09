class TicTacToeBoard:
    def __init__(self):
        self.field = []
        self.coord = []
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

    def new_game(self):  # созданиe новой игры;
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

    def get_field(self):  # получениe поля (список списков);
        return self.field

    def check_field(self):  # проверкa, есть ли победитель, который возвращает X, если победил первый игрок,
        if self.win == 'Победила дружба!':  # 0, если второй, D, если ничья и None, если можно продолжать игру;
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
            return 'GAME OVER'
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
            self.coord = ((self.field[0][0], self.field[0][1], self.field[0][2]),
                          (self.field[1][0], self.field[1][1], self.field[1][2]),
                          (self.field[2][0], self.field[2][1], self.field[2][2]),
                          (self.field[0][0], self.field[1][0], self.field[2][0]),
                          (self.field[0][1], self.field[1][1], self.field[2][1]),
                          (self.field[0][2], self.field[1][2], self.field[2][2]),
                          (self.field[0][0], self.field[1][1], self.field[2][2]),
                          (self.field[0][2], self.field[1][1], self.field[2][0]))
            for (x, y, z) in self.coord:
                if x == y == z and x != '-':
                    self.end_of_game = True
                    self.win = x
                    return f'Победил - {x}'
                elif self.field[0].count('-') == 0 and self.field[1].count('-') == 0 and self.field[2].count('-') == 0:
                    self.end_of_game = True
                    self.win = 'Победила дружба!'
                    return 'Победила дружба!'
                else:
                    print(f'Играем дальше{x,y,z}')


board = TicTacToeBoard()

print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(2, 3))
print(board.make_move(3, 2))

print(*board.get_field(), sep="\n")
