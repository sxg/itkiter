'''
CLI to iterate over multiple folders of images and segmentations with ITK-SNAP.
'''

import setuptools

setuptools.setup(
    name='itksnap-iter',
    version='1.0.0',
    description='CLI to iterate over multiple folders of images and segmentations with ITK-SNAP.',
    author='Satyam Ghodasara',
    author_email='sghodas@gmail.com',
    url='https://github.com/sxg/itksnap-iter',
    py_modules=['itksnap-iter'],
    packages=setuptools.find_packages(),
    install_requires=[
        'click'
    ]
)