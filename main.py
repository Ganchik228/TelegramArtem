import logging
from telethon import TelegramClient, events
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji

logging.basicConfig(level=logging.INFO)

api_id = '26180333'
api_hash = '75ae7e2921ff402e2810e06071845f46'
phone_number = '+79825095557'

channel_username = '@NatashaGoncharova333'

client = TelegramClient('session_name', api_id, api_hash)


async def main():
    await client.start(phone=phone_number)

    @client.on(events.NewMessage(chats=channel_username))
    async def handler(event):
        try:
            await client(SendReactionRequest(
                peer=event.message.to_id,
                msg_id=event.message.id,
                reaction=[ReactionEmoji(emoticon='💩')]
            ))
            logging.info(f"Added 💩 reaction to message {event.message.id}")
        except Exception as e:
            logging.error(f"Failed to add reaction: {e}")

    logging.info(f"Listening to new messages on {channel_username}...")
    await client.run_until_disconnected()


if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())