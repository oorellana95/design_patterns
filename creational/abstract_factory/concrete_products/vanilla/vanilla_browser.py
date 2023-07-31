from creational.abstract_factory.abstract_products.browser import Browser


class VanillaBrowser(Browser):
    """
    Type: Concrete Product
    Abstract methods of the Browser base class are implemented.
    """

    # Interface - Create Search Toolbar
    def create_search_toolbar(self):
        print("Search Toolbar Created")

    # Interface - Create Browser Window]
    def create_browser_window(self):
        print("Browser Window Created")