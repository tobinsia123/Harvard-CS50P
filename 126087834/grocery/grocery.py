dict = {}
while True:
    try:
        grocery = input()
        if grocery in dict:
            dict_val = dict[grocery] + 1
            dict[grocery] = dict_val
        else:
            dict[grocery] = 1
    except EOFError:
        print()
        for i in sorted(dict):
            key = i.upper()
            value = dict[i]
            print(f'{value} {key}')
        break

