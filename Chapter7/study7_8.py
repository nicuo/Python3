from study7_7 import mammoth
import re

pat = r'\bc\w*'
print (re.findall(pat,mammoth))
