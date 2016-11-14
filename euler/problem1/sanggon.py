# 배수 구하는 함수
# def multiple(num, rn):
#     answers = list()
#     idx = 0
#     while True:
#         if idx != 0:
#              += num * idx
#         elif
#         idx += 1
#         answers =
#     return answers


# multiple(3, 1000)
idx = 1
answer = 0
while True:
    print(idx)
    if idx == 1000:
        break
    elif idx % 3 == 0 or idx % 5 == 0:
        print(idx)
        answer += idx
    idx += 1

print("답:", answer)
