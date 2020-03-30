def error_resp(reason):
    """Default responce json responce in case of error"""
    return {
        "error": reason
    }


def success_resp(seconds, planet):
    return {
        "from": "earth",
        "to": planet,
        "seconds": seconds
    }
