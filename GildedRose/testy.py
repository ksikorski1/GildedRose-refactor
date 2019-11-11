from mine_gilded_rose import *

items = [
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="+5 Dexterity Vest", sell_in=6, quality=20),
        Item(name="+5 Dexterity Vest", sell_in=-1, quality=20),
        Item(name="Aged Brie", sell_in=5, quality=10),
        Item(name="Aged Brie", sell_in=-1, quality=10),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=13, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=20),
        Item(name="Conjured Mana Cake", sell_in=3, quality=20),
        Item(name="Conjured Mana Cake", sell_in=-1, quality=20),
      ]

GildedRose(items).another_update_quality()

def SulfurasTest():
  assert items[0].quality == 80, ("Blad dla:", items[0])
  assert items[1].quality == 80, ("Blad dla:", items[1])

def NormalItemTest():
  assert items[2].quality == 19, ("Blad dla:", items[2])
  assert items[3].quality == 18, ("Blad dla:", items[3])


def AgedBrieTest():
  assert items[4].quality == 11, ("Blad dla:", items[4])
  assert items[5].quality == 12, ("Blad dla:", items[5])

def BackstageTicketsTest():
  assert items[6].quality == 21, ("Blad dla:", items[6])
  assert items[7].quality == 22, ("Blad dla:", items[7])
  assert items[8].quality == 23, ("Blad dla:", items[8])  
  assert items[9].quality == 0, ("Blad dla:", items[9])

def ConjuredTest():
  assert items[10].quality == 18, ("Blad dla:", items[10])
  assert items[11].quality == 16, ("Blad dla:", items[11])
  

SulfurasTest()
NormalItemTest()
AgedBrieTest()
BackstageTicketsTest()
ConjuredTest()