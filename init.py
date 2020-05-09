#!/usr/bin/env python

import time, sys, os


def main():
    try:
        from settings import settings
    except ImportError as exc:
        raise ImportError(
            "Couldn't import settings."
            "Did you forget to activate a virtual environment?"
        ) from exc
    settings.check_args(sys.argv)


if __name__ == "__main__":
    main()
