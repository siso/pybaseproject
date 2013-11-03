import os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'pybaseproject',
    'author': 'Foo Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['pybaseproject'],
    'scripts': [os.path.join('bin', 'pybaseproject')],
    'name': 'pybaseproject'
}

setup(**config)
