from service.models.menu_item import MenuItem


def test_menu_item():
    menu_item_id = 42
    name = 'Spam & Eggs'
    price = 15.0
    mi = MenuItem(menu_item_id, name, price)

    assert mi.id == menu_item_id
    assert mi.name == name
    assert mi.price == price
