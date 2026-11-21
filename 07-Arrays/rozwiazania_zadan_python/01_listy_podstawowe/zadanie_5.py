# 4, Zadanie 5
# Polecenie: Napisz program, który sortuje nazwy gier alfabetycznie i wyświetla je z numerami, używając while.
# Sortowanie i numerowanie listy gier za pomocą while

computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

computer_games.sort()

i = 0
while i < len(computer_games):
    print(i + 1, computer_games[i])
    i = i + 1
