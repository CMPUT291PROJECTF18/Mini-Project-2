#!/usr/bin/python
# -*- coding: utf-8 -*-

""""""

from bs4 import BeautifulSoup


# xml = input("Give me xml:")
test = """
<?xml version="1.0" encoding="UTF-8"?>
<ads type="array">
<ad><aid>1304786670</aid><date>2018/11/07</date><loc>Calgary</loc><cat>camera-camcorder-lens</cat><ti>Nikon 500 mm F4 VR</ti><desc>I have owned this Nikon lens for about 2 years and purchased it new in Calgary. The lens is extremely sharp, and fast focusing. It is a wildlife or bird photographers dream lens. I am selling it</desc><price>8500</price></ad>
<ad><aid>1385570526</aid><date>2018/11/05</date><loc>Edmonton</loc><cat>camera-camcorder-lens</cat><ti>NIKON D3s amateur useage body for sale</ti><desc>This camera has been my main travel camera and has generated wonderful prints some of which are hanging on our walls in paper, canvas and aluminum. The resolution and the HDR capability of shooting</desc><price>0</price></ad>
<ad><aid>1275366783</aid><date>2018/11/07</date><loc>Calgary</loc><cat>camera-camcorder-lens</cat><ti>Canon 30D DSLR BODY Like New</ti><desc>Canon 30D DSLR BODY Perfect Woirking Condition like New</desc><price>240</price></ad>
<ad><aid>1370676359</aid><date>2018/11/07</date><loc>Edmonton</loc><cat>camera-camcorder-lens</cat><ti>Canon Macro Lens</ti><desc>Take your photography to the next level with the Canon 100mm Macro Lens, EF100 1-2.8 USM. This lens is in excellent, hardly used condition and takes amazing macro photos. It has been described as one</desc><price>525</price></ad>
<ad><aid>1269098382</aid><date>2018/11/07</date><loc>Red-Deer</loc><cat>camera-camcorder-lens</cat><ti>Olympus digital camera 7.1 mp 10x zoom 2.5 screen</ti><desc>Olympus digital 7.1 mp 10 optical zoom 2.5 screen. Charging cord. No card or batteries. Email if interested</desc><price>80</price></ad>
<ad><aid>1396178670</aid><date>2018/11/07</date><loc>Calgary</loc><cat>camera-camcorder-lens</cat><ti>Fuji X-H1 24MP Mirrorless Camera Like New</ti><desc>Fuji X-H1 24MP Mirrorless Camera Like New - purchased a few months ago from Henrys - Comes with box, manual and charger</desc><price>1600</price></ad>
<ad><aid>1001612872</aid><date>2018/11/04</date><loc>Edmonton</loc><cat>bed-mattress</cat><ti>[SALE] BRAND NEW MATTRESSES [SALE]</ti><desc>JAG MATTRESS WHOLESALE !! - This Weeks Deal - compare @ $1299 Queen 13&#034; Luxury Plush Eurotop Mattress - $460 - BRAND NEW - Two Sided Mattress Twin / Single Mattress.....$130 Double/Full</desc><price>130</price></ad>
<ad><aid>1002787981</aid><date>2018/11/07</date><loc>Red-Deer</loc><cat>art-collectibles</cat><ti>Ken Linseman Game Used Stick</ti><desc>Asking $75.00 for a Ken Linseman Game Used Stick. Please call Doug at 403-346-6339 or e-mail to arrange shipping or pick-up. I can ship anywhere and can accept Paypal and Interac via e-mail</desc><price>75</price></ad>
<ad><aid>1003735318</aid><date>2018/11/07</date><loc>Edmonton</loc><cat>art-collectibles</cat><ti>Antique Hummel figurine</ti><desc>-&#034;soloist&#034; #135 -perfect condition -1960-1972 mark -call lloyd 780-217-9527</desc><price>50</price></ad>
<ad><aid>1003735660</aid><date>2018/11/07</date><loc>Edmonton</loc><cat>art-collectibles</cat><ti>Antique Hummel figurine</ti><desc>-&#034;school girl&#034; #81/2/0 -perfect condition -1960-1972 mark -call lloyd 780-217-9527</desc><price>50</price></ad>
</ads>

"""
soup = BeautifulSoup(test, "lxml")


ads = soup.find_all("ad")
print(ads)
for ad in ads:
    title = ad.find("ti").getText()
    description = ad.find("desc").getText()
    aid = ad.find("aid").getText()
    print(title, description)
    terms = set(title.lower().split()+description.lower().split())
    filter()

    print(terms)
# print(titles)
# print(descriptions)