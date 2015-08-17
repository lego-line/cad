from decimal import Decimal, InvalidOperation
import fileinput

for line in fileinput.input(inplace=True):
    line = line.split(' ')
    new_line = []
    
    for cell in line:
        try:
            new_cell = Decimal(cell)
        except InvalidOperation:
            new_cell = cell
        else:
            new_cell = str(new_cell.quantize(Decimal('5')))
        new_line.append(new_cell)
        
    print ' '.join(new_line),