# TradeBot
Place trade orders based on calls given in Telegram channel on Paytm Money.</br></br>

This code uses telethon lib for telegram API access and</br>
pyPMClient by paytm money as broker platform.

---

This code is written for calls given in this format-</br>
`BANKNIFTY 44000 CE CMP 100 add till 90 SL 68 Target 140-160-200`</br>
Change the parsing logic as per your requirement.

---

Go to [developer.paytmmoney.com](https://developer.paytmmoney.com/create-app) to generate your Paytm Money API key and API secret.</br>
Login to this URL to get your request-token</br>
https://login.paytmmoney.com/merchant-login?apiKey={api_key}&state={state_key}</br>
Replace {api_key} with your API key and {state_key} with tradeBot.

---

Follow this [link](https://core.telegram.org/api/obtaining_api_id) to generate TELEGRAM_API_ID and TELEGRAM_API_HASH.  

---

Once you have all the above, replace the constants in config-repo.py and rename it to config.py and run the code using
```
python3 controller.py
```
---

You need to download and unzip the [pyPMClient repo](https://github.com/paytmmoney/pyPMClient) to this same directory.</br>
Else, resolve the import errors you might face.

---
If you face any difficulties, report an issue.