sentence = input("Введіть речення: ")

words = sentence.split()  # Розбиваємо речення на окремі слова

print("Слова, які починаються на 'як':")
for word in words:
    if word.startswith("як") or word.startswith("Як"):
        print(word)