from math import pi

accuracy  = 1000000 # higher = more accurate, but slower

D = 3
Pi = 1
symbol = "s"
for i in range(accuracy):
    if symbol == "s":

        Pi = Pi - (1 / D)
        D = D + 2
        symbol = "a"

    if symbol == "a":

        Pi = Pi + (1/D)
        D = D + 2
        symbol = "s"

print("The code got:", Pi * 4)

print( "The actual pi:", pi)