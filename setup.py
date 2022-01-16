from setuptools import setup

required: list

with open('requirements.txt') as f:
    required = f.readlines()

setup(
    name='dbsync',
    version='0.2.0',
    py_modules=['dbsync'],
    install_requires=[x.strip() for x in required],
    entry_points='''
        [console_scripts]
        dbsync=dbsync:main
    '''
)
