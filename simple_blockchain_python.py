import hashlib, time
class Block:
    def __init__(self, index, nonce, previous_hash, transactions):
        self.index = index
        self.nonce = nonce
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time.time()
        self.hash = self.get_hash()
    
    def get_hash(self):
        header_bin = (str(self.previous_hash) + 
                      str(self.nonce) + 
                      str(self.timestamp) +
                      str(self.transactions)).encode()
        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash
tx = {
    'sender':"0",
    'recipient':"address_1",
    'amount':1,
}
block0 = Block(0, 0, 0, tx)
block0_hash = block0.hash

blockchain = [block0]
print blockchain[0].hash
block1 = Block(1, 0, block0_hash, tx)
blockchain.append(block1)
print blockchain[1].hash
class Blockchain(object):
    
    def __init__(self):
        self.chain = []
        self.create_genesis_block()
    
    def create_genesis_block(self):
        transactions = {'sender':"genesis", 'recipient':"address_1", 'amount':1,}
        block = self.create_new_block(nonce=0, previous_hash=0, transactions=transactions)
        self.chain.append(block)

    def mine(self, previous_hash, transactions):
        ##pow to find nonce
        MAX_TARGET = int("00FFFFFFFFFF0000000000000000000000000000000000000000000000000000", 16)  
        difficulty = 1
        target = int(MAX_TARGET / difficulty)
        target32 = '{:0>64x}'.format(target) 
        MAX_NOUNCE = 2**32
        nonce = 0
        while nonce <= MAX_NOUNCE:
            block = self.create_new_block(nonce, previous_hash, transactions)
            if block.hash < target32:
                self.chain.append(block)
                return block
            nonce += 1
        return None
        
    def create_new_block(self, nonce, previous_hash, transactions):
        
        block = Block(
            index=len(self.chain),
            nonce=nonce,
            previous_hash=previous_hash,
            transactions=transactions
        )
                
        return block
    
    @property
    def get_last_block(self):
        return self.chain[-1]
    
    def get_block(self, index):
        return self.chain[index]
    
    def get_blockchain_height(self):
        return len(self.chain)
blockchain = Blockchain()
print "block.index", "block.nonce", "block.hash"
print blockchain.chain[0].index, blockchain.chain[0].nonce, blockchain.chain[0].hash
for i in range(1, 5):
    tx = {
    'sender':"0",
    'recipient':"address_" + str(i), 
    'amount':1,
    }

    last_hash = blockchain.get_last_block.get_hash()
    block = blockchain.mine(last_hash, tx)
    print block.index, block.nonce, block.hash
    
print "blockchain height: ", blockchain.get_blockchain_height()   
block.index block.nonce block.hash
