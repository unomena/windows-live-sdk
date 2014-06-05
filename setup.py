from setuptools import setup, find_packages

setup(
    name='windows-live-sdk',
    version='0.0.1',
    description='Python bindings for Windows Live OAuth and API',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read(),
    author='Michael Whelehan',
    author_email='dev@unomena.com',
    license='BSD',
    url='http://git.unomena.net/unomena/windows-live-sdk',
    packages = find_packages(),
    dependency_links = [
    ],
    install_requires = [
        'requests==2.0.0',
    ],
    tests_require=[
        'django-setuptest>=0.1.2',
        'pysqlite>=2.5',
	    'requests==2.0.0'
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
