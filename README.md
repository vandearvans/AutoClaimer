# 🤖 Discord AutoClaimer Bot 

A Python-based self-bot that monitors newly created text channels under specific category names in a Discord server and performs automated actions.

> ⚠️ This bot uses `self_bot=True`, which is against [Discord's Terms of Service](https://discord.com/terms). Use it only in testing environments or private servers where you have permission.

---

## ✅ Features

- Monitors newly created text channels in the following categories:
  - `INR TO CRYPTO`
  - `CRYPTO TO INR`
  - `I2C`
  - `C2I`
- Sends a Windows desktop notification when a matching channel is created
- Automatically opens the new channel using the Discord protocol link
- Prompts for and uses a Discord token to log in
- Displays an error if the token is invalid

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```


## 🚀 Usage

1. Make sure you have Python installed.

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the script:

```
python main.py
```

4. When prompted, enter your **Discord token**.

5. Keep the script running. When a new text channel is created in one of the following categories:

   * INR TO CRYPTO
   * CRYPTO TO INR
   * I2C
   * C2I

   The bot will:

   * Send a Windows system notification
   * Open the newly created channel in your browser using a Discord link

