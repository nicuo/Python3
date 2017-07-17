from study7_7 import mammoth
import re

pat = r'\b\w*r\b'
print(re.findall(pat,mammoth))

pat = r'\b[\w\']*l\b'
print(re.findall(pat,mammoth))
