import os
import random
from subprocess import call
import time


class ProgressBar:
    theme_color = None
    clear_screen = False
    show_title = True
    title = "Progress Bar"
    bar_length = 100
    in_progress = ""
    incomplete = ""
    bar = ""
    half_bar_length = 0
    full_bar_length = 0
    colors = {
        'red': '\033[91m',
        'yellow': '\033[93m',
        'green': '\033[92m',
        'invisible': '\033[08m',
        'bold': '\033[01m',
        'end': '\033[0m',
        'dim': "\033[2m",
        'blue': "\033[34m",
        'magenta': "\033[35m",
        'cyan': "\033[36m",
        'light-gray': "\033[37m",
        'dark-gray': "\033[90m",
        'light-red': "\033[91m",
        'light-green': "\033[92m",
        'light-yellow': "\033[93m",
        'light-blue': "\033[94m",
        'light-magenta': "\033[95m",
        'light-cyan': "\033[96m",
        'white': "\033[97m"
    }

    def __init__(
            self,
            bar_length=100,
            theme_color=None,
            in_progress_color=None,
            incomplete_color=None,
            in_progress_character="#",
            incomplete_character="_"):
        ip_char = in_progress_character
        ip_color = in_progress_color
        ic_char = incomplete_character
        ic_color = incomplete_color
        self.bar_length = bar_length
        self.theme_color = self.colors.get(theme_color, None) if theme_color else None
        if ip_color:
            ip_color = self.colors.get(ip_color, None)
        if ic_color:
            ic_color = self.colors.get(ic_color, None)
        self.in_progress = [
            ip_color + "\033[01m" + ip_char + "\033[0m" if ip_color else ip_char for _ in range(bar_length)]
        self.incomplete = [
            ic_color + "\033[01m" + ic_char + "\033[0m" if ic_color else ic_char for _ in range(bar_length)]
        self.bar = self.in_progress + self.incomplete
        self.half_bar_length = int(len(self.bar) / 2)
        self.full_bar_length = len(self.bar)

    @staticmethod
    def clear():
        _ = call('clear' if os.name == 'posix' else 'cls')

    def print_bar(self, value, final):
        print(
            self.theme_color + self.title + "\n\033[0m" if self.theme_color else self.title + "\n"
        ) if self.show_title else None
        percentage = int((value / final) * 100)
        bar_relative = int(self.half_bar_length * (percentage / 100))
        print("".join(self.bar[self.half_bar_length - bar_relative:self.full_bar_length - bar_relative]))
        if self.theme_color:
            print(self.theme_color + str(percentage) + "% Complete...\033[0m\n")
        else:
            print(percentage, "% Complete...\n", sep="")

    def progress_bar(self, value=None, final=100, delay=0):
        rand = False
        if delay == "random":
            delay = random.random
            rand = True
        if self.bar_length < 1:
            print("At least a length of 1 is required!")
            return

        if value is None:
            i = 0
            while i <= final:
                self.print_bar(i, final)
                i += 1
                if delay:
                    time.sleep(delay() if rand else delay)
                self.clear() if self.clear_screen else None
            return

        if value >= 0:
            if value > final:
                print("Value shouldn't be greater than final!")
                return
            self.print_bar(value + 1, final)
            if delay:
                time.sleep(delay() if rand else delay)
            return
