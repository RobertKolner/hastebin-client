from setuptools import setup

setup(
    # Metadata
    name='hastebin-client',
    version='0.1.2',
    description='Command line tool for uploading files to hastebin.com',
    keywords=['hastebin', 'haste', 'client'],

    # Origin
    url='https://github.com/RobertKolner/hastebin-client',
    download_url='https://github.com/RobertKolner/hastebin-client/releases/tag/0.1.1',
    author='Robert Kolner',
    author_email='robert.kolner@gmail.com',
    license='MIT',

    # Package data
    packages=['hastebin_client'],
    scripts=['bin/haste'],
    include_package_data=True,
    zip_safe=False,

    # Requirements
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
