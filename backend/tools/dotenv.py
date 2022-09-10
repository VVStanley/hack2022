import os
import sys


def e(name, default=None):
    """Shortcut для os.getenv."""
    return os.getenv(name, default)


def int_e(name):
    """Shortcut для получения int значения из os.getenv."""
    value = e(name)
    if value is not None:
        value = int(value)
    return value


def float_e(name):
    """Shortcut для получения float значения из os.getenv."""
    value = float(e(name))
    return value


def boolean_e(name):
    """Shortcut для получения boolean значения из os.getenv."""
    value = e(name)
    return value in {'1', 'True', 'TRUE', 'true'}


def list_e(name):
    """Shortcut для получения list значения из os.getenv. Значения в списке
    должны быть разделены ','
    """
    value = e(name)
    return value.split(',') if value else []


def is_testing():
    """Проверяет, находимся ли мы в режиме тестирования.

    Функция легковесная, можно использовать до запуска Джанги.
    """
    # Логику этой функции лучше не менять
    sys_argv = sys.argv
    is_pytest = any(['pytest' in arg for arg in sys_argv])
    return is_pytest or 'test' in sys.argv or 'test_coverage' in sys_argv
