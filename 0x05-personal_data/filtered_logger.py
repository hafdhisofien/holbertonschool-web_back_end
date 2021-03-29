#!/usr/bin/env python3
"""
0. Regex-ing
"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        init method
        """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        format method
        """
        return filter_datum(self.fields,
                            self.REDACTION,
                            super().format(record),
                            self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    Args:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        separator: a string representing by which
        character is separating all fields in the log line
    Returns:
        message: a string representing the log line
    """
    for field in fields:
        message = re.sub('{}=.*?{}'.format(field, separator),
                         '{}={}{}'.format(field, redaction, separator),
                         message)
    return message
