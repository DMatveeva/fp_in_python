# 3.1

@curry(2)
def tag(t, v):
    return f"<{t}>{v}</{t}>"
bold = tag("b")
italic = tag("i")

# 3.2

@curry(3)
def tag(tg, attr, val):
    map_str = ''
    for k, v in attr.items():
        map_str += f' {k}="{v}"'
    return f"<{tg}{map_str}>{val}</{tg}>"


a = tag('li', {'class': 'list-group'}, 'item 23')
print(a)
