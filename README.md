pycolor
=======

A color module for python

# Intro
Ansi color in python sucks. You basically have a handful of options, all of which have their benefits but none of which really get the job done.

* Colorama
	* Colorama is good, but it has limited color support (8 colors...)
* Termcolor
	* Termcolor is basically Colorama without Windows support (8 colors, again)
* Fabulous
	* Fabulous seems cool, but it is questionable whether or not it is kept up to date
* Blessings
	* Blessings is way too complicated

With pycolor you can kinda do whatever you want and it'll work. 256 color support and attribute support, as well as the typical 8 color support. We also do rainbow, because we're gangster like that.

# Examples
#### print blue text
```python
import color
from color import color_string
our_string = 'Testing that color module'
print_color(our_string, fg_color = 'blue')
```

#### return rainbows, and then print that to stderr

##### (gotta have some fun reading old logs right?)

```python
import color
import sys
from color import color_string
from sys import stderr
print('nyan')
error_nyan = color_string('ERROR! Unexpected Nyan\n', fg_color = 'rainbow')
stderr.write(error_nyan)
```

#### print some black text on white background

```python
import color
from color import print_color
print_color('some black text on white background',
            fg_color = 'black',
            bg_color = 'white')
```

# Functions
#### fg (object):

	`fg` is an object within color that will return a simple escape sequence for a specified color. fg is only meant to be used with the standard 16 colors (black, red, green, yellow, blue, magenta, cyan, white, lightred, lightgreen, lightyellow, lightblue, lightmagenta, lightcyan). To set the escape sequence just call `fg.color` (i.e. `fg.lightblue`). The reset sequence can be called by `fg.reset` or just `fg.re`. Lastly, you can call colors by their one or two letter designation (b, r, g, y, bl, m, c, w, lr, lg, ly, lb, lm, lc, respectively) in the same manner (i.e. `fg.lb`)

#### bg (object):

	`bg` is exactly the same in every way as fg, except it returns the background escape sequence instead of the foreground escape sequence

#### atr (object):

	`atr` works similarly to bg and fg, except it is for attributes. Supported attributes are reset_all, bold, dim, underline, blink, and negative. The short names are ra, bo, d, ul, bl, and n respectively

#### reset_all:

	`reset_all` resets all attributes, formatting, and colors. Usually only used internally, but can be usefull nonetheless

#### get_bold, get_dim, get_underline, get_blink(speed), get_negative:

	These get functions return their respective escape sequences. `get_blink` takes a single input being the speed (which is either 0 or 1)

#### get_color_esc(attribute, color):

	`get_color_esc` returns the escape sequence for the given color. It takes two variables, attribute, which is either `'fg'` or `'bg'`, and the color, which can be a number from 0 to 256 or a valid xterm 256 color name

#### make_rainbow(string, start_color='rand'):

	`make_rainbow` is mostly for internal use, use color_string(fg_color = 'rainbow') or print_color(fg_color = 'rainbow')

#### color_string(string, attribute = 'none', fg_color = 'none', bg_color = 'none'):

	`color_string` takes a variety of variables to return a string that is coupled with various escape sequences. Attribute is one of the attributes in atr (ra, bo, d, ul, bl). Similarly `fg_color` and `bg_color` can be set to any color from `get_color_esc`. `string` is simply the string you want colored.

#### print_color(string, attribute = 'none', fg_color = 'none', bg_color = 'none'):

	`print_color` works exactly the same as `color_string` except for instead of returning the string it prints it to stdout.


