#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

required_version = (3, 1)  # Cambia a la versión que tu proyecto necesita
if sys.version_info[:2] < required_version:
    raise RuntimeError(
        f"Este proyecto requiere Python {required_version[0]}.{required_version[1]}"
        f"Estás usando Python {sys.version_info[0]}.{sys.version_info[1]}"
    )


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_server.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
