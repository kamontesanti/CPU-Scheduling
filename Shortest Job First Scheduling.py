# code to generate the shortest-job-first (SJF) CPU Scheduling algorithm:

# using a standard, mock PCB class:
import operator
class Process:
    def __init__ (self, burstTime, waitTime):
        self.burst = burstTime              # burst time attribute
        self.wait = waitTime                # wait time attribute
        
# with a standard queue class for the ready queue:
class Queue(Process):                       # inherits from Process class

    # custom constructor:
    def __init__(self):
        self.items = []
        self.time = 0                          # local variable for wait time
        self.totalTime = 0
    
    # method to determine if the queue is empty:
    def isEmpty(self):
        if self.items == []:
            print("The queue is empty.")
        else:
            print("The queue is not empty.")
    
    # method to add an item at the end of the queue:
    def enqueue(self,item):
        self.items.sort(key=operator.attrgetter('burst'))
        self.items.insert((len(self.items)),item)
        
    # method to pop out a value of the queue:
    def dequeue(self,item):
        self.items.pop(item)
    
    # output the size of the queue:
    def size(self):
        return len(self.items)
    
    # print out each process burst time:
    def printBurst(self):
        print("Burst Time: \n")
        for elem in range(0, len(self.items)):
            print(self.items[elem].burst, "ms")
    
    # print out each element of the queue:
    def printQueue(self):
        for items in self.items:
            print(items)
            
    def calcWait(self):
        # calculate and override the wait times for each process:
        for elem in range(1, len(self.items)):
            self.time += (self.items[elem - 1].burst)
            self.items[elem].wait = self.time
            
        for value in range(1, len(self.items)):
            self.totalTime += (self.items[value].wait)
            
        return (self.totalTime) / (len(self.items))
    
# instantiate the arbitrary processes with burst time and cleared wait time:
P1 = Process(8, 0)                          
P2 = Process(10, 0)
P3 = Process(1, 0)
P4 = Process(4, 0)
P5 = Process(12, 0)

# instantiate a ready queue for the processes:
readyQ = Queue()

# allocate processes to the ready queue:
readyQ.enqueue(P1)
readyQ.enqueue(P2)
readyQ.enqueue(P3)
readyQ.enqueue(P4)
readyQ.enqueue(P5)

# print out the list of processes to confirmt he sorting by shortest job:
readyQ.printBurst()

