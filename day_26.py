'''
meta characters:
1.[]-->A-z,a-z,[ahg]

import re
so="Python is a language"
any=re.findall("[ait]",so)
print(any)
#2.(.)
import re
so="Python is a language"
any=re.findall("P..h..",so)
print(any)
#(^)---checks the string is starting or not:
import re
so="Python is a language"
any=re.findall("^Python",so)
print(any)
#($)--
import re
so="Python is a language"
any=re.findall("language$",so)
print(any)
import re
so="Python is a language"
any=re.search("language$",so)
print(any)
#(*)--> zero to n number char
import re
so="Python is a language"
any=re.findall("P.*",so)
print(any)
#(+)--> 
import re
so="Python is a language"
any=re.findall("P.+ython",so)
print(any)
import re
so="Python is a language"
any=re.findall("P.+n",so)
print(any)
#{}
import re
so="Python is a language"
any=re.findall("P.{10}",so)
print(any)
'''
