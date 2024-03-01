# Basic-Blockchain-in-Python
This project is a simple implementation of a blockchain in Python. It provides a basic understanding of how blockchain technology works and demonstrates creating blocks with hashing capabilities.
Features
Block Class: Defines the structure of a block in the blockchain, including attributes such as index, timestamp, data, previous hash, and hash.
Blockchain Class: Manages the chain of blocks, including methods to create the genesis block, add new blocks, and calculate hashes.
Usage
To use this project, follow these steps:
1. Clone the repository to your local machine:
   
   git clone https://github.com/anjaliiiii1/Basic-Blockchain-in-Python.git

2. Navigate to the project directory:

   cd basic-blockchain-python

3. Run the blockchain.py file to see the example usage:

    python blockchain.py
   
5. Explore the code to understand how the blockchain is implemented and how blocks are created.
   Example:
   Here's a brief example of how to create a block using the provided classes:

block = Block(1, date.datetime.now(), "Hello, World!", "0")

print("Block Index:", block.index)

print("Timestamp:", block.timestamp)

print("Data:", block.data)

print("Previous Hash:", block.previous_hash)

Contributions
Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

print("Block Hash:", block.hash)





