import matplotlib.pyplot as plt

def collatz_steps(n):
    s = 1
    while n != 1:
        s += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
    return s

for settings in [('small', 25), ('big', 8000)]:
    interval = range(1, settings[1])
    values = list(map(collatz_steps, interval))
    plt.plot(interval, values, 'ko')
    plt.savefig('collatz_seq_len_' + settings[0] + '.png')

