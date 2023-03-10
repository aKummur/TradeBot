import datetime

class Scrip():
    def __init__(self, id, name, symbol, strike):
        self.id = id
        self.name = name
        self.symbol = symbol
        self.strike = strike

class ScripMaster():
    allScrips = []

    def __init__(self, pm):
        self.pm = pm
        self.loadNiftyAndBNFScrips()

    def loadNiftyAndBNFScrips(self):
        print("loading Scrips")
        try:
            res = self.pm.security_master(scrip_type="OPTION")
            lines = res.splitlines()
            for line in lines:
                id, symbol, name = line.split(",")[:3]
                strike = line.split(",")[-2][1:-1]
                index = name.split(" ")[0][1:]
                # print("{0} {1} {2} {3} {4}".format(id, symbol, name, strike, index))
                if index == "NIFTY" or index == "BANKNIFTY":
                    # add Scrip
                    if ("16 " + self.getCurrentMonth()) in name:
                        # print("{0} {1} {2} {3} {4}".format(id, symbol, name, strike, index))
                        self.addScrip(id[1:-1], index, symbol, strike)
        except Exception as e:
            print("Error : {}".format(e))

    def addScrip(self, id, name, symbol, strike):
        # print("adding {}".format(symbol))
        self.allScrips.append(Scrip(id=id, name=name, symbol=symbol, strike=strike))

    def scripLookup(self, name, strike, CeOrPe):
        print("Total Scrips {}".format(len(self.allScrips)))
        # print("0th scrip {0} {1}".format(self.allScrips[0].name, self.allScrips[0].strike))
        for s in self.allScrips:
            if s.name == name and s.strike == strike and CeOrPe in s.symbol:
                return s
            
    def getCurrentMonth(self):
        month_names = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
               'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
        current_month = datetime.datetime.now().month
        return month_names[current_month]