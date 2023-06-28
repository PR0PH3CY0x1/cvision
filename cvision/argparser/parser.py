from argparse import ArgumentParser


def parser():
    parser = ArgumentParser(
        prog='cvision'
    )

    parser.add_argument(
        '-i',
        '--input'
    )

    parser.add_argument(
        '-c',
        '--cascade'
    )

    return parser.parse_args()
