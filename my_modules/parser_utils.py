import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='', allow_abbrev=False)
    parser.add_argument('-i', '--input', type=str, help='input device', default='0')
    parser.add_argument('-s', '--size', type=str, help='model size: nano/small/medium/large', default='nano')
    parser.add_argument('-t', '--threshold', type=float, help='detection threshold [0-1]', default=0.2)
    return parser

def get_parser_args():
    parser = get_parser()
    args = parser.parse_args()
    return vars(args)

def get_cli_params() -> list:
    args_dict: dict = get_parser_args() # get params into dictionary
    params_list: list = ['input', 'size', 'threshold']
    output_list: list = []
    for param in params_list:
        output_list.append(args_dict[param])
    return output_list

def device_to_int(DEVICE: str)-> int:
    # if device is shorter than 2 characters, try to convert it from str to int
    if len(DEVICE) < 2:
        try:
            DEVICE = int(DEVICE)
        except:
            pass
    return DEVICE


