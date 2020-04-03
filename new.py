import can_data_class
import time
import random
print('===========Start==========')
a = can_data_class.can_data(1,2,3,4,5)
#a.print_data()

#a = can_data_class.can_data(11,12,13,14,15)
a.print_data()
i=0
while i<1:
    i=0
    #a = can_data_class.can_data(random.randrange(0, 3), random.randrange(0, 8), random.randrange(0,50), random.randrange(0, 50), random.randrange(0, 50))
    #a.print_data()
    a = [1,2,3,4,5]
    for b in range(len(a)):
        print(a[b])
    time.sleep(0.5)