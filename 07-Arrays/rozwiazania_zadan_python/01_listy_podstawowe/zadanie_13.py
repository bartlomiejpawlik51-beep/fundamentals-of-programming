# 4, Zadanie 13
# Polecenie: Napisz program, który sortuje listy za pomocą wbudowanej funkcji sorted(), rosnąco i malejąco.
# Sortowanie list za pomocą wbudowanej funkcji sorted()

distances_traveled = [120, 150, 180, 90, 200, 175, 160]
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
file_names = [
    "report.docx", "presentation.pptx", "data.csv", "photo.jpg",
    "notes.txt", "invoice.pdf", "resume.docx", "budget.xlsx",
    "meeting.mp4", "schedule.pdf"
]

print("Od najmniejszej odległości:", sorted(distances_traveled))
print("Od najwyższej temperatury:", sorted(daily_temperatures, reverse=True))
print("Nazwy plików alfabetycznie:", sorted(file_names))
