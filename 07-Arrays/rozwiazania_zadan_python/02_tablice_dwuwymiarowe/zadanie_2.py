# 4, Zadanie 2 - Tablice dwuwymiarowe
# Polecenie: Napisz program, który wyświetla planszę do gry w kółko i krzyżyk w układzie 3 na 3.
# Wyświetlanie planszy do gry w kółko i krzyżyk

tic_tac_toe_board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]

for row in tic_tac_toe_board:
    for element in row:
        print(element, end=" ")
    print()
