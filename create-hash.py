from stellar_sdk import Server, Keypair, Network, TransactionBuilder, TextMemo
from stellar_sdk.exceptions import BadRequestError

# Initial configurations
secret_key = ""  # Replace with the correct private key
public_key = Keypair.from_secret(secret_key).public_key
message = ""

# 1. Signing the message
keypair = Keypair.from_secret(secret_key)
signature = keypair.sign(message.encode())

# 2. Connecting to the Stellar Mainnet server
server = Server("https://horizon.stellar.org")

# 3. Loading the account
account = server.load_account(public_key)

# 4. Building the transaction
transaction = (
    TransactionBuilder(
        source_account=account,
        network_passphrase=Network.PUBLIC_NETWORK_PASSPHRASE,
        base_fee=server.fetch_base_fee()
    )
    .add_text_memo(TextMemo(message))  # Adding the message as MEMO
    .append_manage_data_op("signature", signature)  # Using 'manage_data' to add the signature
    .build()
)

# 5. Signing the transaction with the private key
transaction.sign(keypair)

# 6. Submitting the transaction
try:
    response = server.submit_transaction(transaction)
    print("✅ Transaction submitted successfully!")
    print("Transaction hash:", response["hash"])  # Gets the transaction hash
    print("Transaction details:", response)
except BadRequestError as e:
    print("⚠ Error submitting the transaction:", e)
