from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np
import cv2
from color import Color


class ColorLabeler:

    def __init__(self):
        # initialize the colors dictionary, containing the color
        # name as the key and the RGB tuple as the value
        colors = OrderedDict({
            Color.beige: (0xB8, 0x86, 0x0B),
            Color.white: (0xFF, 0xFF, 0xFF),
            Color.red: (0xFF, 0x00, 0x00),
            Color.dark_orange: (0xFF, 0x8C, 0x00),
            Color.green: (0x00, 0x80, 0x00),
            Color.yellow: (0xFF, 0xFF, 0x00),

            # "DarkGreen": (0x00, 0x64, 0x00),
            # "LightGreen": (0x90, 0xEE, 0x90),
            # "Gray": (0x80, 0x80, 0x80),
            # "Orange": (0xFF, 0xA5, 0x00),
            # "LightGray": (0xD3, 0xD3, 0xD3),
            # "AliceBlue": (0xF0, 0xF8, 0xFF),
            # "AntiqueWhite": (0xFA, 0xEB, 0xD7),
            # "Aqua": (0x00, 0xFF, 0xFF),
            # "Aquamarine": (0x7F, 0xFF, 0xD4),
            # "Azure": (0xF0, 0xFF, 0xFF),
            # "Beige": (0xF5, 0xF5, 0xDC),
            # "Bisque": (0xFF, 0xE4, 0xC4),
            # "Black": (0x00, 0x00, 0x00),
            # "BlanchedAlmond": (0xFF, 0xEB, 0xCD),
            # "Blue": (0x00, 0x00, 0xFF),
            # "BlueViolet": (0x8A, 0x2B, 0xE2),
            # "Brown": (0xA5, 0x2A, 0x2A),
            # "BurlyWood": (0xDE, 0xB8, 0x87),
            # "CadetBlue": (0x5F, 0x9E, 0xA0),
            # "Chartreuse": (0x7F, 0xFF, 0x00),
            # "Chocolate": (0xD2, 0x69, 0x1E),
            # "Coral": (0xFF, 0x7F, 0x50),
            # "CornflowerBlue": (0x64, 0x95, 0xED),
            # "Cornsilk": (0xFF, 0xF8, 0xDC),
            # "Crimson": (0xDC, 0x14, 0x3C),
            # "Cyan": (0x00, 0xFF, 0xFF),
            # "DarkBlue": (0x00, 0x00, 0x8B),
            # "DarkCyan": (0x00, 0x8B, 0x8B),
            # "DarkGray": (0xA9, 0xA9, 0xA9),
            # "DarkGrey": (0xA9, 0xA9, 0xA9),
            # "DarkKhaki": (0xBD, 0xB7, 0x6B),
            # "DarkMagenta": (0x8B, 0x00, 0x8B),
            # "DarkOliveGreen": (0x55, 0x6B, 0x2F),
            # "DarkOrchid": (0x99, 0x32, 0xCC),
            # "DarkRed": (0x8B, 0x00, 0x00),
            # "DarkSalmon": (0xE9, 0x96, 0x7A),
            # "DarkSeaGreen": (0x8F, 0xBC, 0x8F),
            # "DarkSlateBlue": (0x48, 0x3D, 0x8B),
            # "DarkSlateGray": (0x2F, 0x4F, 0x4F),
            # "DarkSlateGrey": (0x2F, 0x4F, 0x4F),
            # "DarkTurquoise": (0x00, 0xCE, 0xD1),
            # "DarkViolet": (0x94, 0x00, 0xD3),
            # "DeepPink": (0xFF, 0x14, 0x93),
            # "DeepSkyBlue": (0x00, 0xBF, 0xFF),
            # "DimGray": (0x69, 0x69, 0x69),
            # "DimGrey": (0x69, 0x69, 0x69),
            # "DodgerBlue": (0x1E, 0x90, 0xFF),
            # "FireBrick": (0xB2, 0x22, 0x22),
            # "FloralWhite": (0xFF, 0xFA, 0xF0),
            # "ForestGreen": (0x22, 0x8B, 0x22),
            # "Fuchsia": (0xFF, 0x00, 0xFF),
            # "Gainsboro": (0xDC, 0xDC, 0xDC),
            # "GhostWhite": (0xF8, 0xF8, 0xFF),
            # "Gold": (0xFF, 0xD7, 0x00),
            # "GoldenRod": (0xDA, 0xA5, 0x20),
            # "Grey": (0x80, 0x80, 0x80),
            # "GreenYellow": (0xAD, 0xFF, 0x2F),
            # "HoneyDew": (0xF0, 0xFF, 0xF0),
            # "HotPink": (0xFF, 0x69, 0xB4),
            # "IndianRed": (0xCD, 0x5C, 0x5C),
            # "Indigo": (0x4B, 0x00, 0x82),
            # "Ivory": (0xFF, 0xFF, 0xF0),
            # "Khaki": (0xF0, 0xE6, 0x8C),
            # "Lavender": (0xE6, 0xE6, 0xFA),
            # "LavenderBlush": (0xFF, 0xF0, 0xF5),
            # "LawnGreen": (0x7C, 0xFC, 0x00),
            # "LemonChiffon": (0xFF, 0xFA, 0xCD),
            # "LightBlue": (0xAD, 0xD8, 0xE6),
            # "LightCoral": (0xF0, 0x80, 0x80),
            # "LightCyan": (0xE0, 0xFF, 0xFF),
            # "LightGoldenRodYellow": (0xFA, 0xFA, 0xD2),
            # "LightGrey": (0xD3, 0xD3, 0xD3),
            # "LightPink": (0xFF, 0xB6, 0xC1),
            # "LightSalmon": (0xFF, 0xA0, 0x7A),
            # "LightSeaGreen": (0x20, 0xB2, 0xAA),
            # "LightSkyBlue": (0x87, 0xCE, 0xFA),
            # "LightSlateGray": (0x77, 0x88, 0x99),
            # "LightSlateGrey": (0x77, 0x88, 0x99),
            # "LightSteelBlue": (0xB0, 0xC4, 0xDE),
            # "LightYellow": (0xFF, 0xFF, 0xE0),
            # "Lime": (0x00, 0xFF, 0x00),
            # "LimeGreen": (0x32, 0xCD, 0x32),
            # "Linen": (0xFA, 0xF0, 0xE6),
            # "Magenta": (0xFF, 0x00, 0xFF),
            # "Maroon": (0x80, 0x00, 0x00),
            # "MediumAquaMarine": (0x66, 0xCD, 0xAA),
            # "MediumBlue": (0x00, 0x00, 0xCD),
            # "MediumOrchid": (0xBA, 0x55, 0xD3),
            # "MediumPurple": (0x93, 0x70, 0xDB),
            # "MediumSeaGreen": (0x3C, 0xB3, 0x71),
            # "MediumSlateBlue": (0x7B, 0x68, 0xEE),
            # "MediumSpringGreen": (0x00, 0xFA, 0x9A),
            # "MediumTurquoise": (0x48, 0xD1, 0xCC),
            # "MediumVioletRed": (0xC7, 0x15, 0x85),
            # "MidnightBlue": (0x19, 0x19, 0x70),
            # "MintCream": (0xF5, 0xFF, 0xFA),
            # "MistyRose": (0xFF, 0xE4, 0xE1),
            # "Moccasin": (0xFF, 0xE4, 0xB5),
            # "NavajoWhite": (0xFF, 0xDE, 0xAD),
            # "Navy": (0x00, 0x00, 0x80),
            # "OldLace": (0xFD, 0xF5, 0xE6),
            # "Olive": (0x80, 0x80, 0x00),
            # "OliveDrab": (0x6B, 0x8E, 0x23),
            # "OrangeRed": (0xFF, 0x45, 0x00),
            # "Orchid": (0xDA, 0x70, 0xD6),
            # "PaleGoldenRod": (0xEE, 0xE8, 0xAA),
            # "PaleGreen": (0x98, 0xFB, 0x98),
            # "PaleTurquoise": (0xAF, 0xEE, 0xEE),
            # "PaleVioletRed": (0xDB, 0x70, 0x93),
            # "PapayaWhip": (0xFF, 0xEF, 0xD5),
            # "PeachPuff": (0xFF, 0xDA, 0xB9),
            # "Peru": (0xCD, 0x85, 0x3F),
            # "Pink": (0xFF, 0xC0, 0xCB),
            # "Plum": (0xDD, 0xA0, 0xDD),
            # "PowderBlue": (0xB0, 0xE0, 0xE6),
            # "Purple": (0x80, 0x00, 0x80),
            # "RebeccaPurple": (0x66, 0x33, 0x99),
            # "RosyBrown": (0xBC, 0x8F, 0x8F),
            # "RoyalBlue": (0x41, 0x69, 0xE1),
            # "SaddleBrown": (0x8B, 0x45, 0x13),
            # "Salmon": (0xFA, 0x80, 0x72),
            # "SandyBrown": (0xF4, 0xA4, 0x60),
            # "SeaGreen": (0x2E, 0x8B, 0x57),
            # "SeaShell": (0xFF, 0xF5, 0xEE),
            # "Sienna": (0xA0, 0x52, 0x2D),
            # "Silver": (0xC0, 0xC0, 0xC0),
            # "SkyBlue": (0x87, 0xCE, 0xEB),
            # "SlateBlue": (0x6A, 0x5A, 0xCD),
            # "SlateGray": (0x70, 0x80, 0x90),
            # "SlateGrey": (0x70, 0x80, 0x90),
            # "Snow": (0xFF, 0xFA, 0xFA),
            # "SpringGreen": (0x00, 0xFF, 0x7F),
            # "SteelBlue": (0x46, 0x82, 0xB4),
            # "Tan": (0xD2, 0xB4, 0x8C),
            # "Teal": (0x00, 0x80, 0x80),
            # "Thistle": (0xD8, 0xBF, 0xD8),
            # "Tomato": (0xFF, 0x63, 0x47),
            # "Turquoise": (0x40, 0xE0, 0xD0),
            # "Violet": (0xEE, 0x82, 0xEE),
            # "Wheat": (0xF5, 0xDE, 0xB3),
            # "WhiteSmoke": (0xF5, 0xF5, 0xF5),
            # "YellowGreen": (0x9A, 0xCD, 0x32)
        })

        # allocate memory for the L*a*b* image, then initialize
        # the color names list
        self.lab = np.zeros((len(colors), 1, 3), dtype="uint8")
        self.colorNames = []

        # loop over the colors dictionary
        for (i, (name, rgb)) in enumerate(colors.items()):
            # update the L*a*b* array and the color names list
            self.lab[i] = rgb
            self.colorNames.append(name)

        # convert the L*a*b* array from the RGB color space
        # to L*a*b*
        self.lab = cv2.cvtColor(self.lab, cv2.COLOR_RGB2LAB)

    def label(self, image, c):
        try:
            # construct a mask for the contour, then compute the
            # average L*a*b* value for the masked region
            mask = np.zeros(image.shape[:2], dtype="uint8")
            cv2.drawContours(mask, [c], -1, 255, -1)
            mask = cv2.erode(mask, None, iterations=2)
            mean = cv2.mean(image, mask=mask)[:3]

            # initialize the minimum distance found thus far
            minDist = (np.inf, None)

            # loop over the known L*a*b* color values
            for (i, row) in enumerate(self.lab):
                # compute the distance between the current L*a*b*
                # color value and the mean of the image
                d = dist.euclidean(row[0], mean)

                # if the distance is smaller than the current distance,
                # then update the bookkeeping variable
                if d < minDist[0]:
                    minDist = (d, i)

            # return the name of the color with the smallest distance
            return self.colorNames[minDist[1]]
        except Exception:
            return "Unknown"
