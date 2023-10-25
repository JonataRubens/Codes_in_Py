from barcode import EAN13
from barcode.writer import ImageWriter # para salvar em png

num = '112565666666666'

cb = EAN13(num,writer=ImageWriter()) #writer para salvar as imagens
cb.save("codigo_barras")