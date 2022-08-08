class item:
    def __init__(self,item_id:str,name : str, qr_code : str,price:int,buying_price:int, categories_id :str):
        self.name = name
        self.id =  item_id
        self.qr_code=  qr_code
        self.price = price
        self.buying_price = buying_price
        self.categories_id = categories_id
        
    
    def getProfic(self):
        return int(self.price - self.buying_price)
        