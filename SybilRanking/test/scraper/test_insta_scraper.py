import os
userlist = \
"""mikeitgeek
khatamy
narges.518
miladmoradi1372s
parvizparastouei
"""
with open("usernamelist.txt", 'w') as outfile:
    outfile.write( userlist )

os.system("python ../../scraper/InstagramScraper.py -u mehdi.est14 -p pu22ycat -i --filename usernamelist.txt")
