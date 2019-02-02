import re

# todo: привести коментарии к правильному виду


# функция проверяет слово на длинну и содержимое
def check_word_len(word):
    if len(word) > 0 and word != " ":
        return True
    else:
        return False


# функция убирает лишние символы в слове
def clear_word(word):
    # todo: какие еще артефакты могут быть в слове?
    # todo: убрать слова, состоящие не из букв
    # todo: убрать слова, включающие знак '
    pure_word = re.sub('[!@#$",.?;]', '', word)
    pure_word = pure_word.lower()
    if check_word_len(pure_word):
        if pure_word.endswith("'"):
            pure_word = pure_word[:-1]
        if pure_word.startswith("'"):
            pure_word = pure_word[1:]
    return pure_word


# функция, очищающая слова в массиве
def clear_word_list(word_list):
    pure_word_list = []
    for word in word_list:
        pure_word = clear_word(word)
        if check_word_len(pure_word):
            pure_word_list.append(pure_word)
    pure_word_list = sorted(list(set(pure_word_list)))
    return pure_word_list


# функция, создающая массив уникальных слов из текста
def create_word_list_from(text):
    clear_text = text.replace("\n", " ").replace("\t", " ")
    result_list = clear_text.split(" ")
    return result_list


# функция, создающая стоку из слов массива, каждое слово с новой строки
def make_string_from(word_list):
    result_string = ""
    for item in word_list:
        result_string += item + "\n"
    return result_string


# читаем содержимое файла в переменную
# todo: вынести параметр наружу
books_text = open("Spider-man_3-Stan_Lee.txt", "r").read()
famous_words = open("famous_words.txt", "r").read()
my_dictionary = open("my_dictionary.txt", "r").read()

# todo: сделать, так чтобы необходимый результат возвращала одна функция
books_text_list = clear_word_list(create_word_list_from(books_text))
famous_words_list = clear_word_list(create_word_list_from(famous_words))
my_dictionary_list = clear_word_list(create_word_list_from(books_text))

new_words_set = set(books_text_list)
new_words_set ^= set(famous_words_list)
new_words_set ^= set(my_dictionary_list)

word_string = make_string_from(list(new_words_set))

new_words = open('new_words.txt', 'w')
new_words.write(word_string)
new_words.close()
