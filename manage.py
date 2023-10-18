#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RRRWebsite.settings')
    try:
        from django.core.management import execute_from_command_line
        result = execute_from_command_line(sys.argv)
    except SystemExit as exc:
        result = exc.code
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    if 'test' in sys.argv: # Only run if testing
        if result:
            print("\033[91mTests failed!\033[0m")  # Print in red
        else:
            print("\033[92mAll tests passed!\033[0m")  # Print in green
            
    sys.exit(result)


if __name__ == '__main__':
    main()
