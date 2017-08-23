from service.repositories.menu_repository import MenuRepository


def test_get_menu():
    menu = MenuRepository.get()
    assert len(menu) == 1


def test_get_menu_item():
    menu_item = MenuRepository.get_item(42)
    assert menu_item.name == 'Spam & Eggs'
    assert menu_item.price == 15.0
