strg = "jc"
c = 0
def is_equal(i,j):
    global c
    c += 1
    return i == j
def str_counter(data):
    for i in set(data):
        counter = 0
        for  j in data:
            if is_equal(i,j):
                counter+=1
        print(f"{i}:{counter}")
str_counter(strg)
print(c)