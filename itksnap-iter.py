'''
CLI to iterate over multiple folders of images and segmentations with ITK-SNAP.
'''

import click
import pathlib
import os

@click.command()
@click.option('-p', '--path', default=pathlib.Path().absolute(), help='Path to the folders containing images and segmentations. Defaults to the current path.')
@click.option('-i', '--image-suffix', required=True, help='Suffix to add to the folder name to create the main image file name.')
@click.option('-s', '--segmentation-suffix', required=True, help='Suffix to add to the folder name to create the segmentation file name.')
@click.option('-a', '--additional-image-suffix', required=True, multiple=True, help='Suffix to add to the folder name to create the file name for an additional image.')
@click.option('-e', '--extension', default='.nii.gz', help='Extension for image and segmentation files. Defaults to .nii.gz.')
@click.option('-d', '--dry', is_flag=True, help="Dry run that only prints the command that would normally be called. The command is not actually run.")
def cli(path, image_suffix, segmentation_suffix, additional_image_suffix, extension, dry):
    '''Tool to iterate over multiple folders of images and segmentations with ITK-SNAP.'''

    # Sort and filter the folders at the `path`
    folders = sorted(os.listdir(os.path.abspath(path)))
    folders = [f for f in folders if f != '.DS_Store']

    # Create file names
    datasets = []
    for f in folders:
        d = {}
        d['image'] = os.path.join(path, f, f + image_suffix + extension)
        d['seg'] = os.path.join(path, f, f + segmentation_suffix + extension)
        d['add_images'] = [os.path.join(path, f, f + a + extension) for a in additional_image_suffix]
        for key, val in d.copy().items():
            if key != 'add_images':
                if not os.path.exists(val):
                    raise FileNotFoundError(val)
                else:
                    d[key] = val.replace(' ', '\ ')
            elif key == 'add_images':
                for i, a in enumerate(val):
                    if not os.path.exists(a):
                        raise FileNotFoundError(a)
                    else:
                        d[key][i] = a.replace(' ', '\ ')
        datasets.append(d)

    cmds = []
    for i, d in enumerate(datasets):
        cmd = f'itksnap -g {d["image"]}'
        cmd = f'{cmd} -s {d["seg"]}'
        cmd = f'{cmd} {" ".join(["-o"] + [a for a in d["add_images"]])}'
        cmds.append(cmd)
        print(f'[{i+1} of {len(datasets)}]')
        if dry:
            print(f'{cmd}\n')
        else:
            os.system(cmd)
        user_input = input('Any key to continue ("q" to quit): ').lower()
        if user_input == 'q' or user_input == 'quit':
            exit(0)

if __name__ == '__main__':
    cli()
