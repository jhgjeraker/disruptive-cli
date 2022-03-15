import sys


def stderr(*args, **kwargs):
    print(*args, file=sys.stderr, flush=True, **kwargs)


def stdout(*args, **kwargs):
    print(*args, file=sys.stdout, flush=True, **kwargs)
