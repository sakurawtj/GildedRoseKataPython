# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Operation:
    def update_quality(self, item: Item):
        pass

    def increase_quality(self, item: Item, amount=1):
        item.quality = min(50, item.quality + amount)

    def decrease_quality(self, item: Item, amount=1):
        item.quality = max(0, item.quality - amount)

    def set_quality(self, item: Item, amount):
        item.quality = amount

    def update_sellin(self, item: Item):
        item.sell_in -= 1


class NormalItemOperation(Operation):
    def update_quality(self, item: Item):
        self.decrease_quality(item)
        self.update_sellin(item)
        if item.sell_in < 0:
            self.decrease_quality(item)


class AgedBrieOperation(Operation):
    def update_quality(self, item: Item):
        self.increase_quality(item)
        self.update_sellin(item)


class SulfurasOperation(Operation):
    def update_quality(self, item: Item):
        self.update_sellin(item)
        if item.quality != 80:
            self.set_quality(item, 80)


class BackstagePassesOperation(Operation):
    def update_quality(self, item: Item):
        if item.sell_in <= 5:
            self.increase_quality(item, 3)
        elif item.sell_in <= 10:
            self.increase_quality(item, 2)
        else:
            self.increase_quality(item)
        self.update_sellin(item)
        if item.sell_in <= 0:
            self.set_quality(item, 0)


class ConjuredItemOperation(Operation):
    def update_quality(self, item: Item):
        self.decrease_quality(item, 2)
        self.update_sellin(item)
        if item.sell_in < 0:
            self.decrease_quality(item, 2)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def getItemOperation(self, item: Item):
        if "Aged Brie" in item.name:
            return AgedBrieOperation()
        elif "Backstage passes" in item.name:
            return BackstagePassesOperation()
        elif "Sulfuras" in item.name:
            return SulfurasOperation()
        elif "Conjured" in item.name:
            return ConjuredItemOperation()
        else:
            return NormalItemOperation()

    def update_quality(self):
        for item in self.items:
            operation = self.getItemOperation(item)
            operation.update_quality(item)

    def remove_quality_zero(self):
        self.items = [item for item in self.items if item.quality > 0]
        return self.items

    def get_items(self):
        return [item.name for item in self.items]
