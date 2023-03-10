# TradeBot
Place trade orders based on calls given in Telegram channel on Paytm Money

This code uses telethon lib for telegram API access and
pyPMClient by paytm money as broker platform.

This code is written for calls given in this format -
'''
BANKNIFTY 44000 CE CMP 100 add till 90 SL 68 Target 140-160-200
'''
Change the parsing logic as per your requirement.

Go to [developer.paytmmoney.com](https://developer.paytmmoney.com/create-app) to generate your API key and API secret.

Login to this URL to get your request-token
: https://login.paytmmoney.com/merchant-login?apiKey={api_key}&state={state_key}
Replace {api_key} with your API key and {state_key} with tradeBot

To generate TELEGRAM_API_ID and TELEGRAM_API_HASH
Follow this [link](https://core.telegram.org/api/obtaining_api_id).

ONce you have all the above, replace the constants in config-repo.py and rename it to config.py and run the code using 
'''
python3 controller.py
'''

You need to download and unzip the [pyPMClient repo to this same directory](https://github.com/paytmmoney/pyPMClient).
Else, resolve the import errors you might face.

If you face any difficulties, report an issue.