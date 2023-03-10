class Order():
    lotSizes = {
        "BANKNIFTY" : 25,
        "NIFTY" : 50
    }

    def __init__(self, pm):
        self.pm = pm

    def getFunds(self):
        try:
            return int(self.pm.funds_summary()['data']["funds_summary"]['trade_balance'])
        except Exception as e:
            print("Error : {}".format(e))

    def placeBuyOrder(self, scrip, buyPrice):
        lotSize = self.lotSizes[scrip.name]
        funds = self.getFunds()
        print("funds {} {}".format(funds, type(funds)))
        quantity = int(funds/(buyPrice*lotSize)) * lotSize
        print("quantity {}".format(quantity))
        try:
            res = self.pm.place_order(
                txn_type="B",
                exchange="NSE",
                segment="D",
                product="M",
                security_id=scrip.id,
                quantity=quantity,
                validity="DAY",
                order_type="MKT",
                price=0,
                source="N",
                off_mkt_flag=False,
            )
            print("Response : {}".format(res))
        except Exception as e:
            print("Error : {}".format(e))

    def placeBuyOrderWithSl(self, scrip, buyPrice, sl):
        lotSize = self.lotSizes[scrip.name]
        funds = self.getFunds()
        print("funds {} {}".format(funds, type(funds)))
        quantity = int(funds/(buyPrice*lotSize)) * lotSize
        print("quantity {}".format(quantity))
        try:
            res = self.pm.place_order(
                txn_type="B",
                exchange="NSE",
                segment="D",
                product="M",
                security_id=scrip.id,
                quantity=quantity,
                validity="DAY",
                order_type="SLM",
                price=0,
                source="N",
                off_mkt_flag=False,
                trigger_price=sl
            )
            print("Response : {}".format(res))
        except Exception as e:
            print("Error : {}".format(e))

if __name__ == "__main__":
    from .pyPMClient.pmClient import PMClient
    from scrips import ScripMaster
    from config import *

    pm = PMClient(api_key=API_KEY, api_secret=API_SECRET, access_token=ACCESS_TOKEN)
    # pm = PMClient(api_key=API_KEY, api_secret=API_SECRET)
    # pm.login("alpha")
    # pm.generate_session("request_token")

    sm = ScripMaster(pm)
    o = Order(pm)
    print(pm.funds_summary())
    print(o.getFunds())

    s = sm.scripLookup("BANKNIFTY", "39700.0", "PE")
    o.placeBuyOrder(s, 65)