from setuptools import setup, find_packages
version = '0.1'

setup(
    name='PySubdiv',
    version=version,
    packages=find_packages(),
    install_requires=['pyvista~=0.33.0',
                      'QtPy~=2.0.0',
                      'PyQt5~=5.15.6',
                      'pyvistaqt~=0.6.0',
                      'numba',
                      'vtk~=9.1.0',
                      'numpy~=1.22.0',
                      'setuptools~=57.0.0'],
    long_description='file : README.md',
    url='',
    include_package_data=True,
    license='',
    author='Mosaku Adeniyi'
)

