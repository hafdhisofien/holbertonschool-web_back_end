#!/usr/bin/env python3
"""
0. Regex-ing
"""
import re
from typing import List


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
        m_format = field + "=.+?(?=abc)*\\" + ";"
        message = re.sub(m_format, field + "=" + redaction + separator, message)
    return message
