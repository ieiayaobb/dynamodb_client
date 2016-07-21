# -*- coding: utf-8 -*-

"""
Exception happened in parse phrase
"""
import logging


class ParseException(Exception):
    def __init__(self, message):
        logging.error("Parse Error : %s" % message)
