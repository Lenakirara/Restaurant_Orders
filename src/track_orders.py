from collections import Counter


class TrackOrders:
    # construtor
    def __init__(self):
        self.orders_list = []

    def __len__(self):
        return len(self.orders_list)

    # novos pedidos =>
    # exe: [['maria, 'coxinha', 'terça-feira']]
    def add_new_order(self, costumer, order, day):
        self.orders_list.append([costumer, order, day])

    # buscar elemento em comum
    # Dica do Murilo - sala C => testando metodo most_common()
    # https://docs.python.org/3/library/collections.html
    # https://www.youtube.com/watch?v=YrFOAhT4Azk
    # https://pymotw.com/2/collections/counter.html
    def get_most_ordered_dish_per_costumer(self, costumer):
        orders_customer = [
            order[1] for order in self.orders_list if order[0] == costumer
        ]
        # [0][0] => para não vir: ('hamburguer', 16)
        counter_orders = Counter(orders_customer).most_common()[0][0]
        return counter_orders

    def get_never_ordered_per_costumer(self, costumer):
        never_orders = {
            order[1] for order in self.orders_list if costumer not in order
        }
        customer_order = {
            order[1] for order in self.orders_list if costumer in order
        }
        return never_orders - customer_order

    def get_days_never_visited_per_costumer(self, costumer):
        never_goes = {
            day[2] for day in self.orders_list if costumer not in day
        }
        customer_goes = {day[2] for day in self.orders_list if costumer in day}
        return never_goes - customer_goes

    def get_busiest_day(self):
        days_orders = [day[2] for day in self.orders_list]
        busiest_day = Counter(days_orders).most_common()[0][0]
        return busiest_day

    def get_least_busy_day(self):
        days_orders = [day[2] for day in self.orders_list]
        least_busy_day = Counter(days_orders).most_common()[-1][0]
        return least_busy_day

    # ao rodar a main.py acusa erro que está faltando função
    # 'get_order_frequency_per_costumer'
    def get_order_frequency_per_costumer(self, param1, param2):
        ...


# if __name__ == "__main__":
#     tracker = TrackOrders()
#     orders = [
#         ["arnaldo", "hamburguer", "terça-feira"],
#         ["joao", "hamburguer", "quinta-feira"],
#         ["joao", "hamburguer", "domingo"],
#         ["joao", "hamburguer", "domingo"],
#         ["maria", "pizza", "terça-feira"],
#         ["maria", "misto-quente", "terça-feira"],
#     ]
#     for i in orders:
#         tracker.add_new_order(i[0], i[1], i[2])
#     print(tracker.get_busiest_day())
#     print(tracker.get_least_busy_day())
