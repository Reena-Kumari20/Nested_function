#Write a Python function to sum all the numbers in a list.
"""def sum_of_list(a):
    i=0
    s=0
    while i<len(a):
        s=s+int(a[i])
        i=i+1
    return(str(s))
a=['2','3','4','5','6','7','8']
print(sum_of_list(a))"""

def sum(b):
    s=0
    for x in b:
        s=s+x
    return s
b=[2,3,4,5]
print(sum(b))
