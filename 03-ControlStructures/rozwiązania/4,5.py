# Zadanie 4.5: Szyfr Cezara -- przesunięcie o jedną literę

plain_text = "The early bird catches the worm"
encrypted_text = ""

for char in plain_text:
    if char >= "a" and char <= "y":
        new_char = chr(ord(char) + 1)  # ord() zamienia znak na kod, chr() zamienia kod na znak
    elif char == "z":
        new_char = "a"
    elif char >= "A" and char <= "Y":
        new_char = chr(ord(char) + 1)
    elif char == "Z":
        new_char = "A"
    else:
        new_char = char

    encrypted_text = encrypted_text + new_char

print("Original text:", plain_text)
print("Encrypted text:", encrypted_text)
