from random import randint

k = input()
file = open("random" + k + ".txt")
line = file.readline()
numbers = list(map(int, line.split()))

freq = [0 for _ in range(7)]
p = 0
for n in numbers:
    freq[n] += 1

    r = randint(1,6) 
    if n != r:
        p += (n-r)**3

print("Numbers: ", len(numbers), ", sum: ", sum(numbers), ", (N*3.5) = ", len(numbers)*3.5, ", penalty: ", p)
print(freq[1:7])
