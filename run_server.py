# run_server.py
from django.core.management import execute_from_command_line

import os
import sys

def run_server():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')
    execute_from_command_line(['manage.py', 'runserver'])

if __name__ == '__main__':
    run_server()
