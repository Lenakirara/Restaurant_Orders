import csv
from collections import Counter


# manipulação de arquivo
# https://app.betrybe.com/course/computer-science/introducao-a-python/entrada-e-saida-de-dados/105dc022-72fa-425f-a452-29b3595bb64d/conteudos/9a69f5d2-dd9d-4831-bea0-bb2f7251cc3b/manipulacao-de-arquivos/6afdd9ae-a6cc-4242-a274-d99295cf2fae?use_case=side_bar
# manipulando arquivo csv:
# https://app.betrybe.com/course/computer-science/introducao-a-python/entrada-e-saida-de-dados/105dc022-72fa-425f-a452-29b3595bb64d/conteudos/9a69f5d2-dd9d-4831-bea0-bb2f7251cc3b/manipulando-arquivos-csv/acbfc282-4ea3-4391-aa85-77f9784efdd2?use_case=side_bar
def get_orders_csv_file(path_file):
    with open(path_file) as file_csv:
        reader = csv.reader(file_csv, delimiter=",", quotechar='"')
        # buscamos as informações de cada pedido / linha
        orders_result = [row for row in reader]
    return orders_result


# https://towardsdatascience.com/comprehending-the-concept-of-comprehensions-in-python-c9dafce5111#:~:text=A%20set%20comprehension%20is%20similar,brackets%20to%20create%20a%20set.&text=The%20list%20includes%20a%20lot,with%20only%20a%20single%20letter.
def maria_favorite_dish(orders):
    # https://pythonacademy.com.br/blog/list-comprehensions-no-python
    # https://stackabuse.com/list-comprehensions-in-python/
    maria_orders = [order[1] for order in orders if order[0] == "maria"]
    # usando counter: elementos armazenados como chaves de dicionário
    # https://docs.python.org/3/library/collections.html#collections.Counter
    # o list() => Estava dando erro:
    # "TypeError: 'dict_keys' object is not subscriptable"
    # https://stackoverflow.com/questions/26394748/nltk-python-error-typeerror-dict-keys-object-is-not-subscriptable
    # colocando posição [0] para vir apenas o primeiro elemento mais pedido.
    # do contrario virá mais de um ex: ['hamburguer', 'pizza']
    maria_fav_order = list(Counter(maria_orders))[0]
    return maria_fav_order


def arnaldo_most_ordered_hamburger(orders):
    most_order = [order[1] for order in orders if order[0] == "arnaldo"]
    return most_order.count("hamburguer")
    # https://stackoverflow.com/questions/9447986/typeerror-count-takes-exactly-one-argument


# http://neci-python.blogspot.com/p/blog-page_99.html
# https://www.pythonforbeginners.com/basics/set-comprehension-in-python
def joao_dishes_never_order(orders, joao_orders):
    not_orders = {order[1] for order in orders if order[1] not in joao_orders}
    return not_orders


def days_joao_never_goes(days, joao_days):
    never_goes = {day[2] for day in days if day[2] not in joao_days}
    return never_goes


def analyze_log(path_to_file):
    orders_data = get_orders_csv_file(path_to_file)
    maria_fav_dish = maria_favorite_dish(orders_data)
    arnaldo_hamburger = arnaldo_most_ordered_hamburger(orders_data)
    joao_not_order = joao_dishes_never_order(orders_data, 'hamburguer')
    never_goes = days_joao_never_goes(orders_data, 'terça-feira')
    # gravar no arquivo mkt_campaign.txt
    with open("data/mkt_campaign.txt", "w") as file_txt:
        file_txt.write(f"{maria_fav_dish}\n")
        file_txt.write(f"{arnaldo_hamburger}\n")
        file_txt.write(f"{joao_not_order}\n")
        file_txt.write(f"{never_goes}\n")


if __name__ == "__main__":
    # print(get_orders_csv_file('data/orders_1.csv'))
    print(analyze_log("data/orders_1.csv"))

    # orders = [
    #     ["maria", "hamburguer", "terça-feira"],
    #     ["maria", "pizza", "terça-feira"],
    #     ["maria", "pizza", "terça-feira"],
    #     ["maria", "hamburguer", "terça-feira"],
    #     ["maria", "hamburguer", "terça-feira"],
    # ]
    # print(maria_favorite_dish(orders))

    # hamburger = [
    #     ["arnaldo", "hamburguer", "terça-feira"],
    #     ["maria", "pizza", "terça-feira"],
    #     ["arnaldo", "pizza", "terça-feira"],
    #     ["maria", "hamburguer", "terça-feira"],
    # ]
    # print(arnaldo_most_ordered_hamburger(hamburger))

    # order = [
    #     ["arnaldo", "hamburguer", "terça-feira"],
    #     ["maria", "pizza", "terça-feira"],
    #     ["maria", "coxinha", "terça-feira"],
    #     ["maria", "misto-quente", "terça-feira"],
    #     ["joao", "hamburguer", "terça-feira"],
    #     ["joao", "hamburguer", "terça-feira"],
    # ]
    # print(joao_dishes_never_order(order, 'hamburguer'))

    # days = [
    #     ["joao", "hamburguer", "terça-feira"],
    #     ["joao", "hamburguer", "quarta-feira"],
    #     ["joao", "hamburguer", "domingo"],
    #     ["maria", "misto-quente", "sabado"],
    # ]
    # print(days_joao_never_goes(days, 'domingo'))
