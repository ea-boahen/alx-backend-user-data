#!/usr/bin/env python3
""" this class manages API authentication
"""
from flask import request
from typing import List, TypeVar

class Auth:
    """Authentication template"""

    def __init__(self):
        """
            Constructor

            Args:
                path: path to authenticate
                excluded_paths: list of excluded path to authenticate
        """

    def require_auth(self, path: str, exclude_paths: List[str]) -> bool:
        #This method will be implemented later, for now its returning False
        return False

    def authorization_header(self, request=None) -> str:
        #This method will be implemented later, for now its returning None
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        #This method will be implemented later, for now its returning None
        return None

