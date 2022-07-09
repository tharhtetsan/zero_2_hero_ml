import pandas as pd
import matplotlib.pyplot as plt
from item import item
import datetime

class util:

    def __init__(self):
        self.df = None
        self.filename = "item.xlsx"

    def readExcelFile(self):
        self.df = pd.read_excel(self.filename)
        

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
        
    def writeExcelFile(self,save_df):
        save_df.to_excel(self.filename)
    

    def update_df(self,cur_item : item):
        
        item_ids = self.df['item_id'].tolist()
        item_names = self.df['item_name'].tolist()
        buy_price = self.df['retail_price'].tolist()
        sale_price = self.df['sale_price'].tolist()
        categories = self.df['category'].tolist()
        
        item_ids.append(cur_item.id)
        item_names.append(cur_item.name)
        buy_price.append(cur_item.buying_price)
        sale_price.append(cur_item.price)
        categories.append(cur_item.categories_id)

        item_dict = {"item_id":item_ids,
            "item_name":item_names,
             "retail_price" : buy_price,
             "sale_price":sale_price,
             "category":categories
            }

        new_df = pd.DataFrame(item_dict)
        self.writeExcelFile(new_df)
        self.df=new_df
        

    def generate_proficCat_fig(self):
        categories = self.df['category'].tolist()
        dist_cate = set(categories)

        categories_profic= {}
        for cur_cat in dist_cate:
            categories_profic[cur_cat] = 0
        categories = self.df['category'].tolist()
        buy_price = self.df['retail_price'].tolist()
        sale_price = self.df['sale_price'].tolist()

        for buy,sale,cat in zip(buy_price,sale_price,categories):
            
            profic = int(sale)-int(buy)
            categories_profic[cat] = profic+categories_profic[cat]

        
        cat_name = list(categories_profic.keys())
        profic = list(categories_profic.values())
        plt.bar(cat_name,profic,c=profic)

       
 
        # using now() to get current time
        current_time = datetime.datetime.now()
        _date  = str(current_time.month)+"\\"+str(current_time.day)+"\\"+str(current_time.year)+"-"+str(current_time.hour)+":"+str(current_time.minute)

        plt.title("Total Profic at ::: "+_date)
        plt.savefig('profic_per_cat.png')