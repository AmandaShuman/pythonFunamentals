""" x = 0
while x < 10:
    x = x+1
    if x == 1:
        print("small")
    if x > 2:
        x = x+1
        print("medium")
    if x == 5:
        x = 7
        print("big") """

#code challenge
d = {0: 'a', False: 'b', 1 > 2: 'c', bool([]): 'd'}

print(d[0])

#code displays - d