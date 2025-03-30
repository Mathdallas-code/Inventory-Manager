class Item:
    def __init__(
        self,
        name: str,
        opening_stock: int,
        stocks_bought: int,
        closing_stock: int,
        sales: int,
        cost_price: float,
        selling_price: float,
    ):
        self.name = name
        self.opening_stock = opening_stock
        self.stocks_bought = stocks_bought
        self.closing_stock = closing_stock
        self.sales = sales
        self.cost_price = cost_price
        self.selling_price = selling_price
