

def str_attr_format(x):
    return x.replace('-', '_').replace(' ', '_').lower()


def str_col_format(x):
    return x.replace('_', '-').replace(' ', '-').upper()
