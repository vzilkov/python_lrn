class can_data:
    def __init__(self):
        self.can_data_dict = {'id': [], 'length': [], 'data': []}

    def clear(self):
        self.can_data_dict.clear()
        self.can_data_dict = {'id': [], 'length': [], 'data': []}



    def append_can_buf(self, id, length, *data):
        if id in self.can_data_dict['id']:
            index = self.can_data_dict['id'].index(id)
            self.can_data_dict['id'][index] = id
            self.can_data_dict['length'][index] = length
            self.can_data_dict['data'][index] = data

        else:
            self.can_data_dict['id'].append(id)
            self.can_data_dict['length'].append(length)
            self.can_data_dict['data'].append(data)

    def print_data(self):
        import tabulate
        import platform
        import os
        system = platform.system()
        if system == 'Linux':
            os.system('clear')
        elif system == 'Windows':
            os.system('cls')
        '''for i in range(len(self.can_data_dict['id'])):
            print(self.can_data_dict['id'][i], self.can_data_dict['length'][i], self.can_data_dict['data'][i])''' 
        print(tabulate.tabulate(self.can_data_dict, headers='keys', tablefmt='grid'))

    def read_data(self):
        import random
        can_data_dict = {'id': random.randrange(0,4), 'length': random.randrange(0,8), 
        'data': 
        [random.randrange(0,10),random.randrange(0,10),random.randrange(0,10),random.randrange(0,10),
        random.randrange(0,10),random.randrange(0,10),random.randrange(0,10),random.randrange(0,10)]}
        self.append_can_buf(can_data_dict['id'],can_data_dict['length'],can_data_dict['data'])
