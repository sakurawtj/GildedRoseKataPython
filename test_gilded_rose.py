# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)

    # example1 of test that checks for logical errors
    def test_Backstage_passes_quality_increase_by_2_less_10_days(self):
        items = [Item("Backstage passes", 8, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        backstage_item = items[0]
        self.assertEquals(27, backstage_item.quality)
        self.assertEquals(7, backstage_item.sell_in)

    # example2 of test that checks for logical errors
    def test_Backstage_passes_quality_to_0_when_expired(self):
        items = [Item("Backstage passes", 1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        backstage_item = items[0]
        self.assertEquals(0, backstage_item.quality)

    # example3 of test that checks for logical errors
    def test_Conjured_item_decrease_quality_twice(self):
        items = [Item("Conjured Regular item", 5, 22)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        backstage_item = items[0]
        self.assertEquals(20, backstage_item.quality)
        self.assertEquals(4, backstage_item.sell_in)

    # example1 of test that checks for syntax errors
    def test_remove_all_quality_0(self):
        items = [
            Item(name="product1", sell_in=0, quality=0),
            Item(name="product2", sell_in=0, quality=0),
            Item(name="product3", sell_in=5, quality=20),
            Item(name="product2", sell_in=6, quality=10),
        ]
        gilded_rose = GildedRose(items)
        items = gilded_rose.remove_quality_zero()
        self.assertEquals(len(items), 2)

    # example4 of test that checks for logical errors
    def test_Backstage_passes_quality_increase_by_3_less_5_days(self):
        items = [Item("Backstage passes", 5, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        backstage_item = items[0]
        self.assertEquals(33, backstage_item.quality)
        self.assertEquals(4, backstage_item.sell_in)


if __name__ == '__main__':
    unittest.main()
