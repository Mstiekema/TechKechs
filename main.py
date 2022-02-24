import sys
input = sys.stdin.readline

inputs = []

while True:
    text = input().strip()
    if text:
        inputs.append(text)
    else:
        break

print(inputs)
