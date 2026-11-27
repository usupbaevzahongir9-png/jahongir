import random
import matplotlib.pyplot as plt
def create_pole():
    pole = [[random.randint(0, 1) for j in range(10)] for i in range(10)]
    return pole
def print_pole(pole):
    for i in range(len(pole)):
        for j in range(len(pole[i])):
            print(pole[i][j], end=' ')
        print()
def count_neighbors(pole, i, j):
    sosedi = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue
            ni = i + di
            nj = j + dj
            if 0 <= ni < len(pole) and 0 <= nj < len(pole[i]):
                if pole[ni][nj] == 1:
                    sosedi += 1
    return sosedi
def next_generation(pole):
    new_pole = []
    for i in range(len(pole)):
        row = []
        for j in range(len(pole[i])):
            sosedi = count_neighbors(pole, i, j)
            if pole[i][j] == 0 and sosedi == 3:
                cell = 1
            elif pole[i][j] == 1 and (sosedi < 2 or sosedi > 3):
                cell = 0
            else:
                cell = pole[i][j]
            row.append(cell)
        new_pole.append(row)
    return new_pole
def main():
    pole = create_pole()
    for i in range(10):
        print("takt:", i + 1)
        print_pole(pole)
        plt.imshow(pole, cmap="binary")
        plt.title("Поколение " + str(i + 1))
        plt.show()
        pole = next_generation(pole)
main()
