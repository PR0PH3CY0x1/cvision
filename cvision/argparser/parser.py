from argparse import ArgumentParser


def parser():
    parser = ArgumentParser(
        prog='careye'
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
