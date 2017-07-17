import jedi
import call_map.jedi_ast_tools as jat
import toolz as tz


test_script = """

import call_map.jedi_ast_tools as jat


def thunk():
    print('hi')


def ff(node):
    aa = get_called_functions(node)
    thunk()

"""



definitions = jedi.api.names(source=test_script)

print(definitions)