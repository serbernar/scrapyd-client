from __future__ import absolute_import

from os.path import join, dirname

from setuptools import setup, find_packages

with open(join(dirname(__file__), 'scrapyd_client/VERSION')) as f:
    version = f.read().strip()

setup(
    name='scrapyd-client',
    version=version,
    url='https://github.com/serbernar/scrapyd-client',
    description='A client for scrapyd',
    long_description=open('README.rst').read(),
    author='Scrapy developers',
    maintainer='Scrapy developers',
    maintainer_email='info@scrapy.org',
    license='BSD',
    packages=find_packages(include=['scrapyd_client']),
    entry_points={
        'console_scripts': [
            'scrapyd-deploy = scrapyd_client.deploy:main',
            'scrapyd-client = scrapyd_client.cli:main'
        ]
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7.0',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=['requests', 'Scrapy>=0.17', 'six']
)
