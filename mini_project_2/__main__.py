#!/usr/bin/python
# -*- coding: utf-8 -*-

"""argparse and entry point script for mini-project-2"""

import argparse
import os
import sys
import logging
from logging import getLogger, basicConfig, Formatter
from logging.handlers import TimedRotatingFileHandler

from mini_project_2.db_queries import QueryEngine

__log__ = getLogger(__name__)

LOG_LEVEL_STRINGS = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]


def log_level(log_level_string: str):
    if log_level_string not in LOG_LEVEL_STRINGS:
        raise argparse.ArgumentTypeError(
            "invalid choice: {} (choose from {})".format(
                log_level_string,
                LOG_LEVEL_STRINGS
            )
        )
    return getattr(logging, log_level_string, logging.INFO)


def get_parser() -> argparse.ArgumentParser:
    """Create and return the argparser for mini-project-2"""
    parser = argparse.ArgumentParser(
        description="Start mini-project-2"
    )

    group = parser.add_argument_group(title="Logging")
    group.add_argument("--log-level", dest="log_level", default="INFO",
                       type=log_level, help="Set the logging output level")
    group.add_argument("--log-dir", dest="log_dir",
                       help="Enable TimeRotatingLogging at the directory "
                            "specified")
    group.add_argument("-v", "--verbose", action="store_true",
                       help="Enable verbose logging")

    group = parser.add_argument_group(title="Database")
    group.add_argument("-ad", "--ads-index", dest="ads_index",
                       required=True,
                       help="Path to the ``ad.idx`` file. "
                            "Noting a Berkely database hashed index "
                            "file for the data contained in ``ads.txt``")
    group.add_argument("-te", "--terms-index", dest="terms_index",
                       required=True,
                       help="Path to the ``te.idx`` file. "
                            "Noting a Berkely database B+-tree index "
                            "file for the data contained in "
                            "``terms.txt``")
    group.add_argument("-da", "--pdates-index", dest="pdates_index",
                       required=True,
                       help="Path to the ``da.idx`` file. "
                            "Noting a Berkely database B+-tree index "
                            "file for the data contained in "
                            "``pdates.txt``")
    group.add_argument("-pr", "--prices-index", dest="prices_index",
                       required=True,
                       help="Path to the ``pr.idx`` file. "
                            "Noting a Berkely database B+-tree index "
                            "file for the data contained in "
                            "``prices.txt``")

    group = parser.add_argument_group(title="Query")
    group.add_argument("-q", "--query",  required=True,
                       help="The Query string to process")
    group.add_argument("-o", "--output", choices=["full", "brief"],
                       help="Specify the output format")
    return parser


def main(argv=sys.argv[1:]) -> int:
    """main entry point mini-project-2"""
    parser = get_parser()
    args = parser.parse_args(argv)

    # configure logging
    handlers_ = []
    log_format = Formatter(fmt="[%(asctime)s] [%(levelname)s] - %(message)s")
    if args.log_dir:
        os.makedirs(args.log_dir, exist_ok=True)
        file_handler = TimedRotatingFileHandler(
            os.path.join(args.log_dir, "mini_project_2.log"),
            when="d", interval=1, backupCount=7, encoding="UTF-8",
        )
        file_handler.setFormatter(log_format)
        file_handler.setLevel(args.log_level)
        handlers_.append(file_handler)
    if args.verbose:
        stream_handler = logging.StreamHandler(stream=sys.stderr)
        stream_handler.setFormatter(log_format)
        stream_handler.setLevel(args.log_level)
        handlers_.append(stream_handler)

    basicConfig(
        handlers=handlers_,
        level=args.log_level
    )

    query_engine = QueryEngine(
        args.ads_index,
        args.terms_index,
        args.pdates_index,
        args.prices_index,
        args.output
    )
    query_engine.run_query(args.query)
    return 0


if __name__ == "__main__":
    sys.exit(main())
