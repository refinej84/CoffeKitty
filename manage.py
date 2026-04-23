#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import subprocess
import sys
from pathlib import Path


def use_project_venv():
    """Re-run with the repo-local virtualenv so activation is optional."""
    project_dir = Path(__file__).resolve().parent
    venv_python = project_dir / 'venv' / 'Scripts' / 'python.exe'

    if not venv_python.exists():
        return

    current_python = Path(sys.executable).resolve()
    target_python = venv_python.resolve()
    if current_python == target_python:
        return

    if os.environ.get('COFFEEKITTY_VENV_REEXEC') == '1':
        return

    env = os.environ.copy()
    env['COFFEEKITTY_VENV_REEXEC'] = '1'
    env['VIRTUAL_ENV'] = str(project_dir / 'venv')
    env['PATH'] = f"{target_python.parent}{os.pathsep}{env.get('PATH', '')}"

    completed = subprocess.run(
        [str(target_python), __file__, *sys.argv[1:]],
        env=env,
        check=False,
    )
    raise SystemExit(completed.returncode)


def main():
    """Run administrative tasks."""
    use_project_venv()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffeekitty.settings')
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
