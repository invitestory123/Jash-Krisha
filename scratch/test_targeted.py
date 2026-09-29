with open('assets/index-2d1L6cXj.js.bak', 'r', encoding='utf-8') as f:
    content = f.read()

tests = [
    ('hero_line', 'children:`Join us for the engagement party of`'),
    ('hero_alt', 'alt:`Illustration of ${$.groom} and ${$.bride} holding photo frames`'),
    ('countdown_label', 'children:`Counting down to the evening`'),
    ('seal_top', 'children:`Save the date`'),
    ('old_venue', 'function D_(){return(0,O.jsxs)(`section`,{className:`px-6 pb-20 text-center sm:pb-28`'),
    ('old_I', 'function I_(){M_();let[e,t]=(0,b.useState)(!1);return(0,O.jsxs)(O.Fragment,{children:[(0,O.jsx)(__,{onOpen:()=>t(!0)})'),
]

for name, t in tests:
    print(name, 'FOUND:', t in content)
