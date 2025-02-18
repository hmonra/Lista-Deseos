#  Pre-configured Wishlist Tracking Bot

This Python script uses Selenium and Undetected ChromeDriver to monitor a pre-configured PcComponentes wishlist and send notifications via Telegram when an item is added to the cart. Ideal for making sure you don't miss out on that offer you've been waiting for!

##  Features

*   **Continuous Monitoring:** The script periodically checks the wishlist for changes.
*   **Telegram Notifications:** Receive instant alerts on your mobile when an item is added to the cart. Includes links to the wishlist, the item, and the cart summary.
*   **Captcha Detection:** Integrates automatic captcha solving to avoid interruptions.
*   **Error Handling:** Includes error management for Timeouts and "Bad Gateway" errors, with automatic retries and Telegram notifications.
*   **Automatic Cookie Acceptance:** The script accepts cookies so you don't have to do it manually.
*   **Easy to Use:** Simple configuration using environment variables or directly in the code (although using environment variables is recommended).

## ⚙️ Installation

1.  **Requirements:**
    *   Python 3.x
    *   The libraries specified in `requirements.txt` (install with `pip install -r requirements.txt`). You can create this file with `pip freeze > requirements.txt` after installing the libraries.
    *   Undetected ChromeDriver (included in the repository).
    *   Telegram account and created Bot (get the token and chat ID).

2.  **Clone the repository:**

    ```bash
    git clone https://github.com/hmonra/Lista-Deseos.git
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration:**

    *   **Environment Variables (Recommended):**
        Create environment variables for `TOKEN_BOT` and `CHAT_ID` with the values of your Telegram bot.
        Example in Linux/macOS:
        ```bash
        export TOKEN_BOT="YOUR_TOKEN_HERE"
        export CHAT_ID="YOUR_CHAT_ID_HERE"
        ```
        Example in Windows:
        ```bash
        set TOKEN_BOT="YOUR_TOKEN_HERE"
        set CHAT_ID="YOUR_CHAT_ID_HERE"
        ```
    *   **Directly in the code (Not recommended):**
        Edit the `main.py` script and replace the values of `bot_token` and `bot_chatid` with those of your Telegram bot.
    *   Modify the `lista_deseos` variable with the URL of your PcComponentes wishlist.

##  Usage

Run the script:

```bash
python main.py