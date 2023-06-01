def recurs(count):
    print(count)
    if count == 7:return None
    recurs(count + 1)
    print(count)

recurs(4)