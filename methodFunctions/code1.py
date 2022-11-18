class Weight():
   weight = 100
   # Defining a method
   def to_pounds(self,weight):      #  A method always requires ‘self‘ as the first argument.
      print("method called")
      return 2.205 * self.weight

# Defining a function
def to_pounds(kilos):
   print("Function called")
   return 2.205 * kilos

# Calling a method on an object.
w = Weight()     # object creation is here...
pounds = w.to_pounds(15)


# Calling a function on an object
kilos = 100
pounds = to_pounds(kilos)