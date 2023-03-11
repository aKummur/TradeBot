from config import PM_API_KEY, PM_API_SECRET, TELEGRAM_API_ID, TELEGRAM_API_HASH, TRADE_CALL_TELEGRAM_CHANNEL_ID
from telethon import TelegramClient, events
from pyPMClient.pmClient import PMClient
from scrips import ScripMaster
from order import Order

client = TelegramClient('historical', TELEGRAM_API_ID, TELEGRAM_API_HASH)
client.start()

BANK_NIFTY = "BANKNIFTY"

pm = PMClient(api_key=PM_API_KEY, api_secret=PM_API_SECRET)
pm.login("alpha")
pm.generate_session("your_request_token_here")

sm = ScripMaster(pm)
Ord = Order(pm)

async def main():
    @client.on(events.NewMessage(chats=TRADE_CALL_TELEGRAM_CHANNEL_ID))
    async def handler(event):
        print(event.message.text)
        if event.message.text and "add till" in event.message.text:
            # get the name, strike, buy price and SL
            try:
                name = "BANKNIFTY" if "BANKNIFTY" in event.message.text else "NIFTY"
                cmpParts = event.message.text.split("CMP")
                preCmp = cmpParts[0].strip()
                postCmp = cmpParts[1].strip()
                strike, cepe = preCmp.split(" ")[-2:]
                buyPrice = postCmp.split(" ")[0]
                sl = 1
                if "SL" in event.message.text:
                    sl = postCmp.split("SL")[1].strip().split(" ")[0]
                print("{} {} {} buy at {} SL {}".format(name, strike, cepe, buyPrice, sl))

                #  look up scrip
                s = sm.scripLookup(name, strike if "." in strike else strike+".0", cepe)
                print("buying {}".format(s.symbol))
                Ord.placeBuyOrder(s, int(buyPrice))
            except Exception as e:
                print("Error : {}".format(e))

with client:
    client.loop.create_task(main())
    client.loop.run_forever()
