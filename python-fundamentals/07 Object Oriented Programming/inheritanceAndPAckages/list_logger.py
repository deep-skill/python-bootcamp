PI = 3.1415


class ListLogger(list):

    def __init__(self):
        super().__init__()
        print('Lista creada')

    def append(self, n):
        print('Agregando elemento a lista')
        super().append(n)


list_logger = ListLogger()
list_logger.append(10)
list_logger.append(11)
list_logger.insert(0, 1)
# list_logger.extend([1, 2])
print(list_logger)

