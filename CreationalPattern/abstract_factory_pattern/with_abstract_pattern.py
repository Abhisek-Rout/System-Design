# Create abstract product interface
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class ScrollBar(ABC):
    @abstractmethod
    def scroll(self):
        pass

# Windows UI components
class WindowsButton(Button):
    def render(self):
        print("Rendering windows button")

class WindowsScrollBar(ScrollBar):
    def scroll(self):
        print("Scrolling windows scroll bar")

# Mac UI components
class MacOsButton(Button):
    def render(self):
        print("Rendering MacOs button")

class MacOsScrollBar(ScrollBar):
    def scroll(self):
        print("Scrolling MacOs scroll bar")


# Abstract factory interface
class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    
    @abstractmethod
    def create_scrollbar(self):
        pass

# Concrete implementation of windows factory
class WindowsUI(UIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_scrollbar(self):
        return WindowsScrollBar()

# Concrete implementation of mac factory
class MacUI(UIFactory):
    def create_button(self):
        return MacOsButton()
    
    def create_scrollbar(self):
        return MacOsScrollBar()

class Application:
    def __init__(self, factory: UIFactory):
        self.button: Button = factory.create_button()
        self.scroll_bar: ScrollBar = factory.create_scrollbar()

    def main(self):
        self.button.render()
        self.scroll_bar.scroll()


if __name__ == "__main__":
    # Decide the UI
    win_ui: WindowsUI = WindowsUI()

    mac_ui: MacUI = MacUI()

    obj: Application = Application(mac_ui)
    obj.main()

