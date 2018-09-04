OPERATORS = {
    'and': ('binary', 'and'),
    'or': ('binary', 'or'),
    '!': ('unary', 'not'),
    '==': ('binary', '=='),
    '!=': ('binary', '!='),
    '===': ('binary', '=='),
    '!==': ('binary', '!='),
    'var': ('data', None),
}


def _get_operator(logic):
    """Return operator name from JsonLogic rule."""
    op = next(iter(logic))
    if op not in OPERATORS:
        raise Exception('Unknown Operator')
    return op


def transpile(logic):
    if isinstance(logic, str):
        return f'"{logic}"'

    if isinstance(logic, (int, float)):
        return f'{logic}'

    json_operator = _get_operator(logic)
    values = logic[json_operator]
    operator_type, operator = OPERATORS[json_operator]

    if isinstance(values, list):
        values = map(transpile, values)

    if operator_type is 'data':
        # TODO: assuming only one level of variable nesting
        obj, prop = values.split('.')
        return f'( {obj}.get("{prop}", "") )'

    if operator_type is 'binary':
        return '( ' + f' {operator} '.join(values) + ' )'

    if operator_type is 'unary':
        return f'( {operator} {next(values)} )'

    raise Exception("Unable to transpile logic")


def execute(logic, _id):
    transpiled_logic = transpile(logic)
    name = f'rules_{_id}'
    code = f'def {name}(rec, seed): return ({transpiled_logic})'
    scope = {}
    exec(code, {}, scope)
    return scope[name]
