from datetime import datetime


def format_timestamp(timestamp: int, fmt: str | None = None) -> str:
    date_object = datetime.fromtimestamp(timestamp)
    if fmt is None:
        fmt = "%Y-%m-%d %H:%M:%S"

    try:
        return date_object.strftime(fmt)
    except Exception:
        return ""