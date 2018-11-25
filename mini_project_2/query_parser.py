#!/usr/bin/python
# -*- coding: utf-8 -*-

""""""
import argparse


class ShellArgumentParser(argparse.ArgumentParser):
    """Custom argument parser"""

    def __init__(self, *args, **kwargs):
        # set ``add_help`` to false to avoid conflicts with the shell
        super().__init__(*args, **kwargs)


