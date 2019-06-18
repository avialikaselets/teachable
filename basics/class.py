class calc:
    def add(x, y):
        answer = x + y
        print(answer)
        answer = answer * 2
        return answer

    def sub(x, y):
        answer = x - y
        print(answer)
        answer = answer + 120
        return answer

    def mult(x, y):
        answer = x * y
        print(answer)
        answer = answer / 3
        return answer

    def div(x, y):
        answer = x / y
        print(answer)
        answer = answer - 45
        return answer

print(calc.div(100,16))
