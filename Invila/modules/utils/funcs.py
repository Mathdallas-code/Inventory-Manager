def check_float(value: any) -> bool:
    try:
        float(value)
        return True
    except:
        return False


def check_int(value: any) -> bool:
    try:
        int(value)
        return int(value)
    except:
        return False
