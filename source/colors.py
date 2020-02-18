class color:
# Main format
# Text Colors
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'

# Text Style
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# Text Colors Quick Print Feature
# just made some modis to the main color format for bit quicker typing if you want some colors
# for text or #'s, will test out other ways making this process a bit faster
purple = color.PURPLE
cyan = color.CYAN
dark_cyan = color.DARKCYAN
blue = color.BLUE
green = color.GREEN
yellow = color.YELLOW
red = color.RED
unknown_color = '~redacted color~ '

# Text Style
bold = color.BOLD
underline = color.UNDERLINE
end = color.END
combo_underline_yellow = underline + yellow

# Package Colors Info
# https://godoc.org/github.com/whitedevops/colors

