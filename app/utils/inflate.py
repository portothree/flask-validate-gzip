import gzip
from flask import request

GZIP_CONTENT_ENCODING = "gzip"


def inflate(func):
    """
    A decorator to inflate content of a single view function
    """

    print("inflate")

    def wrapper(*args, **kwargs):
        _inflate_gzipped_content()
        return func(*args, **kwargs)

    return wrapper


def _inflate_gzipped_content():
    content_encoding = getattr(request, "content_encoding", None)

    if content_encoding != GZIP_CONTENT_ENCODING:
        return

    # We don't want to read the whole stream at this point.
    request.stream = gzip.GzipFile(fileobj=request.stream)
