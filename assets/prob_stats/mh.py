from random import randint

N = 100000

def mh():
    treasure = randint(0,2)
    guess = randint(0,2)

    # smart
    if treasure == guess:
        smart = 0
    else:
        smart = 1 

    # stay
    if treasure == guess:
        stay = 1
    else:
        stay = 0

    return (smart, stay)


smart_success = 0
stay_success = 0
for i in range(N):
    r_smart, r_stay = mh()
    smart_success += r_smart
    stay_success += r_stay

print("Smart: ", smart_success, "/", N)
print("Stay: ", stay_success, "/", N)
