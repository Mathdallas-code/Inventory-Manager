def check_int(value: any) -> bool:
    try:
        int(value)
        return int(value)
    except:
        return False
