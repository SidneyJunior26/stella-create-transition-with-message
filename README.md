# Stellar Message Signing and Transaction Submission 🚀

This Python project allows you to connect to the Stellar network, sign a message, and send it along with a transaction to the Stellar blockchain using the `stellar_sdk` library. Whether you're integrating Stellar's capabilities into your application or just experimenting with Stellar transactions, this tool provides an easy-to-use implementation for message signing and transaction submission.

## Features ✨

- **Message Signing**: Signs a message using a provided private key.
- **Transaction Building**: Connects to the Stellar Mainnet server, loads an account, and constructs a transaction.
- **Transaction Submission**: Signs the transaction and submits it to the Stellar network, including the signature and message as part of the transaction data.

## Prerequisites 📋

To use this project, you need the following:
- Python 3.x
- `stellar_sdk` library

You can install the `stellar_sdk` library using the following command:
```bash
pip install stellar-sdk
```

## Configuration ⚙️

1. Clone this repository to your local machine.
2. Open the main script and enter your **private key** in the `secret_key` field.

## Usage 🛠️

### Code Walkthrough 📖

1. **Initial Setup**:  
   - Define the `secret_key` (your private key) to generate the account's public key.
   - Enter a message that you wish to sign and send as part of the transaction.

2. **Message Signing**:  
   - The provided message is signed using the private key, ensuring authenticity.

3. **Connecting to the Stellar Server**:  
   - The script connects to the [Stellar Mainnet server](https://horizon.stellar.org), which serves as the main access point for Stellar's network.

4. **Loading the Account**:  
   - The account associated with the public key is loaded, enabling operations on that account.

5. **Transaction Building and Signing**:  
   - A transaction is built with a base network fee, a memo containing the signed message, and a `manage_data` operation to include the signature.

6. **Transaction Submission**:  
   - The transaction is signed with the private key and submitted to the Stellar network. If successful, it returns the transaction hash and details; if an error occurs, it captures and displays the error message.

### Running the Script 🚀

To run the script, simply execute the following command:
```bash
python <filename>.py
```

### Example Output 🖥️

On successful transaction submission:
```plaintext
✅ Transaction submitted successfully!
Transaction hash: <TRANSACTION_HASH>
Transaction details: <TRANSACTION_DETAILS>
```

### Notes 📝

- **Submission Error**:  
  If the transaction submission fails, a `BadRequestError` is raised, providing details on the cause of the error.

- **Testing Network**:  
  If you want to experiment without spending real Lumens, you can switch to the Testnet:
  - Replace `Network.PUBLIC_NETWORK_PASSPHRASE` with `Network.TESTNET_NETWORK_PASSPHRASE`
  - Use the Testnet server: `https://horizon-testnet.stellar.org`

## References 📚

- [Stellar SDK Documentation for Python](https://stellar-sdk.readthedocs.io/en/latest/)
- [Stellar Horizon API](https://www.stellar.org/developers/horizon/reference/)
```

This markdown-based README provides clear documentation, helping users understand the setup, usage, and purpose of your project. The added emojis also help make the README more engaging.
