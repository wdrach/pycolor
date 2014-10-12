#!/usr/bin/python3 -B

# a few import things
import random
import sys
from sys import stdout

VERSION = '1.2.0'

escape = '\033['

## General things about Ansii escape sequences
# 256 color sequence
# foreground \033[38;5;NNNm
# background \033[48;5;NNNm
# where NNN is a integer between 0t o 256, inclusive
#
# 3 sets of colors in the 256 color sequence
# first set is basic color set, from 0-15.
# second set is a cube of distributed colors from 16-231.
# third set is a grayscale set, from 232-256.
# black:  0
# white:  256

# attribute sequences \033[Nm
# where N is: 
#reset = 0
#bold  = 1
#dim   = 2
#foreground = 3x (0 <= x <= 9, not 8)
#background = 4x (0 <= x <= 9, not 8)
#underline  = 4
#blink      = 5
#negative   = 7
#hidden     = 8

# Full colors is a list of all of the 256 colors
full_colors = {'black': '0', 'red': '1', 'green': '2', 'yellow': '3',
               'blue': '4', 'magenta': '5', 'cyan': '6', 'white': '7',
               'lightred': '9', 'lightgreen': '10',
               'lightyellow': '11', 'lightblue': '12',
               'lightmagenta': '13', 'lightcyan': '14',
               'grey0': '016', 'navyblue': '017', 'darkblue': '018',
               'blue3': '019', 'blue3': '020', 'blue1': '021',
               'darkgreen': '022', 'deepskyblue4': '023',
               'deepskyblue4': '024', 'deepskyblue4': '025',
               'dodgerblue3': '026', 'dodgerblue2': '027',
               'green4': '028', 'springgreen4': '029',
               'turquoise4': '030', 'deepskyblue3': '031',
               'deepskyblue3': '032', 'dodgerblue1': '033',
               'green3': '034', 'springgreen3': '035',
               'darkcyan': '036', 'lightseagreen': '037',
               'deepskyblue2': '038', 'deepskyblue1': '039',
               'green3': '040', 'springgreen3': '041',
               'springgreen2': '042', 'cyan3': '043',
               'darkturquoise': '044', 'turquoise2': '045',
               'green1': '046', 'springgreen2': '047',
               'springgreen1': '048', 'mediumspringgreen': '049',
               'cyan2': '050', 'cyan1': '051', 'darkred': '052',
               'deeppink4': '053', 'purple4': '054', 'purple4': '055',
               'purple3': '056', 'blueviolet': '057',
               'orange4': '058', 'grey37': '059',
               'mediumpurple4': '060', 'slateblue3': '061',
               'slateblue3': '062', 'royalblue1': '063',
               'chartreuse4': '064', 'darkseagreen4': '065',
               'paleturquoise4': '066', 'steelblue': '067',
               'steelblue3': '068', 'cornflowerblue': '069',
               'chartreuse3': '070', 'darkseagreen4': '071',
               'cadetblue': '072', 'cadetblue': '073',
               'skyblue3': '074', 'steelblue1': '075',
               'chartreuse3': '076', 'palegreen3': '077',
               'seagreen3': '078', 'aquamarine3': '079',
               'mediumturquoise': '080', 'steelblue1': '081',
               'chartreuse2': '082', 'seagreen2': '083',
               'seagreen1': '084', 'seagreen1': '085',
               'aquamarine1': '086', 'darkslategray2': '087',
               'darkred': '088', 'deeppink4': '089',
               'darkmagenta': '090', 'darkmagenta': '091',
               'darkviolet': '092', 'purple': '093', 'orange4': '094',
               'lightpink4': '095', 'plum4': '096',
               'mediumpurple3': '097', 'mediumpurple3': '098',
               'slateblue1': '099', 'yellow4': '100', 'wheat4': '101',
               'grey53': '102', 'lightslategrey': '103',
               'mediumpurple': '104', 'lightslateblue': '105',
               'yellow4': '106', 'darkolivegreen3': '107',
               'darkseagreen': '108', 'lightskyblue3': '109',
               'lightskyblue3': '110', 'skyblue2': '111',
               'chartreuse2': '112', 'darkolivegreen3': '113',
               'palegreen3': '114', 'darkseagreen3': '115',
               'darkslategray3': '116', 'skyblue1': '117',
               'chartreuse1': '118', 'lightgreen': '119',
               'lightgreen': '120', 'palegreen1': '121',
               'aquamarine1': '122', 'darkslategray1': '123',
               'red3': '124', 'deeppink4': '125',
               'mediumvioletred': '126', 'magenta3': '127',
               'darkviolet': '128', 'purple': '129',
               'darkorange3': '130', 'indianred': '131',
               'hotpink3': '132', 'mediumorchid3': '133',
               'mediumorchid': '134', 'mediumpurple2': '135',
               'darkgoldenrod': '136', 'lightsalmon3': '137',
               'rosybrown': '138', 'grey63': '139',
               'mediumpurple2': '140', 'mediumpurple1': '141',
               'gold3': '142', 'darkkhaki': '143',
               'navajowhite3': '144', 'grey69': '145',
               'lightsteelblue3': '146', 'lightsteelblue': '147',
               'yellow3': '148', 'darkolivegreen3': '149',
               'darkseagreen3': '150', 'darkseagreen2': '151',
               'lightcyan3': '152', 'lightskyblue1': '153', 
               'greenyellow': '154', 'darkolivegreen2': '155',
               'palegreen1': '156', 'darkseagreen2': '157',
               'darkseagreen1': '158', 'paleturquoise1': '159',
               'red3': '160', 'deeppink3': '161', 'deeppink3': '162',
               'magenta3': '163', 'magenta3': '164',
               'magenta2': '165', 'darkorange3': '166',
               'indianred': '167', 'hotpink3': '168',
               'hotpink2': '169', 'orchid': '170',
               'mediumorchid1': '171', 'orange3': '172',
               'lightsalmon3': '173', 'lightpink3': '174',
               'pink3': '175', 'plum3': '176', 'violet': '177',
               'gold3': '178', 'lightgoldenrod3': '179', 'tan': '180',
               'mistyrose3': '181', 'thistle3': '182', 'plum2': '183',
               'yellow3': '184', 'khaki3': '185',
               'lightgoldenrod2': '186', 'lightyellow3': '187',
               'grey84': '188', 'lightsteelblue1': '189',
               'yellow2': '190', 'darkolivegreen1': '191',
               'darkolivegreen1': '192', 'darkseagreen1': '193',
               'honeydew2': '194', 'lightcyan1': '195', 'red1': '196',
               'deeppink2': '197', 'deeppink1': '198',
               'deeppink1': '199', 'magenta2': '200',
               'magenta1': '201', 'orangered1': '202',
               'indianred1': '203', 'indianred1': '204',
               'hotpink': '205', 'hotpink': '206',
               'mediumorchid1': '207', 'darkorange': '208',
               'salmon1': '209', 'lightcoral': '210',
               'palevioletred1': '211', 'orchid2': '212',
               'orchid1': '213', 'orange1': '214',
               'sandybrown': '215', 'lightsalmon1': '216',
               'lightpink1': '217', 'pink1': '218', 'plum1': '219',
               'gold1': '220', 'lightgoldenrod2': '221',
               'lightgoldenrod2': '222', 'navajowhite1': '223',
               'mistyrose1': '224', 'thistle1': '225',
               'yellow1': '226', 'lightgoldenrod1': '227',
               'khaki1': '228', 'wheat1': '229', 'cornsilk1': '230',
               'grey100': '231', 'grey3': '232', 'grey7': '233',
               'grey11': '234', 'grey15': '235', 'grey19': '236',
               'grey23': '237', 'grey27': '238', 'grey30': '239',
               'grey35': '240', 'grey39': '241', 'grey42': '242',
               'grey46': '243', 'grey50': '244', 'grey54': '245',
               'grey58': '246', 'grey62': '247', 'grey66': '248',
               'grey70': '249', 'grey74': '250', 'grey78': '251',
               'grey82': '252', 'grey85': '253', 'grey89': '254',
               'grey93': '255'}


