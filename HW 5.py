def a1():
    a = input()
    f = input()
    try:
        f = int(f) + int(a)
    except:
        f = f + a
    print(f)

