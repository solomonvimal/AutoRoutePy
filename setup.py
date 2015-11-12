from setuptools import setup

setup(
    name='AutoRoutePy',
    version='0.0.1',
    description='Python scripting interface for the AutoRoute progam.'
                ' Has ability to Prepare input from RAPID output (www.rapid-hub.org).',
    keywords='AutoRoute',
    author='Alan Dee Snow',
    author_email='alan.d.snow@usace.army.mil',
    url='https://github.com/erdc-cm/AutoRoute-py',
    download_url='https://github.com/erdc-cm/AutoRoute-py/tarballs/0.0.1',
    license='MIT',
    packages=['AutoRoutePy'],
    install_requires=['condorpy', 'psutil', 'gdal', 'netCDF4', 'gdal'],
)
