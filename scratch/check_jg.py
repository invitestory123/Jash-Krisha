with open('assets/index-2d1L6cXj.js.bak', 'r', encoding='utf-8') as f:
    content = f.read()

pos = content.find('function Jg')
print('pos of Jg:', pos)
if pos != -1:
    print(content[pos:pos+900])
