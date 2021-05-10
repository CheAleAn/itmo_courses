n = int(input())
p = int(input())
with open('data.txt') as file:
    input_data = file.readline()

input_data = input_data.strip('\n')
input_data = input_data.strip(' ')
data = []
for i in input_data.split():
    data.append(i)
numbers = list(map(int, data))
out2 = list(map(lambda a: a ** p, numbers))
out1 = list(filter(lambda a: a % n == 0, numbers))
str1 = ' '.join(list(map(str, out1)))
str2 = ' '.join(list(map(str, out2)))
with open('out-1.txt', 'w') as file:
    file.write(str1)
with open('out-2.txt', 'w') as file:
    file.write(str2)
