@curry(2)
def to_left(bird_num, x): 
    return Just([x[0] + bird_num, x[1]]) if abs(x[0] + bird_num - x[1]) <= 4 else Nothing
  
@curry(2)
def to_right(bird_num, x):
    return Just([x[0], x[1] + bird_num]) if abs(x[1] + bird_num - x[0]) <= 4 else Nothing
  
banana = lambda x: Nothing
begin = Just([0, 0])

def show(maybe):
    return maybe == Nothing
  
is_fall_1 = show( begin.bind(to_left(2)).bind(to_right(5)).bind(to_left(-2)) )
is_fall_2 = show( begin.bind(to_left(2)).bind(to_right(5)).bind(to_left(-1)) )
is_fall_3 = show( begin.bind(to_left(2)).bind(banana).bind(to_right(5)).bind(to_left(-1)) )
