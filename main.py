import web3

# Connect to the Ethereum network
w3 = web3.Web3(web3.Web3.HTTPProvider("https://mainnet.infura.io/v3/API-KEY-HERE"))

# Open the keys file
with open("keys.txt", "r") as f:
    # Read the Ethereum account addresses from the file
    addresses = f.readlines()

# Iterate over the Ethereum account addresses
for address in addresses:
    # Get the balance of the Ethereum account
    balance = w3.eth.getBalance(address.strip())
    # Convert the balance from wei to ether
    balance_ether = w3.fromWei(balance, "ether")
    # Print the balance
    print(f"Balance of {address.strip()}: {balance_ether} ether")
