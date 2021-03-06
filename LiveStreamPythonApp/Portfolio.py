class Portfolio(object):
    """Portfolio countaining the cash and cryptocurrencies"""

    def __init__(self, cash, crypto, max_holding):
        self.cash = cash
        self.crypto = crypto
        self.initial_cash = cash
        self.initial_crypto = crypto
        self.max_holding = max_holding

    def get_cash(self):
        return self.cash
    
    def get_crypto(self):
        return self.crypto

    def get_initial_cash(self):
        return self.initial_cash

    def get_initial_crypto(self):
        return self.initial_crypto

    def buy_crypto(self, quantity, mid, fee):
        if self.crypto < self.max_holding and self.cash > quantity * mid:
            self.crypto += quantity
            self.cash -= quantity * mid * (1 - fee)

    def sell_crypto(self, quantity, mid, fee):
        if self.crypto > 0 and self.crypto >= quantity:
            self.crypto -= quantity
            self.cash += quantity * mid * (1 - fee)
        elif self.crypto > 0 and self.crypto  < quantity:
            self.cash += (self.crypto) * mid * (1 - fee)
            self.crypto = 0

    def get_portfolio_value(self, mid):
        return self.cash + self.crypto * mid
        


