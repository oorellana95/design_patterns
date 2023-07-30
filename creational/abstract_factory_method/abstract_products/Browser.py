from abc import ABC, abstractmethod


class Browser(ABC):
    """
    Creates "Abstract Product A"
    """

    # Interface - Create Search Toolbar
    @abstractmethod
    def create_search_toolbar(self):
        pass

    # Interface - Create Browser Window
    @abstractmethod
    def create_browser_window(self):
        pass
