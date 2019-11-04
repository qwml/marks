# -*- coding: utf-8 -*-
# https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/master/python

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie": 
                item.quality = min([50, item.quality + 1])
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.quality = min([50, item.quality + 1])
                item.quality = min([50, max([self.quality + _ for _ in [0, 1 if item.quality < 6 else 0, 2 if item.qualty < 11 else 0]])])
            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass
            else:
                item.quality = max([0, item.quality - 1])

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    item.quality = min([50, item.quality + 1]) 
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0
                elif item.name == "Sulfuras, Hand of Ragnaros":
                    pass
                else:
                    item.quality = item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)