availabletkt=2
class Movie:
    def __init__(self, names, otp, cost):
        self.names = names
        self.otp = otp
        self.cost = cost


class Ticketbooking:
    # def __init__(self, names, otp, cost):
    #     self.names = names
    #     self.otp = otp
    #     self.cost= cost



    def Bookticket(self):

        # appending instances to list
        # list.append(Movie("amit", 3, 100))
        # list.append(Movie("sai", 13, 200))
        # list.append(Movie("roopam", 33, 300))
        tsum = 0;
        print("Lets Book New Ticket")
        name = input("Enter your Name: ")
        otp = int(input("Enter your OTP: "))
        print("Combos Available:\n200:PopCorn \n300:PopCorn Samosa \n400: Popcorn Samosa Pepsi")
        cost = int(input("Enter your cost: "))
        list.append(Movie(name, otp, cost))

        print("****final records****")
        for obj in list:
            print(obj.names, end=' \t\t\t\t')
            print(obj.otp, end=' \t\t\t\t')
            print(obj.cost, end=' \t\t\t\t')
            print()

        for obj in list:
            # calling method
            # obj.Sum();
            tsum = tsum + obj.cost
        print("Total Amount:", tsum)
    def Removeticket(self ,name , otp):
        # for obj in list:
        #     name = input("Enter your Name/Email Id: ")
        #     otp = int(input("Enter your OTP to be cancelled: "))
        for obj in list:
            if (obj.otp == otp and obj.names == name):
                # del obj
                list.remove(obj)
                print("Record deleted with otp ",obj.otp)
            print("****final records****")
            for obj in list:
                print(obj.names, end=' \t\t\t\t')
                print(obj.otp, end=' \t\t\t\t')
                print(obj.cost, end=' \t\t\t\t')
                print()


list = []
p1 = Ticketbooking()
again='y'
while(again=='y' or again=='Y'):
   if(availabletkt>=1):
     p1.Bookticket()
     availabletkt= availabletkt-1;
     print("tickets available to book", availabletkt)
     again = input("Enter your y for Again: ")
   else:
       print("All tickets are sold for the day !")
       break;

print("Thanks for service ,Njoy Have a great Day")
#p1.Removeticket();


cancel='n'
cancel = input("Enter your y to cancel ticker Any: ")
while(cancel=='y' or cancel=='Y'):
    #cancel='n'

    if(cancel=='y'):
        name = input("Enter your Name/Email Id: ")
        otp = int(input("Enter your OTP to be cancelled: "))
        p1.Removeticket(name,otp)
    print("Thanks Bye")
    cancel = input("Any more Enter your y to cancel ticker Any: ")
print("logging off.....Bye")





