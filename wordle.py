import random

# Список слов. Можно добавить больше слов для разнообразия
word_list = ["яблоко", "груша", "банан", "вишня", "апельсин", "виноград", "лимон"]

def choose_word():
    return random.choice(word_list)

def display_word(secret_word, guessed_letters):
    displayed_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def check_guess(secret_word, guess):
    result = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            result.append("🟩")  # Правильная буква на правильном месте
        elif guess[i] in secret_word:
            result.append("🟨")  # Правильная буква на неправильном месте
        else:
            result.append("⬜")  # Неправильная буква
    return result

def wordle_game():
    secret_word = choose_word()
    attempts = 6
    guessed_letters = []

    print("Добро пожаловать в игру Wordle!")
    print("Угадайте 6-буквенное слово. У вас 6 попыток.")

    while attempts > 0:
        print("\nУ вас осталось попыток:", attempts)
        print("Слово:", display_word(secret_word, guessed_letters))

        guess = input("Введите ваше предположение (6 букв): ").lower()

        if len(guess) != len(secret_word):
            print("Пожалуйста, введите слово из 6 букв.")
            continue

        guessed_letters.extend(guess)

        result = check_guess(secret_word, guess)
        print("Результат:", " ".join(result))

        if guess == secret_word:
            print("Поздравляем! Вы угадали слово:", secret_word)
            break

        attempts -= 1

    if attempts == 0:
        print("Вы не угадали. Загаданное слово было:", secret_word)

if __name__ == "__main__":
    wordle_game()