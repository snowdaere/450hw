# the three errors are:
# 1. k is not incremented, so stop condition can't be met. add k += 1 after s += 1/k
# 2. k < m should be k <= m, because summations are inclusive
# 3. given the function 1/n, you can't start from k = 0, but that's more of a design issue than a bug
# -> I'm not sure what the third error is. I've checked the original code against every online calculator I could find
# -> as well as by hand, but I haven't found any discrepancies between the outputs or gotten any errors.

s = 0; k = 1; M=3
while k <= M:
    s += 1/k
    k += 1
print(s)
