# ZADANIE 10: Tworzenie listy zakupów z danych wpisywanych z klawiatury.

shopping_list = "shopping_list.txt"


def add_product(file_name, product_name):
    """Dopisuje nazwę produktu na końcu pliku.

    file_name - nazwa pliku z listą zakupów,
    product_name - nazwa produktu wpisana przez użytkownika.
    """
    # Tryb "a" dopisuje dane na końcu pliku.
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(product_name + "\n")


product = ""

# Pętla działa do momentu wpisania przez użytkownika 0.
while product != "0":
    product = input("Podaj produkt (0 kończy): ")

    if product == "0":
        break
    else:
        # Wywołujemy funkcję, która zapisuje produkt.
        add_product(shopping_list, product)

print("Lista zakupów została zapisana.")
