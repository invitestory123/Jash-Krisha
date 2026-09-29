with open('assets/index-2d1L6cXj.js.bak', 'r', encoding='utf-8') as f:
    content = f.read()

pos_start = content.find('function b_({ready:e=!0})')
pos_end = content.find('function S_()')
print('b_ start:', pos_start, 'end:', pos_end)
exact_b = content[pos_start:pos_end]
print('exact_b length:', len(exact_b))
print('exact_b ends with:', repr(exact_b[-100:]))
