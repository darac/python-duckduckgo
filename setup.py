from setuptools import setup
from duckduckgo3 import __version__

long_description = open('README.rst').read()

setup(
      name='duckduckgo3',
      version=__version__,
      py_modules=['duckduckgo3'],
      description='Library for querying the Duck Duck Go API',
      author='Michael Stephens, Jacobi Petrucciani',
      author_email='jacobi@mimirhq.com',
      license='BSD',
      url='https://github.com/jpetrucciani/python-duckduckgo',
      long_description=long_description,
      platforms=['any'],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
                   ],
      entry_points={'console_scripts': ['ddg3 = duckduckgo:main']},
)
