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
def strcounter(s): # решение за N
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items():
        print(sym, count)
strcounter('aabbbbccd')

word = "Hello World"
letter_count = {}
for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
for letter, count in letter_count.items():
    print(f"{letter}: {count}")