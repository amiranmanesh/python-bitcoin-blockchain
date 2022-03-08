import json
import sys
from time import time
import hashlib
from flask import Flask, jsonify
from uuid import uuid4


class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_trxs = []
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        ''' create a new block '''
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'trxs': self.current_trxs,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.current_trxs = []
        self.chain.append(block)

        return block

    def new_trx(self, sender, recipient, amount):
        ''' add a new trx to the mempool '''
        self.current_trxs.append({'sender': sender, 'recipient': recipient, 'amount': amount})
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        ''' hash a block'''
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
        pass

    @property
    def last_block(self):
        ''' return the last block '''
        pass

    @staticmethod
    def valid_proof(last_proof, proof):
        ''' check if this proof is fine or not '''
        this_proof = f'{proof}{last_proof}'.encode()
        this_proof_hash = hashlib.sha256(this_proof).hexdigest()

        return this_proof_hash[:4] == '0000'

    @staticmethod
    def proof_of_work(self, last_proof):
        ''' shows that the work is done '''
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof


app = Flask(__name__)

node_id = str(uuid4())

block_chain = BlockChain()


@app.route('/mine')
def mine():
    ''' This will mine oen block and will add it to the chain '''
    return "I will mine!"


@app.route('/trxs/new', methods=['POST'])
def new_trx():
    ''' will add a new trx'''
    return "a new trx added"


@app.route('/chain')
def full_chain():
    res = {
        'chain': block_chain.chain,
        'length': len(block_chain.chain),
    }
    return jsonify(res), 200


if __name__ == '__main__':
    port = 8090
    if len(sys.argv) >= 2:
        port = int(sys.argv[1])

    app.run(host='0.0.0.0', port=port)
