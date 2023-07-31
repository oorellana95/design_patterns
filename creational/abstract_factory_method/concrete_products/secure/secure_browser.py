from creational.abstract_factory_method.abstract_products.browser import Browser


class SecureBrowser(Browser):
    """
    Type: Concrete Product
    Abstract methods of the Browser base class are implemented.
    """

    # Abstract Method of the Browser base class
    def create_search_toolbar(self):
        print("Secure Browser - Search Toolbar Created")

    # Abstract Method of the Browser base class
    def create_browser_window(self):
        print("Secure Browser - Browser Window Created")

    def create_incognito_mode(self):
        print("Secure Browser - Incognito Mode Created")