def is_value(symbol):
    tempSymbol = int(symbol)
    if 0 <= symbol <= 15:
        return True
    else:
        return False

'''def is_label(symbol):
    if "(" and ")" in symbol:
        return True
    else:
        return False'''

def is_comment(symbol):
    if "//" in symbol:
        return True
    else:
        return False

def is_source(symbol):
    if "," in symbol:
        return True
    else:
        return False

def is_destination(symbol):
    if symbol == "R0" or "R1" or "R2" or "R3":
        return True
    else:
        return False

def is_target(symbol):
    if "$" in symbol:
        tempTarget = symbol.replace("$","")
        tempTarget2 = int(tempTarget)
        if 0 <= tempTarget2 <= 4:
            return True
    else:
        return False