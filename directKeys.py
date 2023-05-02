import ctypes
from curses.ascii import isupper
from time import sleep
from math import sqrt


DictKey= {
    '0':0x0B,
    '1':0x02,
    '2':0x03,
    '3':0x04,
    '4':0x05,
    '5':0x06,
    '6':0x07,
    '7':0x08,
    '8':0x09,
    '9':0x0A,
    'TAB':0x0F,
    '-':0x0C,
    '=':0x0D,
    'Back_Space':0x0E,
    'Q':0x10,
    'W':0x11,
    'E':0x12,
    'R':0x13,
    'T':0x14,
    'Y':0x15,
    'U':0x16,
    'I':0x17,
    'O':0x18,
    'P':0x19,
    '[':0x1A,
    ']':0x1B,
    'ENTER':0x1C,
    'CTRL_L':0x1D,
    'A':0x1E,
    'S':0x1F,
    'D':0x20,
    'F':0x21,
    'G':0x22,
    'H':0x23,
    'J':0x24,
    'K':0x25,
    'L':0x26,
    ';':0x27,
    "'":0x28,
    '`':0x29,
    'MAJ_L':0x2A,
    '\\':0x2B,
    'Z':0x2C,
    'X':0x2D,
    'C':0x2E,
    'V':0x2F,
    'B':0x30,
    'N':0x31,
    'M':0x32,
    ',':0x33,
    '.':0x34,
    '/':0x35,
    'MAJ_R':0x36,
    '*':0x37,
    'Alt_L':0x38,
    ' ':0x39,
    'Caps_Lock':0x3A,
    'F1':0x3B,
    'F2':0x3C,
    'F3':0x3D,
    'F4':0x3E,
    'F5':0x3F,
    'F6':0x40,
    'F7':0x41,
    'F8':0x42,
    'F9':0x43,
    'F10':0x44,
    'Num_Lock':0x45,
    'Scroll_Lock':0x46,
    'F11':0x57,
    'F12':0x58,
    'F13':0x64,
    'F14':0x65,
    'F15':0x66,
}

DictKeySpe = {
    '0':0x52,
    '1':0x4F,
    '2':0x50,
    '3':0x51,
    '4':0x4B,
    '5':0x4C,
    '6':0x4D,
    '7':0x47,
    '8':0x48,
    '9':0x49,
    'à':'0224',
    'á':'0225',
    'â':'0226',
    'ã':'0227',
    'ä':'0228',
    'ç':'0231',
    'è':'0232',
    'é':'0233',
    'ê':'0234',
    'ë':'0235',
    'ì':'0236',
    'í':'0237',
    'î':'0238',
    'ï':'0239',
    'ñ':'164',
    'ò':'0242',
    'ó':'0243',
    'ô':'0244',
    'õ':'0245',
    'ö':'0246',
    'š':'0154',
    'ù':'0249',
    'ú':'0250',
    'û':'0251',
    'ü':'0252',
    'ý':'0253',
    'ÿ':'0255',
    'ž':'0158',
    'À':'0192',
    'Á':'0193',
    'Â':'0194',
    'Ã':'0195',
    'Ä':'0196',
    'Ç':'0199',
    'È':'0200',
    'É':'0201',
    'Ê':'0202',
    'Ë':'0203',
    'Ì':'0204',
    'Í':'0205',
    'Î':'0206',
    'Ï':'0207',
    'Ñ':'165',
    'Ò':'0210',
    'Ó':'0211',
    'Ô':'0212',
    'Õ':'0213',
    'Ö':'0214',
    'Š':'0138',
    'Ú':'0218',
    'Û':'0219',
    'Ü':'0220',
    'Ù':'0217',
    'Ý':'0221',
    'Ÿ':'0159',
    'Ž':'0142',
    '€':'0128',
    '☺':'1',
    '☻':'2',
    '♥':'3',
    '♦':'4',
    '♣':'5',
    '♠':'6',
    '•':'7',
    '◘':'8',
    '○':'9',
    '◙':'10',
    '♂':'11',
    '♀':'12',
    '♪':'13',
    '♫':'14',
    '☼':'15',
    '►':'16',
    '◄':'17',
    '↕':'18',
    '‼':'19',
    '¶':'20',
    '§':'21',
    '▬':'22',
    '↨':'23',
    '↑':'24',
    '↓':'25',
    '→':'26',
    '←':'27',
    '∟':'28',
    '↔':'29',
    '▲':'30',
    '▼':'31',
    '!':'33',
    '#':'35',
    '$':'36',
    '%':'37',
    '&':'38',
    "'":'39',
    '(':'40',
    ')':'41',
    '*':'42',
    '+':'43',
    ',':'44',
    '-':'45',
    '.':'46',
    '/':'47',
    ':':'58',
    ';':'59',
    '<':'60',
    '=':'61',
    '>':'62',
    '?':'63',
    '@':'64',
    '[':'91',
    '\\':'92',
    ']':'93',
    '^':'94',
    '_':'95',
    '`':'96',
    '{':'123',
    '|':'124',
    '}':'125',
    '~':'126',
    'Δ':'127',
    '¢':'155',
    '£':'156',
    '¥':'157',
    '₧':'158',
    'ƒ':'159',
    'ª':'166',
    'º':'167',
    '¿':'168',
    '®':'169',
    '¬':'170',
    '½':'171',
    '¼':'172',
    '¡':'173',
    '«':'174',
    '»':'175',
    '░':'176',
    '▒':'177',
    '▓':'178',
    '│':'179',
    '┤':'180',
    '╡':'181',
    '╢':'182',
    '╖':'183',
    '╕':'184',
    '╣':'185',
    '║':'186',
    '╗':'187',
    '╝':'188',
    '╜':'189',
    '╛':'190',
    '┐':'191',
    '└':'192',
    '┴':'193',
    '┯':'194',
    '├':'195'
}


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


def moveMouseTo(FirstPos: list or tuple, SecondPos: list or tuple, pps: int = 300, step: int = 1):
    """
    Move the mouse from the first position to the second position with a certain speed and step.

    :param FirstPos (list or tuple): a list or tuple containing the coordinates (x, y) of the first position.
    :param SecondPos (list or tuple): a list or tuple containing the coordinates (x, y) of the second position.
    :param pps (int, optional): the speed of movement in pixels per second. Defaults to 300.
    :param step (int, optional): the number of pixels to move the mouse for each step. Defaults to 1.
    """

    x1, y1 = FirstPos
    ctypes.windll.user32.SetCursorPos(x1, y1)
    x2, y2 = SecondPos
    distance = round(sqrt((x2 - x1)**2 + (y2 - y1)**2))
    steps = max(distance // step, 1)
    dx = (x2 - x1) / steps
    dy = (y2 - y1) / steps
    time_per_step = 1 / pps
    total_time = distance * time_per_step
    sleep_per_step = total_time / steps
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
        for i in DictKeySpe[Char]:
            Hex = DictKeySpe[i]
            PressKey(Hex);ReleaseKey(Hex)
            sleep(0.0000000000000001)
    except:
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
