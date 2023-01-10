# Python3 code here for creating class
class geeks:
    def __init__(self, names, otp, cost):
        self.names = names
        self.otp = otp
        self.cost= cost


    def Sum(self):
        print(self.name + self.otp)

        # calling the destructor

    def __del__(self):
        print("Object gets destroyed");


# creating list
list = []

# appending instances to list
list.append(geeks("amit", 3, 100))
list.append(geeks("sai", 13, 200))
list.append(geeks("roopam", 33, 300))
tsum = 0;
for obj in list:
    # calling method
    # obj.Sum();
    tsum = tsum + obj.cost
print(tsum)
for obj in list:
    print(obj.names, end=' \t')
    print(obj.otp)

# We can also access instances method
# as list[0].Sum() , list[1].Sum() and so on.
list.append(geeks(22, 33, 400))
print("***********Final records************")
for obj in list:
    print(obj.names, end=' \t')
    print(obj.otp, end=' \t')
    print(obj.cost, end=' \t')
    print()
for obj in list:
    if(obj.otp==13 and obj.names==12):
        #del obj
        list.remove(obj)
    print()
print("****final records****")
for obj in list:
    print(obj.names, end=' \t')
    print(obj.otp, end=' \t')
    print(obj.cost, end=' \t')
    print()


#iterative entries
for i in range(2):
    name = input("Enter your Name: ")
    otp = input("Enter your OTP: ")
    print("Combos Available:\n 200:PopCorn \n300:PopCorn Samosa \n 400: Popcorn Samosa Pepsi")
    cost = input("Enter your cost: ")


    list.append(geeks(name, otp, cost))

print("****final records****")
for obj in list:
    print(obj.names, end=' \t')
    print(obj.otp, end=' \t')
    print(obj.cost, end=' \t')
    print()