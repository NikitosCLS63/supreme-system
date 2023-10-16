import time

def print_story(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)  

story = "Добро пожаловать в игру висилица....."
story_wod = "Смотри не повесься"
print_story(story)
print(" ")
print(" ")
print_story(story_wod)
print(" ")
print(" ")


import random

def print_hangman(lives):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    print(stages[lives])




def select_word():
    words = {
        "яблоко": "Красный фрукт съедобный",
        "банан": "Желтый фрукт, который растет на дереве",
        "вишня": "Маленький красный фрукт с косточкой",
        "дуриан": "Фрукт с сильным запахом",
        "ежевика": "Фрукт сочного черного цвета с маленькими колючками"
    }
    word = random.choice(list(words.keys()))
    question = words[word]
    return word, question
categories = ["животные", "фрукты", "страны"]
#2. Попросите пользователя выбрать категорию перед началом игры:
category = input("Выберите категорию (животные, фрукты, страны): ")
#3. Проверьте, что выбранная категория существует в списке категорий:
if category in categories:
    # Загрузите список слов для выбранной категории
    # Например, если выбрана категория "животные":
    if category == "животные":
        word_list = ["кошка", "собака", "слон"]
    elif category == "фрукты":
        word_list = ["яблоко", "банан", "вишня"]
    elif category == "страны":
        word_list = ["Россия", "США", "Франция"]
else:
    print("Выбранная категория не существует.")
    # Возможно, вы захотите перезапустить игру или попросить пользователя выбрать категорию заново
#4. Выберите случайное слово из списка слов для выбранной категории и продолжайте игру как обычно.
import random
word = random.choice(word_list)

def get_guess():
    guess = input("Введите букву: ")
    return guess.lower()

def update_word(word, guessed_letters):
    updated_word = ""
    for letter in word:
        if letter in guessed_letters:
            updated_word += letter
        else:
            updated_word += "_"
    return updated_word

def play_game():
    while True:
        word, question = select_word()
        guessed_letters = set()
        lives = 6
        score = 0
        

        while True:
            print_hangman(lives)
            print(f"Слово: {update_word(word, guessed_letters)}")
            print(" ")
            print(f"Угаданные буквы: {', '.join(sorted(guessed_letters))}")
            print(f"Вопрос: {question}")
            print(" ")
            print(f"Очки: {score}")

            if "_" not in update_word(word, guessed_letters):
                score += 50
                print("Поздравляю! Вы угадали слово.")
                print(f"Ваш счет: {score}")
                break

            if lives == 0:
                print(f"Игра окончена! Слово было {word}.")
                print(f"Ваш счет: {score}")
                break

            guess = get_guess()

            if guess in guessed_letters:
                print("Вы уже угадали эту букву. Попробуйте еще раз.")
            elif guess in word:
                guessed_letters.add(guess)
                score += 10
                print("Правильная буква!")
            else:
                guessed_letters.add(guess)
                lives -= 1
                print("Неправильная буква!")

        play_again = input("Хотите сыграть еще раз? (да/нет): ")
        if play_again.lower() != "да":
            break

if __name__ == "__main__":
    play_game()

    
    
        
        
