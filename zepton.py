#!/usr/bin/env python3
"""
Project Zepton — entry point.
A modular, msfconsole-style security toolkit for Termux.
"""
import os
import sys

# Make the repo root importable regardless of the current working directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.colors import error  # noqa: E402


def main():
    if sys.version_info < (3, 8):
        error("Zepton requires Python 3.8+.")
        sys.exit(1)

    from core.console import ZeptonConsole
    ZeptonConsole().cmdloop()


if __name__ == "__main__":
    main()