# these are the 256 colors that go in a sorta rainbow order
_rainbow_256 = [196, 202, 208, 214, 220, 226, 190, 154, 118, 82, 46,
                47, 48, 49, 50, 51, 45, 39, 33, 27, 21, 57, 93, 129,
                165, 201, 129, 21, 33, 45, 50, 47, 82, 154, 226, 208]

class fg(object):
    '''A set of ansi escape sequences
       for foreground colors'''

    # escape sequence, need m at the end of the color
    fg_escape = escape + '38;5;'

    # reset sequence
    reset = escape + '39m'
    re    = escape + '39m'

    # long names and sequences
    black   = '\033[38;5;0m'
    red     = '\033[38;5;1m'
    green   = '\033[38;5;2m'
    yellow  = '\033[38;5;3m'
    blue    = '\033[38;5;4m'
    magenta = '\033[38;5;5m'
    cyan    = '\033[38;5;6m'
    white   = '\033[38;5;7m'

    # long light colors
    lightred     = '\033[38;5;9m'
    lightgreen   = '\033[38;5;10m'
    lightyellow  = '\033[38;5;11m'
    lightblue    = '\033[38;5;12m'
    lightmagenta = '\033[38;5;13m'
    lightcyan    = '\033[38;5;14m'

    # short names
    b  = '\033[38;5;0m'
    r  = '\033[38;5;1m'
    g  = '\033[38;5;2m'
    y  = '\033[38;5;3m'
    bl = '\033[38;5;4m'
    m  = '\033[38;5;5m'
    c  = '\033[38;5;6m'
    w  = '\033[38;5;7m'

    # short light colors
    lr = '\033[38;5;9m'
    lg = '\033[38;5;10m'
    ly = '\033[38;5;11m'
    lb = '\033[38;5;12m'
    lm = '\033[38;5;13m'
    lc = '\033[38;5;14m'

