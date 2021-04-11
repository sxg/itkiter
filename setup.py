'''
CLI to iterate over multiple folders of images and segmentations with ITK-SNAP.
'''

import setuptools

setuptools.setup(
    name='itkiter',
    version='1.1.1',
    description='CLI to iterate over multiple folders of images and segmentations with ITK-SNAP.',
    author='Satyam Ghodasara',
    author_email='sghodas@gmail.com',
    url='https://github.com/sxg/itksnap-iter',
    py_modules=['itkiter'],
    packages=setuptools.find_packages(),
    install_requires=[
        'click'
    ],
    entry_points={
        'console_scripts': [
            'itkiter = itkiter:cli'
        ]
    }
)