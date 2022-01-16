import textwrap
import typing
import argparse
import sys


class Native(argparse.ArgumentParser):
    def error(self, message: str) -> typing.NoReturn:
        self.print_help()
        sys.exit(2)


def main():
    parser = Native(
        prog="freightmatric.com",
        usage=argparse.SUPPRESS,
        formatter_class=argparse.RawTextHelpFormatter,
        description=textwrap.dedent("""
        CLI Tool For FreightMatric
            search                      Search Anything
            docket_number               Search MC Number
            dot_number                  Search Docket Number
        """),
        add_help=False,
        allow_abbrev=True,
    )
    parser.add_argument("search", help=argparse.SUPPRESS)
    parser.add_argument("dotNumber", help=argparse.SUPPRESS)
    parser.add_argument("docketNumber", help=argparse.SUPPRESS)

    args = parser.parse_args()

    match args:
        case args.search:
            print("search it is")




