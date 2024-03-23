def str_func(value):
    """
    :return: строка с буквами в верхнем регистре
    """
    return value.upper()


def title_word(value):
    """
    :return: строка в которое каждое слово прописывается с заглавной буквы
    """
    return ' '.join(word.capitalize() for word in value.split())

