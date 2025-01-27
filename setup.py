from setuptools import setup
from Cython.Build import cythonize

setup(
    name = 'alpha',
    ext_modules = cythonize(
        [
            'stack.py',
            'main.py'
        ],
        compiler_directies={'language_leel': "3"}
        ),
    zip_safe = True,
)