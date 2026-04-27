# 2.3.1
@curry(2)
def concat(s1, s2):
    return s1 + s2
hello_concat = concat('Hello, ')

# 2.3.2
# Возможно, надо поменять местами аргументы "заключительный знак" и "имя"

@curry(4)
def first_step(greeting, punct_mark_1, punc_mark_2, name):
    return greeting + punct_mark_1 + ' ' + name + punc_mark_2
  
final = first_step("Hello")(",")("!")
f = final("Petya")
print(f)
