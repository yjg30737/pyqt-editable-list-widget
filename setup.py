from setuptools import setup, find_packages

setup(
    name='pyqt-editable-list-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='Easily editable list widget',
    url='https://github.com/yjg30737/pyqt-editable-list-widget.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)