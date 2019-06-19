import sys
from setuptools import setup, find_packages
from distutils.version import LooseVersion

if sys.hexversion < 0x30500f0:
    print('Stex API client requires at least Python 3.5')
    sys.exit(1)

setup(
    name='stex_client',
    description='Stex API V3 client for python.',
    long_description='Stex provides all the core exchange functionality, and additional merchant tools available via the HTTP API where all returned messages are in JSON. Its much easier to work with the API by using one of the clients provided by Stex.com, so while this page describes the API in case you want or need to build your own client, the examples use the Python client.',
    url='https://github.com/StocksExchange/python_client',
    version=str(LooseVersion('1.0.0')),
    packages=find_packages('stex_client'),
    zip_safe=False,
    package_dir={'': 'stex_client'},
    python_requires='>=3.5',
    author='STEX (Stocks.Exchange)',
    license='MIT',
    copyright='Copyright (C) 2019 Stex.com',
    author_email='analytics@stex.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='api client request stocks.exchange stex library websocket-client stex.com',
    install_requires=['requests', 'furl', 'pendulum', 'python-socketio'],
)
