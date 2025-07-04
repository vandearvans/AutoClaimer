

import os
import colorama
from colorama import Fore, Style
import time
import discord
import asyncio
import requests
from discord.ext import commands
from plyer import notification

# Initialize colorama for cross-platform colored text
colorama.init(autoreset=True)

# Function to clear the screen based on the OS
def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/macOS
        os.system('clear')

# Call clear screen
clear_screen()

# Beautiful and dynamic welcome message
def dynamic_welcome():
    welcome_message = """
    $$\    $$\ $$$$$$\  $$$$$$$\   $$$$$$$\ 
    \$$\  $$  |\____$$\ $$  __$$\ $$  _____|
    \$$\$$  / $$$$$$$ |$$ |  $$ |\$$$$$$\  
    \$$$  / $$  __$$ |$$ |  $$ | \____$$\ 
    \$  /  \$$$$$$$ |$$ |  $$ |$$$$$$$  |
        \_/    \_______|\__|  \__|\_______/ 
    """
    for char in welcome_message:
        print(Fore.MAGENTA + Style.BRIGHT + char, end='', flush=True)
        time.sleep(0.01)
    print("\n" + Fore.YELLOW + "Welcome to the Autoclaimer Console!\n" + "-" * 55)

# Function to prompt for token with a stylish input box
def get_token_input():
    print(Fore.CYAN + Style.BRIGHT + """
    ╔═══════════════════════════════════════════════════╗
    ║        Please enter your Discord bot token        ║
    ╚═══════════════════════════════════════════════════╝
    """)
    return input(Fore.LIGHTGREEN_EX + "Token: ")

# Display dynamic welcome message
dynamic_welcome()

# Prompt for token with a styled box
token = get_token_input()

# Initialize Discord client and webhook URL
client = commands.Bot(command_prefix="!", self_bot=True)

@client.event
async def on_guild_channel_create(channel):
    category_names = ["INR TO CRYPTO", "CRYPTO TO INR", "I2C", "C2I"]
    if isinstance(channel, discord.TextChannel) and channel.category and str(channel.category.name.lower()) in [name.lower() for name in category_names]:
        # Create a link to the channel using the discord:// protocol
        channel_url = f'discord://discord.com/channels/{channel.guild.id}/{channel.id}'

        # Send a Windows notification with the link
        notification.notify(
            title='New Channel Created',
            message=f'A new channel "{channel.name}" has been created in the category! Click to view.',
            app_name='Discord Bot',
            app_icon=None,
            timeout=10
        )

        # Open the channel link
        import webbrowser
        webbrowser.open(channel_url)

@client.event
async def on_ready():
    print(Fore.GREEN + Style.BRIGHT + f"\n✨ Success! Logged in as {client.user} ✨\n")


# Run the bot with the provided token
try:
    client.run(token)
except discord.errors.LoginFailure:
    # Handle invalid token error with a beautiful message
    print(Fore.RED + Style.BRIGHT + "\n❌ Error: The token provided is invalid. Please check your token.")
    print(Fore.YELLOW + "\nFor guidance on how to get your Discord bot token, refer to YouTube tutorials or the official Discord documentation:")
    print(Fore.CYAN + "https://youtu.be/nW8c7vT6HnU")  # Link to a YouTube tutorial on how to get the token
