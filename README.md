# itkiter
CLI to iterate over multiple folders containing images and segmentations with ITK-SNAP.

## Help

```
Usage: itkiter [OPTIONS]

  Tool to iterate over multiple folders of images and segmentations with
  ITK-SNAP.

Options:
  -p, --path TEXT                 Path to the folders containing images and
                                  segmentations. Defaults to the current path.

  -i, --image-suffix TEXT         Suffix to add to the folder name to create
                                  the main image file name.  [required]

  -s, --segmentation-suffix TEXT  Suffix to add to the folder name to create
                                  the segmentation file name.  [required]

  -a, --additional-image-suffix TEXT
                                  Suffix to add to the folder name to create
                                  the file name for an additional image.
                                  [required]

  -e, --extension TEXT            Extension for image and segmentation files.
                                  Defaults to .nii.gz.

  -d, --dry                       Dry run that only prints the command that
                                  would normally be called. The command is not
                                  actually run.

  --version                       Show the version and exit.
  --help                          Show this message and exit.
```
