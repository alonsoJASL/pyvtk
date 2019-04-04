# Setup for anaconda

## Donwlooad and install

Go online, download and install. It's mostly common things.

## Installing VTK/ITK
Run the following
```bash
conda install -c conda-forge itk
conda install -c anaconda vtk
```
## Create an environment
In case there's different versions needed or whatever. Create an environment
so things are neat and organised:
```bash
conda create --name [SOME_NAME] python=3 [PACHAGES]
```
There is a default environment called `base`.
## To actually use the correct python when working
By default the base should do:
```bash
conda activate base
```
Otherwise, change `base` for the `SOME_NAME` you chose.
