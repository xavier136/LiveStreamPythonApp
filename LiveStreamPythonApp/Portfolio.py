class Portfolio(object):
    """Portfolio countaining the cash and cryptocurrencies"""

    def __init__(self, cash, crypto):
        self.cash = cash
        self.crypto = crypto
        self.initial_cash = cash
        self.initial_crypto = crypto

    def get_cash(self):
        return self.cash
    
    def get_crypto(self):
        return self.crypto

    def get_initial_cash(self):
        return self.initial_cash

    def get_initial_crypto(self):
        return self.initial_crypto

    def buy_crypto(self, quantity, mid, fee):
        self.crypto += quantity
        self.cash -= quantity * mid * (1 - fee)

    def sell_crypto(self, quantity, mid, fee):
        self.crypto -= quantity
        self.cash += quantity * mid * (1 - fee)

    def get_portfolio_value(self, mid):
        return self.cash + self.crypto * mid
        


