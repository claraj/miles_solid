class MileageError(Exception):
    # For errors that the client may be able to do something about.
    pass


# Other errors, that represent some kind of programming issue, will be allowed to be
# raised, so hopefully the developer can fix the issue. 