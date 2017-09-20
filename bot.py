import os
from functools import wraps
from telegram.ext import Updater, CommandHandler

from commands import vol_mute, vol_set, display_brightness, display_sleep


TELEGRAM_TOKEN = os.environ['TG_TOKEN']
LIST_OF_ADMINS = list(map(int, os.environ['TG_UID'].split(',')))


def restricted(func):
    """
    This decorator restricts access of a command to users specified in
    LIST_OF_ADMINS.

    Taken from: https://git.io/v5KpI
    """
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            # tell the unauthorized user to go away
            update.message.reply_text('Go away.')
            return
        return func(bot, update, *args, **kwargs)
    return wrapped


def hello(bot, update):
    """
    Greet the user with their first name and Telegram ID.
    """
    user_firstname = update.message.from_user.first_name
    user_id = update.message.from_user.id
    return update.message.reply_text(
        'Hello {}, your Telegram ID is {}'.format(user_firstname, user_id)
    )


@restricted
def vol_handler(bot, update, args):
    """
    Handle volume (/v) commands.

    /v mute - Mute or unmute system volume.
    /v n(0-100) - Set system volume to n.
    """
    if len(args) == 1:
        if args[0].isdigit():
            return update.message.reply_text(vol_set(args[0]))
        elif args[0] == 'mute':
            return update.message.reply_text(vol_mute())

    return update.message.reply_text('Syntax: /v [mute|<level(0-100)>]')


@restricted
def display_handler(bot, update, args):
    """
    Handle display (/d) commands.

    /d sleep - Put display to sleep.
    /d n(0-100) - Set display brightness to n.
    """
    if len(args) == 1:
        if args[0].isdigit():
            return update.message.reply_text(display_brightness(args[0]))
        elif args[0] == 'sleep':
            return update.message.reply_text(display_sleep())

    return update.message.reply_text('Syntax: /d [sleep|<level(0-100)>]')


if __name__ == '__main__':
    updater = Updater(TELEGRAM_TOKEN)

    updater.dispatcher.add_handler(
        CommandHandler('hello', hello)
    )
    updater.dispatcher.add_handler(
        CommandHandler('v', vol_handler, pass_args=True)
    )
    updater.dispatcher.add_handler(
        CommandHandler('d', display_handler, pass_args=True)
    )

    updater.start_polling()
    updater.idle()
