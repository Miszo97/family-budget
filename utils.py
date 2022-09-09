def get_core_url(url: str) -> str:
    question_mark = url.find("?")
    if question_mark > 0:
        return url[:question_mark]
    return url
