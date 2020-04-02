import can_data_class
a = can_data_class.can_data(1,2,3,4,5)
a.print_data()

Dict = {'id': 1, 'length': 2, 'data': [3,4,5,6,7,8,9,10]}
#print(Dict)
mass = [Dict]
b = {'id': 11, 'length': 12, 'data': [3,4,5,6,7,8,9,10]}
mass.append(b)

a = can_data_class.can_data(11,12,13,14,15)
a.print_data()