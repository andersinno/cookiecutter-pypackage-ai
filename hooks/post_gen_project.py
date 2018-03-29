import io
import os
import shutil

is_it_django_package = '{{ cookiecutter.is_it_django_package }}'
python_pkg_dir = '{{ cookiecutter.project_slug }}'

if is_it_django_package != 'yes':
    assert is_it_django_package == 'no'

    # Remove the tests dir as its Django specific
    tests_dir = os.path.join(python_pkg_dir, 'tests')
    shutil.rmtree(tests_dir)


# Fix title line length in README.rst
with io.open('README.rst', 'rt', encoding='utf-8') as fp:
    lines = iter(fp)
    first_line = next(lines)
    second_line = next(lines)
    assert set(second_line.strip()) == set(['='])
    underlining = (len(first_line.rstrip()) * '=') + '\n'
    new_lines = [first_line, underlining] + list(lines)
with io.open('README.rst', 'wt', encoding='utf-8') as fp:
    fp.write(''.join(new_lines))
