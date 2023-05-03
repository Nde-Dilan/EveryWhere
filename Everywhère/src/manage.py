#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EveryWhere.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Changement du port de 8000 à 7000
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','EveryWhere.settings')
    port=7000
    execute_from_command_line(['manage.py','runserver',str(port)])
    # FIN

if __name__ == '__main__':
    main()
