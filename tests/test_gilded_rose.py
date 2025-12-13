import pytest

from item import Item
from gilded_rose import GildedRose



def test_regular_items_decrease_by_one():
    items = [Item("+5 Dexterity Vest", 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    item = items[0]
    assert item.sell_in == 9
    assert item.quality == 19


@pytest.mark.parametrize(
    "name,sell_in,quality,expected_sell_in,expected_quality",
    [
        ("Aged Brie", 20, 30, 19, 31),
        ("Backstage passes to a TAFKAL80ETC concert", 20, 30, 19, 31),
    ],
)
def test_quality_goes_up_for_improving_products(
    name, sell_in, quality, expected_sell_in, expected_quality
):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    item = items[0]
    assert item.sell_in == expected_sell_in
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "name,sell_in,quality,expected_sell_in,expected_quality",
    [
        ("Backstage passes to a TAFKAL80ETC concert", 8, 30, 7, 32),
    ],
)
def test_quality_goes_up_by_two_for_backstage_products_with_10_days_or_less_left(
    name, sell_in, quality, expected_sell_in, expected_quality
):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    item = items[0]
    assert item.sell_in == expected_sell_in
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "name,sell_in,quality,expected_sell_in,expected_quality",
    [
        ("Backstage passes to a TAFKAL80ETC concert", 5, 15, 4, 18),
    ],
)
def test_quality_goes_up_by_three_for_backstage_products_with_5_days_or_less_left(
    name, sell_in, quality, expected_sell_in, expected_quality
):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    item = items[0]
    assert item.sell_in == expected_sell_in
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "name,sell_in,quality,expected_sell_in,expected_quality",
    [
        ("+5 Dexterity Vest", 0, 20, -1, 18),
        ("Conjured Mana Cake", 0, 6, -1, 4),
    ],
)
def test_quality_and_sellin_decrease_twice_as_fast_after_sell_by(
    name, sell_in, quality, expected_sell_in, expected_quality
):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    item = items[0]
    assert item.sell_in == expected_sell_in
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "name,sell_in,quality,expected_sell_in,expected_quality",
    [
        ("Backstage passes to a TAFKAL80ETC concert", 0, 20, -1, 0),
    ],
)
def test_backstage_passes_go_to_quality_zero_after_sell_by(
    name, sell_in, quality, expected_sell_in, expected_quality
):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    item = items[0]
    assert item.sell_in == expected_sell_in
    assert item.quality == expected_quality


def test_sulfuras_the_immutable():
    items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    item = items[0]
    assert item.sell_in == 0
    assert item.quality == 80


def test_quality_does_not_increase_past_50():
    items = [Item("Aged Brie", 4, 50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    item = items[0]
    assert item.sell_in == 3
    assert item.quality == 50


@pytest.mark.skip(reason="TODO: implement conjured rule")
def test_conjured_items_decrease_in_quality_twice_as_fast():
    items = [Item("Conjured Mana Cake", 3, 6)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    item = items[0]
    assert item.sell_in == 2
    assert item.quality == 2