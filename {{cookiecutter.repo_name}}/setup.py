import io
import re
from setuptools import setup

init_py = io.open('{{cookiecutter.repo_name}}/__init__.py').read()
metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", init_py))
metadata['doc'] = re.findall('"""(.+)"""', init_py)[0]

setup(
    name='{{cookiecutter.repo_name}}',
    version=metadata['version'],
    description=metadata['doc'],
    author=metadata['author'],
    author_email=metadata['email'],
    url=metadata['url'],
    packages=['{{cookiecutter.repo_name}}'],
    include_package_data=True,
    install_requires=io.open('requirements/runtime.txt').readlines(),
    entry_points={
        'console_scripts': [
            '{{cookiecutter.repo_name}} = {{cookiecutter.repo_name}}.cli:main',
        ],
    },
    license=open('LICENSE').read(),
)
