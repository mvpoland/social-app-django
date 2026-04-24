# -*- coding: utf-8 -*-
"""Setup file for easy installation"""
import re

from os.path import join, dirname
from setuptools import setup

import social_django


setup(
    name='social-auth-app-django',
    version=social_django.__version__,
    author='Matias Aguirre',
    author_email='matiasaguirre@gmail.com',
    description='Python Social Authentication, Django integration.',
    license='BSD',
    keywords='django, social auth',
    url='https://github.com/python-social-auth/social-app-django',
    packages=[
        'social_django',
        'social_django.migrations',
        'social_django.management',
        'social_django.management.commands',
    ],
    long_description_content_type='text/markdown',
    install_requires=[
        'Django>=3.2',
        'social-auth-core>=3.3.3',
    ],
    python_requires=">=3.9",
    zip_safe=False
)
