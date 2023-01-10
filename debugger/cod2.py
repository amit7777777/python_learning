import pdb


def multiply(a, b):
    answer = float(a) * float(b)
    return answer

pdb.set_trace()
x = input("Enter first number : ")
y = input("Enter second number : ")
result = multiply(x, y)
print(result)
