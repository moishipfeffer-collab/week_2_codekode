def c_to_f(celsius):
    return (celsius * 9/5) + 32 

HOT_TENP = 30
COLD_TEMP = 15

def describe(celsius):
    if celsius >= HOT_TENP:
        return "hot"
    elif celsius <= COLD_TEMP:
        return "cold"
    else:
        return "pleasent"
    