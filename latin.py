import random


def shuffle_array(array):
    for i in range(len(array) - 1, 0, -1):
        j = random.randint(0, i)
        array[i], array[j] = array[j], array[i]


def generate_square(size):
    square = [[0] * size for _ in range(size)]

    # Remplir la première ligne avec des nombres consécutifs
    for i in range(size):
        square[0][i] = i + 1

    # Mélanger la première ligne de manière aléatoire
    shuffle_array(square[0])

    # Générer les lignes suivantes
    for i in range(1, size):
        for j in range(size):
            square[i][j] = square[i - 1][(j + 1) % size]

    return square


def main():
    size = int(input("Taille du carré latin: "))
    square = generate_square(size)

    # Afficher le carré latin généré
    for row in square:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
