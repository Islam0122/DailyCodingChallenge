""" Day -> 1 """

""" 8-kyu -> reverse """
# def reverse(st:str):
#     return " ".join(st.split()[::-1])
# print(reverse("Hello World"))  # -> World Hello


""" 5-kyu -> pig_it """
# def pig_it(text:str):
#     return " ".join(word[1:] + word[0] + "ay" if word.isalpha() else word for word in text.split())

# print(pig_it('Pig latin is cool'))  # igPay atinlay siay oolcay


""" 4-kyu -> top_3_words """
# import re
# import collections

# def top_3_words(text: str):
#     words = re.findall(r"[a-zA-Z']+", text)  # Ищем слова с апострофами
#     words = [word.lower() for word in words if any(char.isalpha() for char in word)]  # Фильтруем пустые апострофы

#     return [word for word, _ in collections.Counter(words).most_common(3)]  # Берем топ-3

# print(top_3_words("//wont won't won't"))  # ['won't', 'wont']


