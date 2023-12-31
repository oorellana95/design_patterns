from creational.abstract_factory.factories.abstract_factory import AbstractFactory


def build_product_components(factory: AbstractFactory):
    browser = factory.create_browser()
    browser.create_browser_window()
    browser.create_search_toolbar()

    messenger = factory.create_messenger()
    messenger.create_messenger_window()

