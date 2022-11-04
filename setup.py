import  setuptools

setuptools.setup(
    name='mypack',
    author='Luke Damkoehler',
    author_email='ljdamkoehler@gmail.com',
    description='Proof of concept for CCI',
    url='https://github.com/ljdamkoehler/mypack',
    project_urls={'Source Code': 'https://github.com/ljdamkoehler/mypack'},
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
)