"""يحدّث رقم النسخة داخل index.html قبل أي نشر.

الصفحة تقارن رقمها مع اللي على السيرفر، فلو ما تغيّر الرقم يظل
اللاعبين يشوفون النسخة القديمة من كاش المتصفح. شغّله قبل كل push:

    python bump.py
"""
import re, io, datetime, sys

P = "index.html"
s = io.open(P, encoding="utf-8").read()
v = datetime.datetime.now().strftime("%Y%m%d-%H%M")
s2, n = re.subn(r'const BUILD="[^"]*";', 'const BUILD="%s";' % v, s, count=1)
if not n:
    sys.exit("ما لقيت const BUILD في index.html")
io.open(P, "w", encoding="utf-8").write(s2)
print("BUILD =", v)
