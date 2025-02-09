"""Day 2"""
import itertools


"""8kyu -> paperwork"""
# def paperwork(n:int, m:int):
#     if m >0 and n>0 :
#         return n*m
#     else:
#         return 0


"""8kyu -> is_uppercase"""
# def is_uppercase(inp: str) -> bool:
#     return inp.upper() == inp


"""4kyu -> next_biiger """
# def next_bigger(n:int):
#     s = str(n)
#     for i in range(len(s) - 2, -1, -1):
#         if s[i] < s[i + 1]:
#             for k in range(len(s) - 1, i, -1):
#                 if s[i] < s[k]:
#                     return int(s[:i] + s[k] + s[-1:k:-1] + s[i] + s[k-1:i:-1])
#     return -1
# print(next_bigger(414))


"""4kyu -> next_smaller """
# def next_smaller(n: int) -> int:
#     digits = list(str(n))
#     i = len(digits) - 2
#     while i >= 0 and digits[i] <= digits[i + 1]:
#         i -= 1
#     if i == -1:
#         return -1
#     j = len(digits) - 1
#     while digits[j] >= digits[i]:
#         j -= 1
#     digits[i], digits[j] = digits[j], digits[i]
#     digits = digits[:i+1] + sorted(digits[i+1:], reverse=True)
#     result = int("".join(digits))
#     return result if digits[0] != '0' else -1
# print(next_smaller(414))


"""4kyu -> permutations  """
# def permutations(string:str):
#     return list("".join(p) for p in set(itertools.permutations(string)))

# print(permutations("aab"))  # ['aab', 'aba', 'baa']
