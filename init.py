#!/usr/bin/env python

import time, sys, os
import notify2

# notify2.init("Test Notifier")
# n = notify2.Notification(None, icon = "")
# n.set_urgency(notify2.URGENCY_NORMAL)
# n.set_timeout(10000)
# n.update("New test title", "Hello Hasan, it is 1:16 am")
# n.show()


def main():
    try:
        from notifier import settings
    except ImportError as exc:
        raise ImportError(
            "Couldn't import settings."
            "Did you forget to activate a virtual environment?"
        ) from exc
    settings.check_args(sys.argv)


if __name__ == "__main__":
    main()
