import datetime
import os

markets_filename = 'markets.txt'
costs_filename = 'costs.txt'

costs_data = []
markets_data = {}
costs_data_header = ''


class MarketCosts(object):
    def __init__(self, market_id, market_name, date, potato_cost, cabbage_cost, onion_cost):
        """Constructor"""
        self.market_id = market_id
        self.market_name = market_name
        self.date = date
        self.potato_cost = potato_cost
        self.cabbage_cost = cabbage_cost
        self.onion_cost = onion_cost


def saveDataToFiles():
    costs = open(costs_filename, 'w', encoding='UTF-8')
    for cost in costs_data:
        line = '{};{};{};{};{};\n'.format(cost.market_id, cost.date.strftime('%d.%m.%Y'), cost.potato_cost,
                                         cost.cabbage_cost, cost.onion_cost)
        costs.write(line)
    costs.close()

    markets = open(markets_filename, 'w', encoding='UTF-8')
    for marketKey in markets_data.keys():
        line = '{};{};\n'.format(marketKey, markets_data[marketKey])
        markets.write(line)
    markets.close()

    print('Данные сохранены!')


def loadDataFromFiles():
    markets = open(markets_filename, 'r', encoding='UTF-8')
    markets_lines = markets.readlines()
    for line in markets_lines:
        market_data = line.split(';')
        markets_data[str(market_data[0])] = market_data[1]

    costs = open(costs_filename, 'r', encoding='UTF-8')
    costs_lines = costs.readlines()
    header = '-----------------------------------------------------------------------------------------\n'
    header += 'Код рынка       Название рынка           Дата              Картошка     Капуста     Лук'
    header += '\n-----------------------------------------------------------------------------------------\n'
    global costs_data_header
    costs_data_header = header

    for line in costs_lines:
        line_data = line.split(';')
        costs_data.append(MarketCosts(line_data[0], markets_data[str(line_data[0])],
                                      datetime.datetime.strptime(line_data[1], '%d.%m.%Y'),
                                      line_data[2], line_data[3], line_data[4]))

    costs.close()


def getCostsTable():
    for cost in costs_data:
        market_formatted_name = cost.market_name.ljust(20)
        print('{}             {}    {}         {}           {}          {}'
              .format(cost.market_id, market_formatted_name, cost.date.date(), cost.potato_cost, cost.cabbage_cost,
                      cost.onion_cost))


def programStartScreen():
    print(costs_data_header)
    getCostsTable()
    waitForCommand()


def addNewCosts(market_id, potato_cost, cabbage_cost, onion_cost):
    costs_data.append(MarketCosts(market_id, markets_data.get(str(market_id)), datetime.datetime.now(), potato_cost, cabbage_cost, onion_cost))
    programStartScreen()


def sortTable():
    global costs_data
    sort_mode = input('0 - сортировка по цене картошки, 1 - капусты, 2 - лука, 3 - номер рынка:\n')
    if sort_mode == '0':
        costs_data = sorted(costs_data, key=lambda cost: cost.potato_cost)
    elif sort_mode == '1':
        costs_data = sorted(costs_data, key=lambda cost: cost.cabbage_cost)
    elif sort_mode == '2':
        costs_data = sorted(costs_data, key=lambda cost: cost.onion_cost)
    elif sort_mode == '3':
        costs_data = sorted(costs_data, key=lambda cost: cost.market_id)


def waitForCommand():
    print('\n0 - открыть таблицу, 1 - добавить новые данные, 2 - сортировка таблицы, 3 - сохранить данные\n4 - выход')
    command_number = input('Введіть номер команди: ')
    if command_number == '0':
        programStartScreen()

    elif command_number == '1':
        market_id = input('Введите код рынка: ')
        if market_id not in markets_data.keys():
            command = input('Рынок с таким кодом отсутствует в базе. 1 - добавить новый, иначе - отменить: ')
            if command is '1':
                markets_data[market_id] = input('Введите имя для нового рынка: ')
            else:
                waitForCommand()

        addNewCosts(market_id, input('Цена на картошку: '), input('Цена на капусту: '),
                    input('Цена на лук: '))
        programStartScreen()

    elif command_number == '2':
        sortTable()
        programStartScreen()
    elif command_number == '3':
        saveDataToFiles()
        waitForCommand()
    elif command_number == '4':
        exit()


if __name__ == '__main__':
    loadDataFromFiles()
    programStartScreen()
