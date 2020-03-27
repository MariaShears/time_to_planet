def error_resp(reason):
    return {
        "error": reason
    }


def success_resp(seconds, planet):
    return {
        "from": "earth",
        "to": planet,
        "seconds": seconds
    }
