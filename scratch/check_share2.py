with open('assets/index-2d1L6cXj.js.bak', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'navigator\.share|shareData|share', content)]
for pos in matches[:6]:
    print(repr(content[pos-30:pos+120]))
