from setuptools import setup, find_packages

setup(
    name='smartftp',
    version='2.7.2',
    url='https://github.com/lenz/smartftp',
    license='PYTHON SOFTWARE FOUNDATION LICENSE',
    author='Lenz Hirsch',
    author_email='hirsch@seamless.de',
    description='A fault tolerant fork of CPythons ftplib',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)
