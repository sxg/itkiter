'''
CLI to iterate over multiple folders of images and segmentations with ITK-SNAP.
'''

import click
import pathlib

@click.command()
@click.option('-p', '--path', default=pathlib.Path().absolute(), help='Path to the folders containing images and segmentations.')
def cli(path):
    print(path)

if __name__ == '__main__':
    cli()
