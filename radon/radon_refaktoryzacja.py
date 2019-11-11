class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def change_day(self, item):
        item.sell_in = item.sell_in - 1
    
    def changeQuality_AgedBrie(self, item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 0:
              item.quality += 1

    def changeQuality_BackstageTickets(self, item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality += 1
        if item.sell_in < 0:
            item.quality = 0

    def changeQuality_Conjured(self, item):
        if item.quality > 0:
            item.quality = item.quality - 2
        if item.sell_in < 0 and item.quality > 0:
            item.quality = item.quality - 2
        
    def changeQuality_normalItem(self, item):
        item.quality = item.quality - 1
        if item.sell_in < 0:
            item.quality = item.quality - 1

    def Sulfuras_Quality(self, item):
        if item.quality != 80:
            item.quality = 80

    def QualityCheck(self, item):

        if item.quality > 50:
            item.quality = 50
        if item.quality < 0:
            item.quality = 0
            
    def another_update_quality(self):
        for item in self.items:
            normalItem = True
            
            self.change_day(item)
            
            if "Sulfuras" in item.name:
                self.Sulfuras_Quality(item)
                continue

            if item.name == "Aged Brie":
                normalItem = False
                self.changeQuality_AgedBrie(item)
                    
            if "Backstage" in item.name:
                normalItem = False
                self.changeQuality_BackstageTickets(item)

            if "Conjured" in item.name:
                normalItem = False
                self.changeQuality_Conjured(item)
            
            if normalItem:
                self.changeQuality_normalItem(item)

            self.QualityCheck(item)