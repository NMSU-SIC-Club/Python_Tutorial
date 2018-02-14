def au_to_mkm(au: float) -> float:
    """
    1 AU = 149,597,870.7 KM
    :param au: dist in AU
    :return: dist in millions of KM
    """
    return au * 141.6
