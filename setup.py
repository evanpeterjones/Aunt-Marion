from setuptools import setup, find_packages
 
setup(name='auntmarion',
      version='0.1',
      url='https://github.com/evanpeterjones/Aunt-Marion',
      license='MIT',
      author='Evan Jones',
      author_email='evan.peter.jones@gmail.com',
      description='a simple text-to-speech-ish wav file generator',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)
