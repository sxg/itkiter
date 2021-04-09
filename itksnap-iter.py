'''
CLI to iterate over multiple folders of images and segmentations with ITK-SNAP.
'''

import click
import pathlib

@click.command()
@click.option('-p', '--path', default=pathlib.Path().absolute(), help='Path to the folders containing images and segmentations. Defaults to the current path.')
@click.option('-i', '--image-suffix', required=True, help='Suffix to add to the folder name to create the main image file name.')
@click.option('-s', '--segmentation-suffix', required=True, help='Suffix to add to the folder name to create the segmentation file name.')
def cli(path, image_suffix, segmentation_suffix, additional_image_suffix):
    print(path)
@click.option('-a', '--additional-image-suffix', required=True, multiple=True, help='Suffix(es) to add to the folder name to create the file name for an additional image.')
@click.option('-e', '--extension', default='.nii.gz', help='Extension for image and segmentation files. Defaults to .nii.gz.')

if __name__ == '__main__':
    cli()
