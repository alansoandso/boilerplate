from glob import glob
from os.path import basename
from os.path import splitext
from setuptools import find_packages
from setuptools import setup

install_requires = [
    'requests'
]

setup(name='tool',
      version='0.1',
      description='Sonething tool to display',
      author='Alan So',
      author_email='alansoandso@gmail.com',
      packages=['package'],
      include_package_data=True,
      entry_points={'console_scripts': ['tool = package.tool:command_line_runner', ]},
      # package_data={'pkg': ['pkg_data.yaml']},
      # include_package_data=True,
      install_requires=install_requires
      )


