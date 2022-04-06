import csv
from collections import Counter


def get_orders_csv_file(path_file):
    with open(path_file) as file_csv:
        reader = csv.reader(file_csv, delimiter=",", quotechar='"')
        # buscamos as informações de cada pedido / linha
        orders_result = [row for row in reader]
    return orders_result


def maria_favorite_dish(orders):
    # https://pythonacademy.com.br/blog/list-comprehensions-no-python
    # https://stackabuse.com/list-comprehensions-in-python/
    maria_orders = [order[1] for order in orders if order[0] == "maria"]
    # [0][0] => para não vir: ex: ['hamburguer', 3]
    maria_fav_order = Counter(maria_orders).most_common()[0][0]
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

    # Teste pedidos Maria:
    # orders = [
    #     ["maria", "hamburguer", "terça-feira"],
    #     ["maria", "hamburguer", "terça-feira"],
    #     ["maria", "pizza", "terça-feira"],
    #     ["maria", "pizza", "terça-feira"],
    #     ["maria", "hamburguer", "terça-feira"]
    # ]
    # print(maria_favorite_dish(orders))

    # Teste quantidade hamburger pedido por Arnaldo
    # hamburger = [
    #     ["arnaldo", "hamburguer", "terça-feira"],
    #     ["maria", "pizza", "terça-feira"],
    #     ["arnaldo", "pizza", "terça-feira"],
    #     ["maria", "hamburguer", "terça-feira"],
    # ]
    # print(arnaldo_most_ordered_hamburger(hamburger))

    # Teste prato nunca pedido por joao
    # never_orders = [
    #     ["arnaldo", "hamburguer", "terça-feira"],
    #     ["maria", "pizza", "terça-feira"],
    #     ["maria", "coxinha", "terça-feira"],
    #     ["maria", "misto-quente", "terça-feira"],
    #     ["joao", "hamburguer", "terça-feira"],
    #     ["joao", "hamburguer", "terça-feira"]
    # ]
    # print(joao_dishes_never_order(never_orders, 'hamburguer'))

    # Teste dias em q Joao nunca vai
    # days = [
    #     ["joao", "hamburguer", "terça-feira"],
    #     ["joao", "hamburguer", "quarta-feira"],
    #     ["joao", "hamburguer", "domingo"],
    #     ["maria", "misto-quente", "segunda-feira"],
    #     ["maria", "misto-quente", "sabado"],
    # ]
    # print(days_joao_never_goes(days, ['domingo', 'terça-feira', 'quarta-feira']))
