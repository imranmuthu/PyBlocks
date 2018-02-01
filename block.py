class block(object):
    transactions = []

    def __init__(self, transactions=None, previous_block=None):
        self.transactions = transactions
        self.previous_block = previous_block

    def get_transactions(self):
        return self.transactions

    def get_previous(self):
        return self.previous_block


    def set_transactions(self, transactions):
        self.transactions = transactions

