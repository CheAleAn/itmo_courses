#print("введите натуральное число")
a = input()
b = 0
answer = 0
i = 0
while i < len(a):
    if b % 2 ==0:
        answer += int(a[i])
    else:
        answer -= int(a[i])
    b += 1
    i +=1
print(answer)
