"""модуль для роботи з файлами первинних даних
- зчитування та вивід на екран
"""

"""модуль зчитує первинні файли для обробки
"""

def get_clients():
    """повертає список клієнтів b з файла `dovidnik.txt`
    Returns:
        clients_list: список клієнтів
    """

    with open("./data/dovidnik.txt") as clients_file:
        from_file = clients_file.readlines()

    clients_list = []
    for line in from_file:
        line_list = line.split(';')
        clients_list.append(line_list)

    return clients_list


def get_orders():
    """повертає список накладних
    Returns:
        from_file: список накладних
    """
    
    with open('./data/orders.txt') as orders_file:
        from_file = orders_file.readlines()

    
    # розбити строку на реквізити та перетворити формати (при потребі)
    
    # список-накопичувач
    orders_list = []    
    
    for line in from_file:
        line_list = line.split(';')
        line_list[3] = int(line_list[3])
        line_list[4] = float(line_list[4])
        orders_list.append(line_list)

    return orders_list


def show_clients(clients):
    """виводить список клієнтів по заданому інтервалу кодів
    Args:
        clients (list): список клієнтів
    """

    # задати інтервал виводу
    client_code_from = input("З якого кода клієнта? ")
    client_code_to   = input("По який кода клієнта? ")

    lines_found = 0

    for client in clients:
        if client_code_from <= client[0] <= client_code_to:
            print ("код: {:5} назва: {:15} адреса: {:25}".format(*client))
            lines_found += 1

    if lines_found == 0:
        print("Клієнтів по Вашому запиту не знайдено") 


def show_orders(orders):
    """
    Args:
        orders (list): 
    """

    for order in orders:
        print("код клієнта: {:3} накладна № {:4} товар: {:20} кількість: {:3} ціна: {:7}"
            .format(order[0], order[1], order[2], order[3], order[4]))

# clients = get_clients()
# show_clients(clients)

# orders= get_orders()
# show_orders(orders)