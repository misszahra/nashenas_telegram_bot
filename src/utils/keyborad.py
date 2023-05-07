from telebot import types
import emoji

def create_keyborad(*keys, row_width=2, resize_keyboard=True):
    """create a keybords from list of keyes.

    Example:
            keys = ['a', 'b', 'c', 'd']
    """
    markup = types.ReplyKeyboardMarkup(
        row_width=row_width,
        resize_keyboard=resize_keyboard,
        )
    keys = map(emoji.emojize, keys)
    bottens = map(types.KeyboardButton, keys)
    markup.add(*bottens)
    return markup
