with open('assets/index-2d1L6cXj.js.bak', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'whatsapp|\.ics|calendar', content, re.IGNORECASE)]
print('calendar/share matches:', matches)
for pos in matches[:5]:
    print(repr(content[pos-50:pos+150]))
