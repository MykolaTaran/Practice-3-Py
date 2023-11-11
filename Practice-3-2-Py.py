
def is_palindrome(s):
    # Перетворення стрічки в нижній регістр і видалення пробілів
    s = s.lower().replace(" ", "")

    # Порівняння оригінальної стрічки з її зворотнім варіантом
    return s == s[::-1]

# Приклад використання
word = "Boring"
if is_palindrome(word):
    print(f"{word} є паліндромом.")
else:
    print(f"{word} не є паліндромом.")
