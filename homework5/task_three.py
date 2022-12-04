with open('text.txt') as text_txt:
    song = text_txt.read()
    user_letter = input("Enter any english letter: ")
    song.lower()
    quantity = song.count(user_letter)
    print(f"Результат: буква встречается {quantity} раз")
