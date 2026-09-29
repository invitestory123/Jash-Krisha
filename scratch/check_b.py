with open('assets/index-2d1L6cXj.js.bak', 'r', encoding='utf-8') as f:
    content = f.read()

pos = content.find('function b_({ready:e=!0})')
print('b_ pos:', pos)
print(content[pos:pos+1500])
