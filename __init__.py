import ctypes
from time import sleep
from math import sqrt
from . import Keys

DictKey=Keys.DictKey
Alt_Code=Keys.Alt_Code
Numerical=Keys.Numerical

SendInput = ctypes.windll.user32.SendInput


# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


from ctypes import windll, Structure, c_long, byref


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def getPosCursor():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return [pt.x, pt.y]


def click(x: list or tuple, y: int = None, RIGHT: bool = False):
    """
    Moves the mouse cursor to the specified (x, y) position or the position specified in a list or tuple.
    If RIGHT is True, performs a right-click instead of a left-click.
    
    Parameters:
    x (int or list/tuple): The x-coordinate or the position as a list or tuple.
    y (int): The y-coordinate. Defaults to 0 if not provided.
    RIGHT (bool): Whether to perform a right-click. Defaults to False.
    """

    if isinstance(x, list) or isinstance(x, tuple):
        x, y = int(x[0]), int(x[1])
    else:
        x, y = int(x), int(y)

    ctypes.windll.user32.SetCursorPos(x, y)

    if RIGHT:
        ctypes.windll.user32.mouse_event(0x0008, 0, 0, 0, 0)  # right down
        ctypes.windll.user32.mouse_event(0x0010, 0, 0, 0, 0)  # right up
    else:
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left down
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # left up


def moveMouseTo(FirstPos: list or tuple, SecondPos: list or tuple, pps: int = 300, step: int = 1, max_time: float = 10, info: bool=False):
    """
    Move the mouse from the first position to the second position with a certain speed and step.

    :param FirstPos (list or tuple): a list or tuple containing the coordinates (x, y) of the first position.
    :param SecondPos (list or tuple): a list or tuple containing the coordinates (x, y) of the second position.
    :param pps (int, optional): the speed of movement in pixels per second. Defaults to 300.
    :param step (int, optional): the number of pixels to move the mouse for each step. Defaults to 1.
    :param max_time (float, optional): the maximum time allowed for the movement to complete in seconds. Defaults to 10.
    """

    x1, y1 = FirstPos
    ctypes.windll.user32.SetCursorPos(x1, y1)
    x2, y2 = SecondPos
    distance = round(sqrt((x2 - x1)**2 + (y2 - y1)**2))
    time_per_step = 1 / pps
    total_time = distance * time_per_step
    if total_time > max_time:
        time_per_step = max_time / distance
        print(time_per_step)
        if info: print(f"Total time ({total_time:.2f}s) exceeds max_time ({max_time}s). Adjusted pps to {int(1 / time_per_step)} pixels/s.")
    steps = max(distance // 1, 1)
    dx = (x2 - x1) / steps
    dy = (y2 - y1) / steps
    sleep_per_step = time_per_step
    for i in range(steps):
        x = int(x1 + i*dx)
        y = int(y1 + i*dy)
        ctypes.windll.user32.SetCursorPos(x, y)
        sleep(sleep_per_step)


def clickDown():
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)

def clickUp():
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)

def clickTo(a_x, a_y , b_x, b_y):
    ctypes.windll.user32.SetCursorPos(a_x, a_y)
    sleep(0.001)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    ctypes.windll.user32.SetCursorPos(b_x, b_y)
    sleep(0.001)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)


def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def SpeChar(Char,ReplaceNotExist="."):
    if type(Char) != str:
        Char = str(Char)

    Fonction('P','Alt_L')
    try:
        for i in Alt_Code[Char]:
            Hex = Numerical[i]
            PressKey(Hex);ReleaseKey(Hex)
            sleep(0.0000000000000001)
        print("")
    except Exception as e:
        print(e)
        print(f'[{Char}] not exist and is replace by [{ReplaceNotExist}]')
    Fonction('R','Alt_L')


def Fonction(POR='PR',Fonc='MAJ_L'):
    ''' 
    POR:
        'PR' = Press & Release,
        'P' = Press,
        'R' = Release
    Fonc:
        'MAJ_L','MAJ_R',
        'Alt_L','CTRL_L',
        'ENTER','TAB',
        'Back_Space','Caps_Lock',
        'Num_Lock','Scroll_Lock' 
    '''

    for i in [Fonc]:
        if POR == 'PR':
            PressKey(DictKey[i]);ReleaseKey(DictKey[i])
        elif POR == 'P':
            PressKey(DictKey[i])
        elif POR == 'R':
            ReleaseKey(DictKey[i])
        sleep(0.0000000000000001)


def Write(text: str = '', MAJ: bool = False, ALT: bool = False, CTRL: bool = False, ReplaceNotExist: str = '.') -> None:
    """
    This function simulates the typing of a given text by pressing the corresponding keys.
    :param text: The text to be typed (default: '')
    :param MAJ: A boolean indicating whether the Shift key should be pressed during typing of text (default: False)
    :param ALT: A boolean indicating whether the Alt key should be pressed during typing of text (default: False)
    :param CTRL: A boolean indicating whether the Ctrl key should be pressed during typing of text (default: False)
    :param ReplaceNotExist: The character to replace non-existent characters in DictKey (default: '.')
    """
    if type(text) != str:
        text = str(text)
    for i in text:
        if (i.upper()) in DictKey:
            Fonction('P','MAJ_L') if MAJ else ...
            Fonction('P','Alt_L') if ALT else ...
            Fonction('P','CTRL_L') if CTRL else ...
            try:
                Hex = DictKey[i.upper()]
            except:
                Hex = DictKey[ReplaceNotExist]
                print(f'[{i}] not exist and is replace by [{ReplaceNotExist}]')
            sleep(0.0000000000000001)
            if i.isupper():
                Fonction('P','MAJ_L')
                PressKey(Hex)
                ReleaseKey(Hex)
                Fonction('R','MAJ_L')
            else:
                PressKey(Hex)
                ReleaseKey(Hex)
            Fonction('R','MAJ_L') if MAJ else ...
            Fonction('R','Alt_L') if ALT else ...
            Fonction('R','CTRL_L') if CTRL else ...
        else:
            SpeChar(i,ReplaceNotExist)



def Copy(All=False,Cut=False):
    if All:
        Fonction('P','CTRL_L');PressKey(DictKey['A'])
        Fonction('R','CTRL_L');ReleaseKey(DictKey['A'])
    if Cut:
        Fonction('P','CTRL_L');PressKey(DictKey['X'])
        Fonction('R','CTRL_L');ReleaseKey(DictKey['X'])
    else:
        Fonction('P','CTRL_L');PressKey(DictKey['C'])
        Fonction('R','CTRL_L');ReleaseKey(DictKey['C'])


def Paste(ReplaceAll=False):
    if ReplaceAll:
        Fonction('P','CTRL_L');PressKey(DictKey['A'])
        Fonction('R','CTRL_L');ReleaseKey(DictKey['A'])
    Fonction('P','CTRL_L');PressKey(DictKey['V'])
    Fonction('R','CTRL_L');ReleaseKey(DictKey['V'])


def BackSpace(iteration=1):
    for i in range(iteration):
        Fonction('PR','Back_Space')
