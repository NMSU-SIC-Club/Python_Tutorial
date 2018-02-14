import argparse
import logging
import sys


def main():
    parser = argparse.ArgumentParser()

    # logging configuration arguments
    parser.add_argument('-d', '--debug', action='store_true', default=False, help='start with debug')
    parser.add_argument('-v', '--verbose', action='count', default=None,
                        help='set verbosity (info, warning, error, critical)')

    args = parser.parse_args(sys.argv[1:])

    # set logging mode
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("Debug Mode Enabled")
    elif args.verbose is not None:
        verbosity = set_verbosity(args.verbose)
        print("log level set to %s" % verbosity)


def set_verbosity(level: int) -> str:
    levels = (logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)
    log_level = levels[min(level, len(levels)) - 1]  # subtract 1 because lists are 0-indexed
    logging.basicConfig(level=log_level)
    return logging.getLevelName(log_level)



if __name__ == "__main__":
    main()
