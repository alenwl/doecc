"""
Main file
"""

import argparse
import datetime
from doecc.src.analyzer import FileAnalyzer
from pathlib import Path
from typing import List


def parse_args():
    """Function to parse arguments."""
    parser = argparse.ArgumentParser(
        description="Run the doecc (Data Operations Engineer Code Challenge) package.",
        prog="doecc",
    )
    parser.add_argument(
        "--init_time", "-i", help="Initial time", type=str, required=True
    )
    parser.add_argument("--end_time", "-e", help="End time", type=str, required=True)
    parser.add_argument(
        "--logfile",
        "-lf",
        help="Log file name",
        nargs="+",
        required=True,
    )

    parser.add_argument(
        "--host",
        "-ho",
        help="End time",
        nargs="+",
        required=True,
    )

    args = parser.parse_args()

    return args, parser


def validate_time(epoch_time: str) -> bool:
    """Ensure timestamp is valid"""
    try:
        datetime.datetime.fromtimestamp(float(epoch_time) / 1000.0)
    except ValueError:
        print(f"Invalid timestamp {epoch_time} provided")
        return False
    return True


def validate_files(filename: List[str]) -> bool:
    """Ensure files exist"""
    file_list = filename[0].split(",")
    for file in file_list:
        if not Path(file).is_file():
            raise IOError(f"Invalid file provided: {file}")
    return True


def main():
    """
    Command line script for doecc package
    """

    args, parser = parse_args()

    if (
        validate_time(args.init_time)
        and validate_time(args.end_time)
        and validate_files(args.logfile)
    ):
        process = FileAnalyzer(
            filename=args.logfile[0].split(","),
            init_timestamp=args.init_time,
            end_timestamp=args.end_time,
            hosts=args.host[0].split(","),
        )
        process.start()
        process.print_report()


########################################################################################

if __name__ == "__main__":
    main()

########################################################################################
