def question_1() -> int:
    sum: int = 0
    for n in range(1000):
        if n % 5 == 0 or n % 3 == 0:
            sum = sum + n
    return sum


def question_1_alt() -> int:
    return sum([i for i in range(1000) if i % 5 == 0 or i % 3 == 0])

print(question_1())
