from setuptools import setup, find_packages

setup( name='displays',
    version = '0.0.1',
    description = 'Displays of Content based on Entropy and Platforms',
    author = 'Daryl Antony',
    author_email = 'daryl@commoncode.com.au',
    url = 'https://github.com/commoncode/displays',
    keywords = ['django',],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    dependency_links = [
        'http://github.com/commoncode/entropy/tarball/master#egg=django-entropy-0.0.3',
        'http://github.com/commoncode/platforms/tarball/master#egg=platforms-0.0.2',
        'http://github.com/commoncode/platforms/tarball/master#egg=menus-0.0.2',
        'http://github.com/commoncode/platforms/tarball/master#egg=positions-0.0.1',
    ],
    setup_requires = [
        'pip',
    ],
    install_requires = [
        'django-entropy',
        'platforms',
        'menus',
        'positions',
    ]
)
