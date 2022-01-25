C = -60; dC = 2
while C <= 60:
    F = (9.0/5)*C + 32
    print(C, F)
    C = C + dC

# the first error is the indentation of the print statement, which should be to the left one tab
# I'm guessing that, since there is no halting condition, that C += dC should have been under the while statement