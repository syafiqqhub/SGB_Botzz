from telethon import TelegramClient, events
import asyncio
import requests
import random
import os

API_ID = '20193822'  # Ganti dengan API ID Anda
API_HASH = '0dff5148275df0740fa60a8aeb66a8a9'  # Ganti dengan API Hash Anda

client = TelegramClient('group_manager_bot', API_ID, API_HASH)

# List untuk menyimpan item (untuk fitur lain yang mungkin Anda inginkan)
store_items = []

# Daftar kata dan emoji yang perlu dideteksi
sensitive_words = ["vcs", "vc", "video call", "bogel", "video pribadi", "video private", "🥵", "💦", "🍆", "🍑"]

@client.on(events.NewMessage(pattern=r'\.kick'))
async def kick_user(event):
    if event.is_group:
        await event.reply("Silakan sebutkan pengguna yang ingin dikeluarkan!")
        return

@client.on(events.NewMessage())
async def detect_sensitive_content(event):
    if any(word in event.raw_text.lower() for word in sensitive_words):
        try:
            await event.delete()  # Menghapus pesan yang tidak diinginkan
            await event.reply("Pesan ini telah dihapus karena mengandung konten sensitif! ❌")
        except Exception as e:
            print(f"Failed to delete message: {e}")

@client.on(events.NewMessage())
async def greet_new_member(event):
    if event.raw_text and event.sender_id:  # Cek apakah ada teks dan ID pengirim
        group = await event.get_chat()
        user = await client.get_entity(event.sender_id)
        if user.first_name:  # Pastikan ada nama pengguna
            await client.send_file(event.chat_id, 'https://d.top4top.io/m_3302qdvnx1.mp4', caption=f"Hai {user.first_name}, sila baca deskripsi grup ya! 📜")

@client.on(events.NewMessage())
async def farewell_member(event):
    if event.raw_text and event.sender_id:  # Cek apakah ada teks dan ID pengirim
        group = await event.get_chat()
        user = await client.get_entity(event.sender_id)
        if user.first_name:  # Pastikan ada nama pengguna
            await client.send_file(event.chat_id, 'https://h.top4top.io/m_330242orb1.mp4', caption=f"Selamat Tinggal {user.first_name}, harap datang kembali! 👋")

@client.on(events.NewMessage(pattern=r'\.cekganteng (.+)'))
async def cek_ganteng(event):
    name = event.message.message.split(' ', 1)[1]
    percentage = random.randint(1, 100)
    await event.reply(f"{name} adalah {percentage}% ganteng! 😎")

@client.on(events.NewMessage(pattern=r'\.cekcantik (.+)'))
async def cek_cantik(event):
    name = event.message.message.split(' ', 1)[1]
    percentage = random.randint(1, 100)
    await event.reply(f"{name} adalah {percentage}% cantik! 😊")

@client.on(events.NewMessage(pattern=r'\.lagu (.+)'))
async def send_song(event):
    song_name = event.message.message.split(' ', 1)[1]
    song_file = f"{song_name}.mp3"  # Pastikan file lagu ada di direktori yang sama
    if os.path.exists(song_file):
        await client.send_file(event.chat_id, song_file)
    else:
        await event.reply("Lagu tidak ditemukan! ❌")

@client.on(events.NewMessage(pattern=r'\.menugroup'))
async def show_menu(event):
    menu_text = (
        "Menu Perintah:\n"
        ".kick - Keluarkan pengguna dari grup\n"
        ".cekganteng [nama] - Cek persentase kegantengan\n"
        ".cekcantik [nama] - Cek persentase kecantikan\n"
        ".lagu [nama_lagu] - Kirim lagu sesuai nama\n"
        ".owner - Tampilkan pemilik bot\n"
    )
    await event.reply(menu_text)

@client.on(events.NewMessage(pattern=r'\.owner'))
async def show_owner(event):
    owner_message = (
        "Haii, @syafiqqparker adalah owner SGP_Botzz! "
        "Kalau mau guna bot group macam ni cek je kt channel dia @n_i4nx"
    )
    await event.reply(owner_message)

async def main():
    await client.start()
    if not await client.is_user_authorized():
        phone = input("Masukkan nomor telepon Anda: ")
        await client.send_code_request(phone)
        code = input("Masukkan kode yang diterima: ")
        await client.sign_in(phone, code)
    print("Userbot sudah berjalan...")
    await client.run_until_disconnected()

with c
lient:
    client.loop.run_until_comple
