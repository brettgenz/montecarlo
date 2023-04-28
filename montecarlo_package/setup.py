from setuptools import setup

setup(name='booklover',
      version='0.1',
      description="""This package organizes a reader's personal information, reading list, and book ratings.""",
      url='https://github.com/brettgenz/booklover',
      author='Brett Genz',
      author_email='brettgenz@gmail.com',
      license='MIT',
      packages=['booklover'],
      install_requires=['pandas']
     )