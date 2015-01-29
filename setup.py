from setuptools import setup

setup(
    name='sdkbuild',
    version='0.1',
    description='Compiling SDK templates',
    url='https://github.com/samdmarshall/SDKBuild',
    author='Sam Marshall',
    author_email='me@samdmarshall.com',
    license='BSD 3-Clause',
    packages=['sdkbuild', 'sdkbuild/sdk', 'sdkbuild/commandparse', 'sdkbuild/settings'],
    entry_points = {
        'console_scripts': ['sdkbuild = sdkbuild:main'],
    },
    zip_safe=False
)