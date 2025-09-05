

import os
import json
import colorama
from colorama import Fore, Style
import time
import discord
import asyncio
import requests
from discord.ext import commands
from plyer import notification
import pyautogui
import winsound

CONFIG_FILE = "config.json"
colorama.init(autoreset=True)

def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/macOS
        os.system('clear')

def load_token():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            return config.get("token")
    return None

def save_token(token):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"token": token}, f, indent=4)

def is_token_valid(token):
    headers = {"Authorization": token}
    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
    return response.status_code == 200

def get_token_input():
    print(Fore.CYAN + Style.BRIGHT + """
╔═══════════════════════════════════════════════════╗
║    Please enter your Discord bot token           ║
╚═══════════════════════════════════════════════════╝
""")
    return input(Fore.LIGHTGREEN_EX + "Token: ")

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

def get_valid_token():
    token = load_token()
    if not token or not is_token_valid(token):
        print(Fore.RED + "No valid token found.")
        while True:
            token = get_token_input()
            if is_token_valid(token):
                save_token(token)
                print(Fore.GREEN + "Token saved and valid!")
                break
            else:
                print(Fore.RED + "Invalid token. Please try again.")
    return token

# Main program
clear_screen()
dynamic_welcome()
token = get_valid_token()

# Initialize Discord client and webhook URL
client = commands.Bot(command_prefix="!", self_bot=True)

@client.event
async def on_guild_channel_create(channel):
    category_names = ["INR TO CRYPTO", "CRYPTO TO INR", "I2C", "C2I"]
    if isinstance(channel, discord.TextChannel) and channel.category and str(channel.category.name.lower()) in [name.lower() for name in category_names]:
        # Create a link to the channel using the discord:// protocol
        channel_url = f'discord://discord.com/channels/{channel.guild.id}/{channel.id}'
        winsound.Beep(1000, 300)  # Frequency: 1000 Hz, Duration: 300 ms


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
        await asyncio.sleep(1)
        pyautogui.write(',c')
        



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
