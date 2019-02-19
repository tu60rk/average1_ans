total = 0
count =0
numbers = []

while True:
    try:
        line = input()
        if line:
            number = int(line)
            total += number
            count += 1
            numbers += [int(line)]
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break

if count:
    print("numbers: ", numbers,)
    print("count =", count, "max =", max(numbers), "min =", min(numbers), "total =", total, "mean =", total / count)
