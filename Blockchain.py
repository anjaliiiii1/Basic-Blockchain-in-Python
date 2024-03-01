import hashlib
import datetime as date

# Define the Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index              # Index of the block in the chain
        self.timestamp = timestamp      # Timestamp of when the block was created
        self.data = data                # Data stored in the block (e.g., transactions)
        self.previous_hash = previous_hash  # Hash of the previous block
        self.hash = self.calculate_hash()  # Hash of the current block

    # Method to calculate the hash of the block
    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(
            str(self.index).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8')
        )
        return sha.hexdigest()

# Define the Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # List to store blocks, starting with the genesis block

    # Method to create the genesis block (the first block in the chain)
    def create_genesis_block(self):
        return Block(0, date.datetime.now(), "Genesis Block", "0")

    # Method to get the latest block in the chain
    def get_latest_block(self):
        return self.chain[-1]

    # Method to add a new block to the chain
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash  # Set previous hash of the new block
        new_block.hash = new_block.calculate_hash()             # Calculate hash for the new block
        self.chain.append(new_block)                            # Append the new block to the chain

# Example usage
blockchain = Blockchain()                      # Create a new blockchain instance
blockchain.add_block(Block(1, date.datetime.now(), "Transaction Data", ""))  # Add a new block to the chain

# Print the blocks in the blockchain
for block in blockchain.chain:
    print("Block Index:", block.index)
    print("Block Hash:", block.hash)
    print("Previous Block Hash:", block.previous_hash)
    print("Block Data:", block.data)
    print("Timestamp:", block.timestamp)
    print("------------------------------------------")
