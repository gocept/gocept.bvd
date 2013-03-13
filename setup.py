from setuptools import setup, find_packages
import os

version = '0.1'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Download\n'
    '********\n'
    )

setup(name='gocept.bvd',
      version=version,
      description="Script to extract version information from buildouts.",
      long_description=long_description,
      classifiers=[
          "Programming Language :: Python",
        ],
      keywords='',
      author='Daniel Havlik',
      author_email='dh@gocept.com',
      url='http://gocept.com',
      license='BSD',
      packages=find_packages('src', exclude=['ez_setup']),
      package_data = {},
      package_dir = {'':'src'},
      namespace_packages=['gocept'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points={
        'console_scripts': [
            'extract_versions = gocept.bvd.extract_versions:main',],
        }, 
      )
