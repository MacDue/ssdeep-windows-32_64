from setuptools import setup

setup(name='ssdeep-windows-32_64',
      version='0.0.1',
      description='Python wrapper for the ssdeep library with win 64 support',
      author='MacDue (forked from Intezer Labs Ltd)',
      packages=['ssdeep'],
      zip_safe=False,
      package_data={'ssdeep': ['bin/*.*']},
      install_requires=['six'])
