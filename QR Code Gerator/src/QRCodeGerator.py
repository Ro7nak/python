import pyqrcode

s = "https://www.hackerrank.com/rounak077?hr_r=1"
url = pyqrcode.create(s)
url.svg("my_Hackerrank_profile.svg", scale=8)
