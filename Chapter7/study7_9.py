from study7_7 import mammoth
import re

pat = r'\bc\w{3}\b'
print(re.findall(pat,mammoth))
