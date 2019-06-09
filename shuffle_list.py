from random import randrange

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numbers before: {numbers}")


def shuffle_list(l):
    shuffled = []
    original = l[:]
    for _ in range(0, len(original)):
        shuffled.append(original.pop(randrange(0, len(original))))
    return shuffled


print(f"Shuffled: {shuffle_list(numbers)}")
print(f"Numbers after: {numbers}")