class bg(object):
    '''A set of ansi escape sequences
       for background colors'''

    # escape sequence, need m at the end of the color
    bg_escape = escape + '48;5;'

    # reset sequence/ reset shortname
    reset = escape + '49m'
    re    = escape + '49m'

    # long names
    black   = '\033[48;5;0m'
    red     = '\033[48;5;1m'
    green   = '\033[48;5;2m'
    yellow  = '\033[48;5;3m'
    blue    = '\033[48;5;4m'
    magenta = '\033[48;5;5m'
    cyan    = '\033[48;5;6m'
    white   = '\033[48;5;7m'

    # long light colors
    lightred     = '\033[48;5;9m'
    lightgreen   = '\033[48;5;10m'
    lightyellow  = '\033[48;5;11m'
    lightblue    = '\033[48;5;12m'
    lightmagenta = '\033[48;5;13m'
    lightcyan    = '\033[48;5;14m'

    # short names
    b  = '\033[48;5;0m'
    r  = '\033[48;5;1m'
    g  = '\033[48;5;2m'
    y  = '\033[48;5;3m'
    bl = '\033[48;5;4m'
    m  = '\033[48;5;5m'
    c  = '\033[48;5;6m'
    w  = '\033[48;5;7m'

    # short light colors
    lr = '\033[48;5;9m'
    lg = '\033[48;5;10m'
    ly = '\033[48;5;11m'
    lb = '\033[48;5;12m'
    lm = '\033[48;5;13m'
    lc = '\033[48;5;14m'

class atr(object):
    '''various attribute escape sequences'''

    # long names
    reset_all = escape + '0m'
    bold      = escape + '1m'
    dim       = escape + '2m'
    underline = escape + '4m'
    blink     = escape + '6m'
    negative  = escape + '2m'

    # short names
    ra = escape + '0m'
    bo = escape + '1m'
    d  = escape + '2m'
    ul = escape + '4m'
    bl = escape + '6m'
    n  = escape + '2m'

def reset_all():
    '''reset all attributes, formatting and colors'''

    #return reset sequence
    return escape + '0' + 'm'

def get_bold():
    '''returns a bold (aka bright) color sequence (string)'''

    return escape + '1' + 'm'


def get_dim():
    '''returns a dim color sequence'''

    return escape + '2' + 'm'


def get_underline():
    '''returns an "underlined text" sequence '''

    return escape + '4' + 'm'


