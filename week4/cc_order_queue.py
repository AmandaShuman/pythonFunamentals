class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        self.customer = customer
        self.flavor = flavor
        self.scoops = scoops

        if flavor in self.flavors and 1 <= scoops <= 3:
            print("Order created!")
            order = {"customer": customer, "flavor": flavor, "scoops": scoops}
            self.orders.enqueue(order)
        else:
            error_msg_flavor = "We don't have that flavor, please choose another flavor."
            error_msg_scoops = "Please choose between 1 and 3 scoops"
            if flavor not in self.flavors:
                print(error_msg_flavor)
            else:
                print(error_msg_scoops)

    def show_all_orders(self):
        print("\nAll Pending Ice Cream Orders")
        if self.orders.items is None:  # use none, not zero!
            print("No upcoming orders")
        for order in self.orders.items:
            print("Customer:", order['customer'], "-- Flavor:",
                  order['flavor'], "-- Scoops:", order['scoops'])

    def next_order(self):
        remove_order = self.orders.dequeue()
        print("\nNext Order Up!")
        if remove_order is None:  # use none, not zero!
            print("No upcoming orders")
        else:
            print("Customer:", remove_order['customer'], "-- Flavor:",
                  remove_order['flavor'], "-- Scoops:", remove_order['scoops'])


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
