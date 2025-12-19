class GildedRose(object):

    max_quality = 50
    min_quality = 0

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if self.is_legendary(item):
                self.process_legendary(item)
            elif self.is_aged_brie(item):
                self.process_aged_brie(item)
            elif self.is_backstage_passes(item):
                self.process_backstage_passes(item)
            elif self.is_conjured(item):
                self.process_conjured(item)
            else:
                self.process_regular(item)

    def is_legendary(self, item):
        return item.name == "Sulfuras, Hand of Ragnaros"

    def is_aged_brie(self, item):
        return item.name == "Aged Brie"

    def is_backstage_passes(self, item):
        return item.name.startswith("Backstage passes")

    def is_conjured(self, item):
        return item.name.startswith("Conjured")

    def process_legendary(self, item):
        #Legendary items do not change
        return

    def process_aged_brie(self, item):
        self.change_quality(item, 1)
        item.sell_in = item.sell_in - 1

    def process_backstage_passes(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in < 6:
            self.change_quality(item, 3)
        elif item.sell_in < 11:
            self.change_quality(item, 2)
        else:
            self.change_quality(item, 1)

        item.sell_in = item.sell_in - 1

    def process_regular(self, item):
        if item.sell_in > 0:
            self.change_quality(item, -1)
        else:
            self.change_quality(item, -2)

        item.sell_in = item.sell_in - 1

    def process_conjured(self, item):
        if item.sell_in > 0:
            self.change_quality(item, -2)
        else:
            self.change_quality(item, -4)
        item.sell_in = item.sell_in - 1

    def change_quality(self, item, change):
        item.quality = min(self.max_quality, item.quality + change)
        item.quality = max(self.min_quality, item.quality)




class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)