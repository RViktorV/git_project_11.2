def str_func(value):
    """
    :param value: введенная строка
    :return: строка с буквами в верхнем регистре
    """
    return value.upper()


def title_word(value):
    """
    :param value: введенная строка
    :return: строка в которое каждое слово прописывается с заглавной буквы
    """
    return ' '.join(word.capitalize() for word in value.split())

