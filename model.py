class Categories:
    def __init__(self,id, created_date,cat_name) -> None:
        self.created_date = created_date
        self.id = id
        self.name = cat_name

class Item:
    def __init__(self, created_date : str, item_id : str, name : str, qr_code : str, price : int, buying_price : int, category : Categories):
        self.created_date = created_date
        self.item_id = item_id
        self.name = name
        self.qr_code = qr_code
        self.price = price
        self.buying_price = buying_price
        self.category = category

    def getProfit(self):
        return int(self.price - self.buying_price)
    
class SaleItem:
    def __init__(self, customer_id : str, created_date : str, item : Item):
        self.item = item
        self.customer_id = customer_id
        self.created_date = created_date

    def getCategoryAndProfit(self):
        return self.item.category.name, self.item.name, self.item.getProfit()
        