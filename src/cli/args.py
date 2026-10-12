import argparse
def get_parser():
    p = argparse.ArgumentParser(prog='link-auditor')
    p.add_argument('path', default='.', nargs='?')
    p.add_argument('--check-external', action='store_true')
    return p
