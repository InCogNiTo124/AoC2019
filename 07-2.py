i = 0
#INPUT = '''3,8,1001,8,10,8,105,1,0,0,21,46,59,80,105,122,203,284,365,446,99999,3,9,102,3,9,9,1001,9,5,9,102,2,9,9,1001,9,3,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,101,5,9,9,1002,9,3,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,4,9,1001,9,2,9,102,4,9,9,101,3,9,9,102,2,9,9,4,9,99,3,9,102,5,9,9,101,4,9,9,102,3,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99'''
INPUT='''3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'''
#INPUT='''3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'''
MEMORY_start = [t for t in map(int, INPUT.split(','))]

def prepare(param_count, stores=False):
    def decorator(f):
        def wrapper(*args, **kwargs):
            params = list(args[:param_count])
            param_modes = list(args[param_count+int(stores):])
            while len(param_modes) < len(params):
                param_modes.append(False)
            for i in range(param_count):
                if not param_modes[i]:
                    params[i] = MEMORY[params[i]]
            args = tuple(params + ([args[param_count]] if stores else []))
            return f(*args)
        return wrapper
    return decorator

@prepare(2, stores=True)
def add(a, b, c):
    MEMORY[c] = a + b
    return True

@prepare(2, stores=True)
def mul(a, b, c):
    MEMORY[c] = a*b
    return True

@prepare(0, stores=True)
def read(c):
    MEMORY[c] = int(input())
    return True

@prepare(1)
def out(x):
    print(x)
    return True

@prepare(2)
def jit(a, b):
    global i
    if a != 0:
        i = b
        return False
    return True

@prepare(2)
def jif(a, b):
    global i
    if a == 0:
        i = b
        return False
    return True

@prepare(2, stores=True)
def lt(a, b, c):
    MEMORY[c] = 1 if a < b else 0
    return True

@prepare(2, stores=True)
def eq(a, b, c):
    MEMORY[c] = 1 if a == b else 0
    return True
    
instructions = {
    0: {"f": lambda x: x, "argc": 0},
    1: {"f": add, "argc": 3},
    2: {"f": mul, "argc": 3},
    3: {"f": read, "argc": 1},
    4: {"f": out, "argc": 1},
    5: {"f": jit, "argc": 2},
    6: {"f": jif, "argc": 2},
    7: {"f": lt, "argc": 3},
    8: {"f": eq, "argc": 3},
}

def read_opcode():
    global i
    opcode = MEMORY[i]
    instr = int(str(opcode)[-2:])
    params = tuple(reversed([t for t in map(bool, map(int, str(opcode)[:-2]))]))
    i += 1
    return instr, params

def handle_params(opcode):
    t = tuple(MEMORY[i:i+instructions[opcode]["argc"]])
    return t

#import sys
#print(sys.argv[1])
MEMORY = MEMORY_start.copy()
while MEMORY[i] != 99:
    opcode, param_args = read_opcode()
    args = handle_params(opcode)
    if instructions[opcode]["f"](*args, *param_args):
        i += instructions[opcode]["argc"]
