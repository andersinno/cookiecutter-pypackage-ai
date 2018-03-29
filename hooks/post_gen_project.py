import os
import shutil

is_it_django_package = '{{ cookiecutter.is_it_django_package }}'
python_pkg_dir = '{{ cookiecutter.project_slug }}'

if is_it_django_package != 'yes':
    assert is_it_django_package == 'no'

    # Remove the tests dir as its Django specific
    tests_dir = os.path.join(python_pkg_dir, 'tests')
    shutil.rmtree(tests_dir)
