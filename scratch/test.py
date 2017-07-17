from call_map import jedi_dump
import call_map.gui
import jedi
import toolz as tz

from call_map.jedi_ast_tools import *


def main():
    jedi_test_node = call_map.gui.make_jedi_test_nodes()
    #test_node = make_test_node()
    call_map.gui.main()


def calls(leaves):
    leaves = list(leaves)
    names = []
    operators = []

    for ii, elt in enumerate(leaves):
        if type(elt) is jedi.parser.tree.Name:
            names.append(elt)

        elif type(elt) is jedi.parser.tree.Operator:
            operators.append(elt)

    return names, operators


#jedi.helpers.evaluate_goto_definition( )

definitions = jedi.api.names(path=__file__)

nodes = jedi_dump.make_nodes(__file__)

d_main = tz.first(filter(lambda x: x.name == 'main', definitions))

def usages(definition):
    return jedi.api.usages.usages(
        definition._evaluator, {definition._name}, mods=frozenset())

main_usages = usages(d_main)

d_jedi_test_node = d_main.defined_names()[0]
#n2.defined_names()

names, operators = calls(leaves(d_jedi_test_node._definition))

print('---')
print(list(jedi_dump.definitions_of_called_objects(d_jedi_test_node)))
