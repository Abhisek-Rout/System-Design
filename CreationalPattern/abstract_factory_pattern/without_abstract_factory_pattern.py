# Windows UI components
class WindowsButton:
    def render(self):
        print("Rendering windows button")

class WindowsScrollBar:
    def scroll(self):
        print("Scrolling windows scroll bar")

# Mac UI components
class MacOsButton:
    def render(self):
        print("Rendering MacOs button")

class MacOsScrollBar:
    def scroll(self):
        print("Scrolling MacOs scroll bar")


class Application:
    def main(self):
        # Windows UI
        button_win: WindowsButton = WindowsButton()
        scroll_bar_win: WindowsScrollBar = WindowsScrollBar()

        # Rendering the buttons
        button_win.render()
        scroll_bar_win.scroll()

        # Mac UI
        button_mac: MacOsButton = MacOsButton()
        scroll_bar_mac: MacOsScrollBar = MacOsScrollBar()

        button_mac.render()
        scroll_bar_mac.scroll()

        # Note:
        # 1. Above there is tight coupling with App and UI
        # 2. Intermixing of UI compoenent is alos possible, which shoud be avoided ideally.

if __name__ == "__main__":
    obj: Application = Application()
    obj.main()

