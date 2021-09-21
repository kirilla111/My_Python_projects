class MyGame():
    def __init__(self, n):
        self.turns = []
        self.turn = 0
        self.grid_num = n

        for i in range(self.grid_num):
            tmp = []
            for j in range(self.grid_num):
                # 1 - p1, 2- p2, 0 - empty
                tmp.append(0)
            self.turns.append(tmp)

    def is_error(self, i, j):
        # self.show_grid()

        if i > self.grid_num - 1 or j > self.grid_num - 1 or i < 0 or j < 0:
            return True

        if self.turns[i][j] != 0:
            return True
        return False

    # tie - 0, First player win - 1, Second player win - 2, Not over yet - 3 , Error - 4

    def make_new_turn(self, i, j):
        # check for error
        if self.is_error(i, j):
            return 4

        player = 2
        if self.turn % 2 == 0:
            player = 1

        self.turn += 1
        self.turns[i][j] = player
        # self.show_grid()

        # check for gorizontal and vertical lines
        for l in range(self.grid_num):
            gorizontal = 0
            vertical = 0
            for k in range(self.grid_num):
                if self.turns[l][k] == player:
                    gorizontal += 1

                if self.turns[k][l] == player:
                    vertical += 1

            if gorizontal == self.grid_num or vertical == self.grid_num:
                return player

        # check for the first diagonal
        gorizontal = 0
        for l in range(self.grid_num):
            if self.turns[l][l] == player:
                gorizontal += 1
        if gorizontal == self.grid_num:
            return player

        # check for the second diagonal
        gorizontal = 0
        # print(i, n - i - 1)
        for l in range(self.grid_num):
            if self.turns[l][self.grid_num - l - 1] == player:
                gorizontal += 1
        if gorizontal == self.grid_num:
            return player

        if self.turn >= self.grid_num * self.grid_num:
            return 0

        return 3

    def get_turn(self):
        return self.turn

    def show_grid(self):
        for i in range(self.grid_num):
            line = ''
            for j in range(self.grid_num):
                line += '%s ' % self.turns[i][j]
            print(line)

    def restart(self):
        self.turns = []
        self.turn = 0

        for i in range(self.grid_num):
            tmp = []
            for j in range(self.grid_num):
                # 1 - p1, 2- p2, 0 - empty
                tmp.append(0)
            self.turns.append(tmp)
