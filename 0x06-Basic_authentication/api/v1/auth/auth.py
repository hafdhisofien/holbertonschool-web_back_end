#!/usr/bin/env python3
"""
Class Auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Api Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require authentication
        """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        else:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user
        """
        return None
