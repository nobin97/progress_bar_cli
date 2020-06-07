import os
import random
import time
from colors import color_and_codes as c_code


class ProgressBar:
    theme_color = None
    clear_screen = False
    show_title = True
    description = ""
    title = "Progress Bar"
    bar_length = 100
    in_progress = ""
    incomplete = ""
    bar = ""
    half_bar_length = 0
    full_bar_length = 0

    def __init__(
            self,
            bar_length=100,
            description=None,
            theme_color=None,
            in_progress_color=None,
            incomplete_color=None,
            in_progress_character="#",
            incomplete_character="_"):
        ip_char = in_progress_character
        ip_color = in_progress_color
        ic_char = incomplete_character
        ic_color = incomplete_color
        self.description = description
        self.bar_length = bar_length
        self.theme_color = self.get_theme_color(theme_color)
        if ip_color:
            ip_color = c_code.get(ip_color, None)
        if ic_color:
            ic_color = c_code.get(ic_color, None)
        self.in_progress = [
            ip_color + "\033[01m" + ip_char + "\033[0m" if ip_color else ip_char for _ in range(bar_length)]
        self.incomplete = [
            ic_color + "\033[01m" + ic_char + "\033[0m" if ic_color else ic_char for _ in range(bar_length)]
        self.bar = self.in_progress + self.incomplete
        self.half_bar_length = int(len(self.bar) / 2)
        self.full_bar_length = len(self.bar)

    @staticmethod
    def clear():
        os.system('echo -e \\\\033c' if os.name == 'posix' else 'cls')

    @staticmethod
    def get_theme_color(inp):
        if isinstance(inp, str):
            return c_code.get(inp, "")
        if isinstance(inp, list):
            return "".join([c_code.get(item, "") for item in inp])
        return ""

    def print_bar(self, value, final):
        if self.show_title:
            print(self.theme_color + self.title + "\n\033[0m")
        print(self.theme_color + self.description + "\n") if self.description else None
        percentage = int((value / final) * 100)
        bar_relative = int(self.half_bar_length * (percentage / 100))
        print("".join(self.bar[self.half_bar_length - bar_relative:self.full_bar_length - bar_relative]))
        print(self.theme_color + str(percentage) + "% Complete...\033[0m\n")

    def progress_bar(self, value=None, final=100, delay=None):
        use_random = False
        if delay == "random":
            delay = random.random
            use_random = True
        if self.bar_length < 1:
            print("At least a length of 1 is required!")
            return

        if value is None:
            index = 0
            while index <= final:
                self.clear() if self.clear_screen else None
                self.print_bar(index, final)
                index += 1
                if delay:
                    time.sleep(delay() if use_random else delay)
            return

        if value >= 0:
            if value > final:
                print("Value shouldn't be greater than final!")
                return
            self.clear() if self.clear_screen else None
            self.print_bar(value, final)
            if delay:
                time.sleep(delay() if use_random else delay)
            return
