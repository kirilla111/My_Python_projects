import time
import random

from Basics.MyGame import MyGame


class GenerateDatasets:
    # def __init__(self):

    # n - nums of rows to generate
    def generate(self, n: int, filename: str, size: int):
        game = MyGame(size)
        # self.filename = filename
        dataset = open(filename, "w+")

        # print(b.make_new_turn(0,1))
        data = ''

        while n > 0:
            n -= 1
            a = random.randint(0, size - 1)
            b = random.randint(0, size - 1)

            while (result := game.make_new_turn(a, b)) not in range(0, 3):
                if result != 4:
                    data += '%s,%s,' % (a, b)
                    # data += '%s,' % b
                a = random.randint(0, size - 1)
                b = random.randint(0, size - 1)

            data += '%s,%s,' % (a, b)
            # data += '%s,' % b

            if game.get_turn() < size * size:
                data += '0,' * (size * size - game.get_turn()) * 2

            data += '%s \n' % result
            game.restart()
            # time.sleep(1)

        print(data)
        dataset.write(data)
        dataset.close()
        return data
