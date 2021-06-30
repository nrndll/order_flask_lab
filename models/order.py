class Order():

    def __init__(self, customer_name, order_date, quantity, book_title, book_author, book_length):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity

        # orders are books
        self.book_title = book_title
        self.book_author = book_author
        self.book_length = book_length
