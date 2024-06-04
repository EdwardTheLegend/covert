class Literal:
    def __init__(self, value):
        self.type = "Literal"
        self.value = value


class Array:
    def __init__(self, value):
        self.type = "Array"
        self.value = value


class Var:
    def __init__(self, name, value):
        self.type = "Var"
        self.name = name
        self.value = value


class Set:
    def __init__(self, caller, property, value):
        self.type = "Set"
        self.caller = caller
        self.property = property
        self.value = value


class Binary:
    def __init__(self, left, operator, right):
        self.type = "Binary"
        self.left = left
        self.operator = operator
        self.right = right


class Func:
    def __init__(self, name, params, body):
        self.type = "Func"
        self.name = name
        self.params = params
        self.body = body


class Return:
    def __init__(self, value):
        self.type = "Return"
        self.value = value


class For:
    def __init__(self, id, range, body):
        self.type = "For"
        self.id = id
        self.range = range
        self.body = body


class While:
    def __init__(self, condition, body):
        self.type = "While"
        self.condition = condition
        self.body = body


class Conditional:
    def __init__(self, condition, body, otherwise):
        self.type = "Conditional"
        self.condition = condition
        self.body = body
        self.otherwise = otherwise


class Struct:
    def __init__(self, name, members):
        self.type = "Struct"
        self.name = name
        self.members = members


class Instance:
    def __init__(self, name, members):
        self.type = "Instance"
        self.name = name
        self.members = members


class Call:
    def __init__(self, caller, args):
        self.type = "Call"
        self.caller = caller
        self.args = args


class Get:
    def __init__(self, caller, property, isExpr=False):
        self.type = "Get"
        self.caller = caller
        self.property = property
        self.isExpr = isExpr


class Unary:
    def __init__(self, operator, apply):
        self.type = "Unary"
        self.operator = operator
        self.apply = apply
