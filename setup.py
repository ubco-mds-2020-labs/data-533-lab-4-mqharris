from setuptools import setup, find_packages

setup(
    name='quickscreen',
    version='0.1',
    packages=find_packages(exclude=[
        'tests*',
         "data", 
         "example.ipynb",
         "description.md"
         ]),
    install_requires=["pandas", "numpy", "matplotlib", "seaborn", "scikit-learn"],
    license='MIT',
    description='A package for exploring data',
    url='https://github.com/mqharris/533_lab2',
    author='Nathan Smith, Mitch Harris, Ryan Koenig',
    author_email='blank'
)
