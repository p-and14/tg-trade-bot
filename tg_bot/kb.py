from aiogram import types


menu_btns = [
    [types.InlineKeyboardButton(text="⚙️ Settings", callback_data="settings")],
    [types.InlineKeyboardButton(text="💵 Buy tokens", callback_data="buy")],
    [types.InlineKeyboardButton(text="💵 Sell tokens", callback_data="sell")],
    [types.InlineKeyboardButton(text="✅ Approve tokens", callback_data="approve")],
]
menu = types.InlineKeyboardMarkup(inline_keyboard=menu_btns)

exit_kb = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="◀️ Exit to the menu")]],
                                    resize_keyboard=True, one_time_keyboard=False)

settings_btns = [
    [types.InlineKeyboardButton(text="◀️ Back", callback_data="menu")],
    [types.InlineKeyboardButton(text="👛 Wallet settings", callback_data="wallet_settings")],
    [
        types.InlineKeyboardButton(text="💵 Buy settings", callback_data="buy_settings"),
        types.InlineKeyboardButton(text="💵 Sell settings", callback_data="sell_settings")
    ],
    [types.InlineKeyboardButton(text="✅ Approve settings", callback_data="approve_settings")],
]
settings = types.InlineKeyboardMarkup(inline_keyboard=settings_btns)


wallet_btns_available = [
    [types.InlineKeyboardButton(text="◀️ Back", callback_data="settings")],
    [types.InlineKeyboardButton(text="❌ Delete addded wallet", callback_data="delete_wallet")],
]
wallet_btns_not_available = [
    [types.InlineKeyboardButton(text="◀️ Back", callback_data="settings")],
    [types.InlineKeyboardButton(text="📝 Add existing wallet", callback_data="add_wallet"),
     types.InlineKeyboardButton(text="🆕 Create new wallet", callback_data="create_wallet"),],
]

wallet_available = types.InlineKeyboardMarkup(inline_keyboard=wallet_btns_available)
wallet_not_available = types.InlineKeyboardMarkup(inline_keyboard=wallet_btns_not_available)
