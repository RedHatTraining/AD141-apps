#!/usr/bin/env python3
import password_errors


def check_trivial(password):
    bad = ["password", "p@ssword", "passw0rd", "p@ssw0rd"]
    if password.lower() in bad:
        raise password_errors.TrivialPasswordError(password)


def check_length(password):
    min_length = 10
    length = len(password)
    if length < min_length:
        raise password_errors.PasswordLengthError("Too short", length)


def check_duplicates(password):
    removedupes = set(password)
    if len(removedupes) < len(password):
        raise password_errors.RepetetiveError("Repetetive Characters Exist")
