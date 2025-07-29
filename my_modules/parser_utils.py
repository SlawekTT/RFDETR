import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='', allow_abbrev=False)
    parser.add_argument('-i', '--input', type=str, help='input device')
    return parser

def get_parser_args():
    parser = get_parser()
    args = parser.parse_args()
    return vars(args)
