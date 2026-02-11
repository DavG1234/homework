import random
def random_length ():
    return random.randint(1,100)

def make_list(size):
    a = []
    for _ in range (size):
        a.append(random.randint(0,9))
    return a


file = open("numbers.txt","w")
file.write(str(make_list(random_length())))
file.close()
