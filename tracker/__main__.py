"""

Usage:
------

    $ jobtracker [options] -opts opts


See jobs still searching for:

    $ jobtracker showvalid


Available options are:
    # To be updated


Contact:
--------

kyle@cooperkyle.com
https://github.com/kc8/jobtracker



Version:
--------

- job-tracker: v0.1
"""

# imports
from .click_cli import main as tracker


def main():  # type: () -> None
    """Call jobtracker"""
    tracker.click_cli.main()



if __name__ == "__main__":
    main()