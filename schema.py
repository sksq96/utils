def schema(d, idx=0):
    """
    Print Schema of a nested Dictionary.
    """
    for k, v in d.items():
        print("\t"*idx, k)
        if isinstance(v, dict):
            schema(v, idx+1)
