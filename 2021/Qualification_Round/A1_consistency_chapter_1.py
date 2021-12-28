"""
CONSISTENCY
자음 중 가장 많은 것으로 바꾸는 경우, 모음 중 가장 많은 것으로 바꾸는 경우
자음 -> 자음 이나 모음 -> 모음 : 2
자음 -> 모음 이나 모음 -> 자음 : 1
"""
from collections import defaultdict

alphabet = [chr(65+i) for i in range(26)]
vowels = ["A", "E", "I", "O", "U"]
consonants = list(set(alphabet) - set(vowels))
vowels_set = set(vowels)
consonants_set = set(consonants)
T = int(input())
for test in range(1, T+1):
    ans, string = 200, input()
    count = defaultdict(int)
    vowel, consonant = 0, 0
    for char in string:
        count[char] += 1
        if char in vowels_set:
            vowel += 1
        else:
            consonant += 1
    # 모음 중 가장 많은 것으로 통일
    temp1 = 0
    max_vowel = 'A'
    for vwl in vowels:
        if count[vwl] > count[max_vowel]:
            max_vowel = vwl
    for char in string:
        if char == max_vowel:
            continue
        if char in vowels_set:
            temp1 += 2
        else:
            temp1 += 1
    # 자음 중 가장 많은 것으로 통일
    temp2 = 0
    max_consonant = 'B'
    for csnt in consonants:
        if count[csnt] > count[max_consonant]:
            max_consonant = csnt
    for char in string:
        if char == max_consonant:
            continue
        if char in consonants_set:
            temp2 += 2
        else:
            temp2 += 1
    # 마무리
    ans = min(ans, temp1, temp2)
    print(f"Case #{test}: {ans}")
