#!/usr/bin/env python3
class PasswordError(Exception):
    """Base class for exceptions in this module."""
    pass


class TrivialPasswordError(PasswordError):
    """Passwords that are too Trivial like: 'password'"""
    def __init__(self, msg):
        super().__init__("Trivial Password:" + msg)


class PasswordLengthError(PasswordError):
    """Passwords that do not meet certain length criteria"""
    def __init__(self, msg, length):
        super().__init__(msg)
        self.length = length

    def get_length(self):
        return self.length


class RepetetiveError(PasswordError):
    """Passwords that have repetitive characters"""
    def __init__(self, msg):
        super().__init__(msg)
