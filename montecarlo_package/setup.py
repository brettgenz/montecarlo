from setuptools import setup

setup(name='booklover',
      version='0.1',
      description="""This package provides a framework to conduct a Monte Carlo simulation.""",
      url='https://github.com/brettgenz/montecarlo',
      author='Brett Genz',
      author_email='brettgenz@gmail.com',
      license='MIT',
      packages=['montecarlo'],
      install_requires=['pandas', 'numpy']
     )
