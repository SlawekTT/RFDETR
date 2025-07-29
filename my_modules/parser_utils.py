import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='', allow_abbrev=False)
    parser.add_argument('-i', '--input', type=str, help='input device')
    parser.add_argument('-s', '--size', type=str, help='model size: nano/small/medium/large')
    parser.add_argument('-t', '--threshold', type=float, help='detection threshold [0-1]')
    return parser

def get_parser_args():
    parser = get_parser()
    args = parser.parse_args()
    return vars(args)
