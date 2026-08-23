from _typeshed import Incomplete

CSI: str
OSC: str
BEL: str

def code_to_chars(code): ...
def set_title(title): ...
def clear_screen(mode: int = 2): ...
def clear_line(mode: int = 2): ...

class AnsiCodes:
    def __init__(self) -> None: ...

class AnsiCursor:
    def UP(self, n: int = 1): ...
    def DOWN(self, n: int = 1): ...
    def FORWARD(self, n: int = 1): ...
    def BACK(self, n: int = 1): ...
    def POS(self, x: int = 1, y: int = 1): ...

class AnsiFore(AnsiCodes):
    BLACK: int
    RED: int
    GREEN: int
    YELLOW: int
    BLUE: int
    MAGENTA: int
    CYAN: int
    WHITE: int
    RESET: int
    LIGHTBLACK_EX: int
    LIGHTRED_EX: int
    LIGHTGREEN_EX: int
    LIGHTYELLOW_EX: int
    LIGHTBLUE_EX: int
    LIGHTMAGENTA_EX: int
    LIGHTCYAN_EX: int
    LIGHTWHITE_EX: int

class AnsiBack(AnsiCodes):
    BLACK: int
    RED: int
    GREEN: int
    YELLOW: int
    BLUE: int
    MAGENTA: int
    CYAN: int
    WHITE: int
    RESET: int
    LIGHTBLACK_EX: int
    LIGHTRED_EX: int
    LIGHTGREEN_EX: int
    LIGHTYELLOW_EX: int
    LIGHTBLUE_EX: int
    LIGHTMAGENTA_EX: int
    LIGHTCYAN_EX: int
    LIGHTWHITE_EX: int

class AnsiStyle(AnsiCodes):
    BRIGHT: int
    DIM: int
    NORMAL: int
    RESET_ALL: int

Fore: Incomplete
Back: Incomplete
Style: Incomplete
Cursor: Incomplete
