import argparse
import logging
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', default=False, help='start with debug')
    parser.add_argument('-v', '--verbose', action='count', default=None,
                        help='set verbosity (info, warning, error, critical)')
    args = parser.parse_args(sys.argv[1:])

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("Debug Mode Enabled")
    elif args.verbose is not None:
        levels = (logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)
        log_level = levels[min(args.verbose - 1, len(levels) - 1)]
        logging.basicConfig(level=log_level)
        print("log level set to %s" % logging.getLevelName(log_level))

    logging.info("This message is informative")
    logging.debug("This message is for debugging")
    logging.warning("This is your first warning")
    logging.error("This is an error")
    logging.critical("This error is critical")


if __name__ == "__main__":
    main()