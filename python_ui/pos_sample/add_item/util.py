import pandas as pd


class util:

    def __init__(self):
        self.df = None

    def readExcelFile(self,filename):
        self.df = pd.read_excel(filename)
        

    def get_latestID(self):
        "ITM_1"
        ids = self.df['item_id']
        latest_id = None
        for cur_itemid in ids:
            latest_id = cur_itemid

        if latest_id is None:
            idCount = 1
        else:
            idCount = int(latest_id.split("_")[1])
            idCount = idCount+1
        
        return "ITM_"+str(idCount)
        



