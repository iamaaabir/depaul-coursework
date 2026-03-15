def unique_values(d):
    unique_vals = set()
    for val in d.values():
        try:
            unique_vals.add(val)
        except:
            pass # or continue
    return unique_vals
