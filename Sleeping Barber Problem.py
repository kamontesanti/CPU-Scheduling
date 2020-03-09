# The Sleeping Barber Problem: A classical process synchronization problem in which we have a certain
# amount of barbers (processor cores/threads) and a certain amount of seats (available resources);
# when a customer (process) requests service from the barber, several different scenarios may ensue ->
# this code is an algorithm to solving the issue of deadlock in a system:

import sys

# get some standard information about the store/system:
print("Please enter the number of seats at store opening: ")
maxSeats = int(input())

numCustomers = 0                                # this is the amount of customers at opening
# ----------------------------------------------------------------------------------------------------

# base class for inheritance, define semaphore data structure:
class Semaphore(object):
    def __init__ (self, value):
        self.val = value                        # number of resources
    
    # method to determine if there are available resources:
    def isAvailable(self):
        if (self.val > 0):
            return True
        else:
            return False
        
    # method to wait if resources are not available:
    def wait(self):
        if (self.val <= 0):
            while(self.val <= 0):
                # simulate a time delay with a for loop, this would naturally be replaced
                # by the barber sleeping, the CPU in idle state:
                for delay in range(0,256):
                    pass
        else:
            print("Resources are available!")
            self.val -= 1                       # decrement the amount of available resources
            
            
    # method to alert that a resource has been freed:
    def signal(self):
        self.val += 1                           # increment the amount of avaiable resources

# ----------------------------------------------------------------------------------------------------          
    
# class for the barbers that inherits from the semaphore ADT class defined above:
class Barbers(Semaphore, object):
    def __init__ (self, number, seats):
        self.numBarbers = Semaphore(number)
        self.numSeats = Semaphore(seats)
        
    # method to check if a barber is avaialable:
    def isBarber(self):
        if (self.numBarbers.isAvailable()):
            print("\nA barber is available.")
            # automatically request service for the customer:
            self.service()
        else:
            print("\nA barber is NOT available at the moment.")
            self.numBarbers.wait()

    # method to request service from the barber:
    def service(self, critical):
        self.numBarbers.wait()                  # call wait() to see if available barbers and allocate if so
        self.task(critical)                     # execute the haircut (critical section)
        self.release()                          # free up barbers once finished
        
    # method to execute the critical section of code from the customer:
    def task(self, critical):
        exec(self.critical)
        
    def release(self):
        self.numBarbers.signal()                # increase the amount of barbers once the process is complete

# -----------------------------------------------------------------------------------------------------

# class for the customers and methods to describe operation with resources: (inherit from barber)
class Customer(Barbers, Semaphore):
    
    #numCustomers += 1                          # upon instantiation, increase amount of customers present
    
    def __init__ (self, number, seats):  
        self.barber = Barbers(number, seats)
        self.critical = "This is the critical section"
        self.numCus = numCustomers  
        self.numCus += 1                        # upon instantiation, increase amount of customers present
    
    # if a barber is available, we must access the barber:
    def runThru(self):
        if (self.barber.isAvailable()):
            self.barber.service(self.critical)
            self.numCus -= 1                    # after execution, decrease number of customers
        
        # if a customer came from a seat, we need to account for this:
        if (self.barber.numSeats.val != maxSeats):
            self.barber.numSeats.val += 1       # take a seat
    
        # if barber is not available and there aren't any available seats, we must leave store:
        elif (not(self.barber.isAvailable()) and (self.barber.numSeats.val <= 0)):
            self.numCus -= 1                    # customer leaves the store
            del self                            # delete the customer (leave store)
            
        else:
            self.barber.numSeats.val -= 1       # take a seat if available
            while(not(self.barber.numBarbers.isAvailable())):
                self.barber.numBarbers.wait()   # wait until a seat is available
                self.barber.service(self.critical)  # get service
            
# -----------------------------------------------------------------------------------------------------

# test the code:
print("\nEnter in the amount of barbers working: ")
customer1 = Customer(int(input()), maxSeats)    # instantiate a customer

# test the system:
print("\nThe number of seats avaiable is:", customer1.barber.numSeats.val, "seats")
print("The number of barbers available is:",customer1.barber.numBarbers.val,"barbers")


        
        
    
    