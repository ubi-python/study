
idx = 1
answer = 0
while True:
    if idx >= 1000:
        break
    elif idx % 3 == 0 or idx % 5 == 0:
        answer += idx
    idx += 1

print("답:", answer)
