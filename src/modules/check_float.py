def check_float(value: any) -> bool:
    try:
        float(value)
        return True
    except:
        return False
