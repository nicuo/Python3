from study7_7 import mammoth
import re

pat = r'\b\w*[aeiou]{3}[^aeiou]\w*\b'
print(re.findall(pat,mammoth))

pat = r'\b\w*[aeiou]{3}[^aeiou\s]\w*\b'
print(re.findall(pat,mammoth))

pat = r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b'
print(re.findall(pat,mammoth))