def get_blink(speed):
    '''returns a blinking text sequence with a specified speed'''

    if speed == 1:
        return escape + '6' + 'm'
    else:
        return escape + '5' + 'm'


def get_negative():
    '''returns a "negative" escape sequence'''

    return escape + '2' + 'm'

def get_color_esc(attribute, color):
    '''returns a terminal escape sequence (string)
       for the specified attribute and color

       attribute is either fg or bg

       color is any valid xterm 256 color name or
       a number between 0 and 256
    '''

    if attribute == 'fg':
        coloresc = escape + '38;5;'
    elif attribute == 'bg':
        coloresc = escape + '48;5;'

    if type(color) is int:
        if color < 0:
            color = 0
        elif color > 256:
            color = 256
        return(coloresc + str(color) + 'm')

    elif type(color) is str:
        try:
            return(coloresc + full_colors[color.lower()] + 'm')
        except KeyError:
            return('\033[0m')

def make_rainbow(string, style='word', width=1, start_color='rand'):
    '''returns the original string mixed with terminal escape
       sequences

       style can be any character or the string 'char(acter)' 'word'
       'line', and indicates when the function will change to the next
       color

       width specifies the number of "styles" before a color change
       and can be an interger of any size or the string (r)andom

       start_color is the starting color, which can be any of the xterm 256
       color names, or a number between 0 and 256, always starts with red

    '''

    try:
        # different color starting points
        # for different "rainbow" colors
        if start_color == 'red':
            rainbow_count = 10
        elif start_color == 'rand':
            rainbow_count = random.randint(0, 35)
        else:
            rainbow_count = 0
    except:
        rainbow_count = 0

    return_string = ''
    double = 0

    for letter in string:
        rs = return_string + escape + '38;5;'
        return_string = rs + (str(_rainbow_256[rainbow_count])) +\
                        'm' + letter
        string = string[2:]
        if double == 0:
            double = 1
        else:
            double = 0
            rainbow_count = rainbow_count + 1
        if rainbow_count == len(_rainbow_256):
            rainbow_count = 0

    reset = reset_all()
    return(return_string + reset)


def color_string(string,
                 attribute = 'none',
                 fg_color  = 'none',
                 bg_color  = 'none'):

    '''return a terminal escape sequence encapsulated string with the 
       specified attribute and color, or returns just the string if the
       attribute or color is empty

       attribute can be any of fg, foreground, bg, background, bold,
       none, dim, underline, blink, reverse.

       color can be any of the valid xterm 256 color names, a number
       between 1 and 256, the string rand(om), or rainbow.
    '''

    # coloresc:  color escape sequence
    coloresc = ''
    # modesc:  modifier escape sequence. bold, fg, negative, etc.
    modesc = ''
    # reset: the appropriate reset escape sequence
    reset = ''

    # possible color options
    if fg_color == 'rand' or fg_color == 'random':
        fg_color = random.randint(1,256)

    if bg_color == 'rand' or bg_color == 'random':
        bg_color = random.randint(1,256)

    # print a rainbow!
    elif fg_color == 'rainbow':
        return make_rainbow(string)

    if fg_color != 'none':
        coloresc = coloresc + get_color_esc('fg', fg_color)
        reset = reset_all()

    if bg_color != 'none':
        coloresc = coloresc + get_color_esc('bg', bg_color)
        reset = reset_all()

    # attributes
    if attribute == 'bold':
        modesc = get_bold()
    elif attribute == 'dim':
        modesc = get_dim()
    elif attribute == 'underline':
        modesc = get_underline()
    elif attribute == 'blink':
        modesc = get_blink(0)
    elif attribute == 'negative':
        modesc = get_negative()

    return(modesc + coloresc + string + reset)

def print_color(string,
                 attribute = 'none',
                 fg_color  = 'none',
                 bg_color  = 'none'):

    '''print the string in color'''

    print(color_string(string,
                       attribute = attribute,
                       fg_color  = fg_color,
                       bg_color  = bg_color))
    return


if __name__ == '__main__':
    n = 0
    for item in range(0,256):
      if n == 18:
        n = 0
        print('')
      stdout.write(color_string(' {0:3d} '.format(item), bg_color=int(item)))
      n = n + 1
    print('')
