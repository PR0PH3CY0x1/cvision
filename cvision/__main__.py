from cvision.argparser.parser import parser

from cvision.utils.capture import capture
from cvision.utils.output import read_capture
from cvision.utils.classifier import classifier


def main():
    args = parser()

    _capture = capture(
        args.input
    )

    _classifier = classifier(
        args.cascade
    )

    read_capture(
        _capture,
        _classifier
    )


if __name__ == '__main__':
    main()
