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
        else:
            error_msg_flavor = "We don't have that flavor, please choose another flavor."
            error_msg_scoops = "Please choose between 1 and 3 scoops"
            print("" if (flavor in self.flavors) else error_msg_flavor)
            print("" if(1 <= scoops <= 3) else error_msg_scoops)

        order = {"customer": customer, "flavor": flavor, "scoops": scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        print("All Pending Ice Cream Orders")
        for order in range :  # finish

    def next_order(self):
        # finish
