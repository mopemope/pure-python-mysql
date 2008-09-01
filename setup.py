from distutils.core import setup
#from distutils.command.install_data import install_data
#from distutils.command.install import INSTALL_SCHEMES
import os
import sys


version_tuple = __import__('pymysql').VERSION

if version_tuple[2] is not None:
    version = "%d.%d_%s" % version_tuple
else:
    version = "%d.%d" % version_tuple[:2]

setup(
    name = "PyMySQL",
    version = version,
    url = '',
    author = 'yutaka.matsubara',
    author_email = 'yutaka.matsubara@gmail.com',
    description = 'Pure Python MySQL Driver ',
    packages = ['pymysql', 'pymysql.constants']
)
