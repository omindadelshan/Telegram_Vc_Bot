from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME


@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**🎈Hello 👋🏻 {}!**\n\n 🤡I Am Garfild Vc Music Play V.1.1 Bot🤗 💥I Can Play Music In Voice Chats of Telegram Groups.🥶I Have A lot of cool feature that will amaze You🥶!\n\n**🤗send /cmdlist For More Help On My Usage ❤  🤗Powerd By @sdprojectupdates 🤗**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("🎙️ Add To Your Group 🎙️", url="https://t.me/SD_VC_Music_Play_Ro_Bot?startgroup=true")
            ],[
            InlineKeyboardButton("🎲Bot Group🎲", url="https://t.me/sdbotworld"),
            InlineKeyboardButton("💥 Update Channal 💥", url="https://t.me/sdprojectupdates")
            ],[
            InlineKeyboardButton("💎 My Commands 💎",callback_data="cmdlist")
            ]]
        ),
        disable_web_page_preview=True
    )
        
@Client.on_message(filters.command(["start", "start@SD_VC_Music_Play_Ro_Bot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**Music Bot Is Online ✅**",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/sdbotworld")
            ]]
        )
    )


@Client.on_message(filters.command(["cmdlist", "start@SD_VC_Music_Play_Ro_Bot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**🤗Welcome To : Help Menu❤️**

__× 👉First Add Me To Your Group..👈
× 👉Promote Me As Admin In Your Group With All Permission..👈__
× 👉And Send a group /userbotjoin Command👈

**🏷 Common Commands.**

• `/play` - Song Name : __Plays Via Youtube🎈__
• `/dplay` - Song Name : __Play Via Deezer🎈__
• `/splay` - Song Name : __Play Via Jio Saavn🎈__
• `/playlist` - __Show now playing list🎈__
• `/current` - __Show now playing🎈__

• `/song` - Song Name : __Get The Song From YouTube🎈__
• `/vid` - Video Name : __Get The Video From YouTube🎈__
• `/deezer` - song name : __download songs you want quickly via deezer🎈__
• `/saavn` - song name : __download songs you want quickly via saavn🎈__
• `/search` - YouTube Title : __(Get YouTube Search Query)🎈__

**🏷 Group Admin Commands.**

• `/skip` : __Skips Music👨‍💻__
• `/pause` : __Pause Playing Music👨‍💻__
• `/resume` : __Resume Playing Music👨‍💻__
• `/end` : __Stops playing Music👨‍💻__
• `/reload` : __Reloads Admin List👨‍💻__
• `/userbotjoin` : __Assistant Joins The Group👨‍💻__
• `/userbotleave` : __Assistant Leaves From The Group👨‍💻.__
👉 Powerd By @sdprojectupdates 👈""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/sdbotworld")
              ]]
          )
      )
