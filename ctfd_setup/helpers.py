"""Command line helper functions."""

from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace:
    """Parse the program's arguments.

    Returns
    -------
    argparse.Namespace
        The program's arguments.

    """
    parser: ArgumentParser = ArgumentParser(
        prog="ctfd_setup",
        description="Automatically setup CTFd instance.",
    )

    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Run headful browser with a slowmo",
    )

    parser.add_argument(
        "--url",
        default="http://localhost:8000",
        type=str,
        help="URL of the CTFd (default: http://localhost:8000)",
    )

    parser.add_argument(
        "-t",
        "--timeout",
        default=30000,
        type=float,
        help="default maximum navigation time in milliseconds (default: 30000)",
    )

    args: Namespace = parser.parse_args()

    if not (args.url.startswith("http://") or args.url.startswith("https://")):
        args.url = f"http://{args.url}"

    return args
