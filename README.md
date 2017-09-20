# tg-mac-remote

This repository contains the code for the article
[Remote-controlling macOS with a Python Telegram bot](https://medium.com/@half0wl/remote-controlling-macos-with-a-python-telegram-bot-d656d2e00226) on Medium.
Read the article for more info. The only difference between the article's code
and this repo is where the Telegram token/UID is set. Over here, we use
environment variables for easier config.

## Usage

1. Create a Telegram bot. See https://core.telegram.org/bots#creating-a-new-bot

2. Clone this repo, create a virtualenv, and install dependencies:

```bash
$ git clone https://github.com/half0wl/tg-mac-remote.git
$ cd tg-mac-remote
$ virtualenv .venv && .venv/bin/activate
$ pip install -r requirements.txt
$ brew install brightness  # required for display brightness control
```

3. Export your Telegram token and UID:

```bash
$ export TG_TOKEN=<your_telegram_token>
$ export TG_UID=<your_telegram_uid>
```

To add multiple `TG_UID`s, seperate them with a comma, e.g.
`1234567890,0987654321`. You can obtain your Telegram UID by firing up the bot
and sending it the "/hello" command.

You should be all set.