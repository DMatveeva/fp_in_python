# Для любых входящих строк провести проверку, что строка в нижнем регистре. 
# Вывести список строк, которые прошли проверку. А для тех, которые не прошли, вывести обобщенное сообщение об ошибке. 

from pymonad.tools import curry
from pymonad.state import State

str_init = {'correct_strings': [], 'error_message': 'Not in lower case:'}
validation_state = State.insert(str_init['correct_strings'])

@curry(2)
def validate(value, correct_values):
    def count_computation(error_message):
        if value.islower():
            return correct_values + [value], error_message
        else:
            return correct_values, error_message + ' ' + value
    return State(count_computation)
  
finale = validation_state.then(validate('absc')).then(validate('Avd')).then(validate('A12345'))

correct_str, error_msg = finale.run(str_init['error_message']) 

# ['absc']
# Not in lower case: Avd A12345
