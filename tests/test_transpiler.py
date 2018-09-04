from jsonlogic_transpiler.transpiler import execute


def test_execute():
    logic = ''
    execute(logic, 'test_id')
