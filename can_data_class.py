class can_data:
    can_data_massive = []

    def __init__(self, id, length, *data):
        can_data_dict = {'id': id, 'length': length, 'data': data}
        if not any(can_dict['id'] == can_data_dict['id'] for can_dict in self.can_data_massive):
            print('new element in massive!')
            self.append_can_buf(can_data_dict)
        else:
            print('There is no new element in massive')
            can_dict['length']

    def print_data(self):
        print("*******Class can_data printing...")
        print(*self.can_data_massive, sep='\n')

    def clear(self):
        self.can_data_massive.clear()

    def append_can_buf(self, buf):
        self.can_data_massive.append(buf)

    def append_can_data(self, id, length, *data):
        can_data_dict = {'id': id, 'length': length, 'data': data}
        self.append_can_buf(can_data_dict)