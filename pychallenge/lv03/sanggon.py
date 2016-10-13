import re

mess = ''
with open('lv3_question.txt') as infile:
    for line in infile:
        mess += line

results = re.findall('[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]', mess)

print(results)

# TODO 결과 리스트의 아이템을 꺼내서 가운데 문자를 뽑아내도록 해야 된다.
# results.

# 정답 : linkedlist
