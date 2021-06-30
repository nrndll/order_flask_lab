class Order():

    def __init__(self, customer_name, order_date, quantity):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity

        # orders are books
        self.book_title = ""
        self.book_author = ""
        self.book_length = 0
