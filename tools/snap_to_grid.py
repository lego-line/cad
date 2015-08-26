"""
This file takes an ldraw file as an input via drag and drop / command line, and modifies it in place.

It works around a LeoCAD 0.82.1 bug, causing positions and rotation to accumulate random errors.
This script removes those errors, by rounding these values

This SHOULD NOT be run on any file containing:
* generated belts
* non-orthogonal pieces
* bricks / baseplates

"""


from decimal import Decimal, InvalidOperation
import fileinput

for line in fileinput.input(inplace=True):
    line = line.split(' ')
    new_line = []
    
    for i, cell in enumerate(line):
        if i in range(2, 5):
            step = Decimal('5')
        elif i in range(5, 14):
            step = Decimal('0.001')
        else:
            step = None

        new_cell = cell

        if step:
            try:
                new_cell = Decimal(cell)
            except InvalidOperation:
                pass
            else:
                new_cell = (new_cell / step).quantize(1) * step
                new_cell = str(new_cell)

        new_line.append(new_cell)
        
    print ' '.join(new_line),