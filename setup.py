try:
    from setuptools import setup    
except ImportError:
    from distutils.core import setup

config = [
    'description': 'Networking tools with python script',
    'author': 'Mujibur Rochman',
    'url': 'https://github.com/mujib-programmer/PyNetTools-Python',
    'download_url': 'https://mujibprogrammer.wordpress.com/',
    'author_email': 'mujib.programmer@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['PyNetTools'],
    'scripts': [],
    'name': 'PyNetTools'
]

setup(**config)
