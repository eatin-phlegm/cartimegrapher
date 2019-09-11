from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='cartimegrapher',
    version='0.0.1',
    url='https://github.com/eatin-phlegm/cartimegrapher',
    license='GPL-3.0',
    author='eatin-phlegm',
    author_email='',
    description='A simple timeline visualizer for writers.',
    long_description=long_description,
    install_requires=['pandas', 'cycler', 'kiwisolver', 'matplotlib',
                      'numpy', 'pyparsing', 'PyQt5', 'PyQt5-sip', 'python-dateutil',
                      'pytz', 'six', 'xlrd']
)
