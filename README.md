This repository contains code that can be used to generate
a "seed image" from input source catalogs. This seed image will
then be used as input to later steps in the NIRCam Data
Simulator (not included in this repo yet).

The seed image is a noiseless countrate image containing
all of the sources specified in the input catalogs. Sources
are scaled to the requested magnitudes and placed in the
appropriate location given the NIRCam distortion model.

The main input to the code is a yaml file (examples are
in the 'inputs' subdirectory). This file contains more
information than is actually needed to run the code,
but the information is all needed to run the entire
NIRCam Data Simulator, so for the moment we've kept all
of the inputs.

Input fields used here include:

Inst:
  mode: examples - 'imaging', 'WFSS'

Readout:
  array_name e.g. NRCB5_FULL
  filter
  pupil

Reffiles:
  subarray_defs - file located in 'config' subdirectory
  astrometric - CRDS-formatted distortion reference file
  distortion_coeffs - SIAF
  flux_cal - file with zeropoints located in 'config' subdirectory

simSignals:
  pointsource - ptsrc catalog, example in 'catalogs' subdirectory
  psfpath - path to PSF library
  psfbasename - base name of files in library
  psfpixfrac - subpixel resolution of PSF library files
  psfwfe - wavefront error to use
  psfwfegroup - realization number for a given WFE
  galaxyListFile - galaxy catalog, example in 'catalogs' subdirectory
  extended - catalog of extended sources

  (Obsolete?)
  extendedscale - multiplicative factor to scale extended target brightness
  extendedCenter - pixel location to place extended object

  PSFConvolveExtended - True/False, convolve extended objects with NIRCam PSF
  movingTargetList - catalog of targets to trail across FOV (e.g KBOs while observing a sidereal target)
  movingTargetSersic - catalog of "galaxies" (2D Sersic profiles) to trail across FOV
  movingTargetExtended - catalog of extended sources to trail across FOV
  movingTargetToTrack - catalog of a non-sidereal target to track. In this case, all targets in the pointsource,
                        galaxyListFile, and extended catalogs will be trailed across the FOV. To use this, set
			the 'mode' keyword at the top to 'moving_target'
  bkgdrate - Uniform background signal to add, in units of ADU/sec

Telescope:
  ra: RA at the reference location of the detector/aperture being simulated
  dec: Dec at the reference location of the detector/aperture being simulated
  rotation: PAV3 of the telescope (degrees E of N)

Output:
  file: filename used as a base for the seed image output
  directory: directory in which to place the output
  save_intermediates: True/False, save intermediate data products
  grism_source_image: True/False. If true, the length and width of the seed image are increased to larger than
                                  the detector FOV



To use the code:

1) From the command line:
python catalog_seed_image.py myfile.yaml

2) Within python:
from catalog_seed_image.catalog_seed_image import catalog_seed_image as csi
cat = csi.Catalog_seed()
cat.paramfile = 'myfile.yaml'
cat.run()


Outputs:

Multi-extension fits file with name ending in 'seed_image.fits', containing:

Extension 0: empty
Extension 1: seed image
Extension 2: segmentation map

Also, the seed image, segmentation map, and exposure info dictionary are
available as:
self.seedimage, self.seed_segmap, and self.seedinfo

