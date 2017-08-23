from service.models.menu_item import MenuItem


class MenuRepository(object):

    spam_and_eggs = MenuItem(42, 'Spam & Eggs', 15.0)

    @staticmethod
    def get():
        return [MenuRepository.spam_and_eggs]

    @staticmethod
    def get_item(menu_item_id):
        if int(menu_item_id) == 42:
            return MenuRepository.spam_and_eggs
