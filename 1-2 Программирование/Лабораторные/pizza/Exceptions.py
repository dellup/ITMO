class Error(Exception):
    pass

#исключение некорректного ввода
class IncorrectInputExcError(Error):
    '''Некорректный ввод'''
    pass
class OperationalError(Error):
    """Ошибка при работе с базой данных"""
    pass
class ValueError(Error):
    """Ошибка ввода"""
    pass