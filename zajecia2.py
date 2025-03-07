#Zadanie 1
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_selector(numbers: list[int]) -> list[int]:
    return [num for num in numbers if is_prime(num)]
#Zadanie 2
def round_numbers(numbers: list[int], threshold: int) -> list[int]:
    rounded = []
    for num in numbers:
        if num < threshold:
            rounded.append((num // 10) * 10)         
        else:
            rounded.append(((num + 9) // 10) * 10)
    return rounded
#Zadanie 3
def longest_increasing_subsequence(sequence: list[int]) -> int:
    if not sequence:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length
#Zadanie 4
def is_balanced(expression: str) -> bool:
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in brackets.values(): 
            stack.append(char)
        elif char in brackets: 
            if not stack or stack.pop() != brackets[char]:
                return False

    return not stack 
#Zadanie 5
def transposition_cipher(text: str, key: int) -> str:
    if key > len(text):
        return text

    text_list = list(text)

    for i in range(0, len(text_list) - key + 1, key):
        text_list[i], text_list[i + key - 1] = text_list[i + key - 1], text_list[i]

    return ''.join(text_list)
#Zadanie 6
def fibonacci_generator(n: int):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1
#Zadanie 7
from collections import Counter

def most_frequent_element(data: list):
    counter = Counter(data)
    return counter.most_common(1)[0][0]
#Zadanie 8
import re

def count_syllables(word: str) -> int:
    return len(re.findall(r'[aeiouyAEIOUY]', word))

def readability_score(text: str) -> float:
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    words = text.split()
    
    avg_words_per_sentence = len(words) / len(sentences)
    avg_syllables_per_word = sum(count_syllables(word) for word in words) / len(words)
    
    return avg_words_per_sentence + avg_syllables_per_word
#Zadanie 9
from itertools import permutations

def unique_permutations(elements: list):
    unique_perms = set(permutations(elements))
    return [list(perm) for perm in unique_perms]
#Zadanie 10
def group_words_by_length(words: list[str]) -> dict:
    grouped = {}
    for word in words:
        length = len(word)
        if length not in grouped:
            grouped[length] = []
        grouped[length].append(word)
    return grouped