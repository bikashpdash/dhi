from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='DHI: The Intelligence',
    long_description=readme,
    author='Bikash P Dash',
    author_email='bikashprakashdash@gmail.com',
    url='na',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

