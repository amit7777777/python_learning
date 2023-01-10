list = []

# Create List of list
# rangefori=2;
# rangeforj=3;
# for i in range(rangefori):
#     list.append([])
#     for j in range(rangeforj):
#         list[i].append(j)



class MovieTicket:
  list = [];
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def Bookticket(self):
    print("Tickets got booked by " + self.name)
    print("Age who booked ticket is " + self.age)

  def somework(self):
    rangefori = 1;#No of customers
    rangeforj = 3; #Only 3 records for every customers needed name OTP cost
    for i in range(rangefori):
      list.append([])
      for j in range(rangeforj):
        list.append([])
        name = input("Enter your Name: ")
        list[i].append(name)
        otp = input("Enter your OTP: ")
        list[i].append(otp)
        cost = int(input("Enter your cost: "))
        list[i].append(cost)
        print(i)
        print(j)
        if j==rangeforj-1 :
            break;

  def someworkadd(self):
    sum_cost=0;
    rangefori = 1;#No of customers
    rangeforj = 3; #Only 3 records for every customers needed
    for i in range(rangefori):
     # list.append([])
      #for j in range(rangeforj):
        #list[i].append(j)
        sum_cost=sum_cost+(list[i][2]);
        print(list[i][2])
    print("total expenses:")
    print(sum_cost)
p1 = MovieTicket("John","36")
p1.Bookticket()
p1.somework();
p1.someworkadd();
print(list)
