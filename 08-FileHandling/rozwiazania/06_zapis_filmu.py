# ZADANIE 6: Zapisanie danych o filmie do pliku tekstowego.

# Zmienne przechowują informacje o filmie.
movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"

file_name = "movie_details.txt"

# Otwieramy plik w trybie zapisu.
# Tryb "w" tworzy nowy plik lub nadpisuje istniejący.
with open(file_name, "w", encoding="utf-8") as file:
    file.write("Movie Title: " + movie_title + "\n")
    file.write("Director: " + director + "\n")
    file.write("Lead Actor: " + lead_actor + "\n")

print("Dane filmu zapisano w pliku", file_name)
