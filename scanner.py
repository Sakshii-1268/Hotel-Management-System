import pyqrcode
import png
from pyqrcode import QRCode

s = 'upi://pay?pa=8652172816@ybl&pn=Sakshi Yadav&mc=0000&mode=02&purpose=00'

url = pyqrcode.create(s)


url.png('myqr.png',scale=6)