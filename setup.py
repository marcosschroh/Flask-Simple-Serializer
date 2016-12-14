"""
Flask-Simple-Serializers
#!/usr/bin/env python

-------------

This is the description for that library
"""
from setuptools import setup

with open('README.md') as f:
    readme = f.read()


setup(
    name='Flask-Simple-Serializer',
    version='1.0',
    url='',
    license='BSD',
    author='Marcos Schroh',
    author_email='marcos.06sch@gmail.com',
    description='Simple Serializers for API validations',
    long_description=readme,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'WTForms',
        'Werkzeug',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
