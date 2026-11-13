# Zadanie 6.17: Konwersja czasu z formatu 24-godzinnego na 12-godzinny

time = input("Enter time (24-hour format HH:MM): ")
parts = time.split(":")  # split() dzieli tekst na części w miejscu dwukropka
hour = int(parts[0])
minute = int(parts[1])

if hour == 0:
    hour12 = 12
    period = "AM"
elif hour < 12:
    hour12 = hour
    period = "AM"
elif hour == 12:
    hour12 = 12
    period = "PM"
else:
    hour12 = hour - 12
    period = "PM"

print(f"Time in 12-hour format: {hour12:02d}:{minute:02d} {period}")
