class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_trx = []

    def new_block(self):
        ''' create a new block '''
        pass

    def new_trx(self):
        ''' add a new trx to the mempool '''
        pass

    @staticmethod
    def hash(self):
        ''' hash a block'''
        pass

    @property
    def last_block(self):
        ''' return the last block '''
        pass
