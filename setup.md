---
layout: page
title: Setup
---

## Software installation

In order to complete the lessons,
you will need access to the following:

* The bash shell
* A text editor
* Git
* Anaconda or Miniconda (which is a Python distribution)

If you don't already have these installed,
please follow The Carpentries [software installation instructions](https://carpentries.github.io/workshop-template/#setup).
(You do not need to install R, which is also listed at that site.)

> ## Troubeshooting
>
> If you have any trouble with software installation,
> The Carpentries maintain a list of common issues on their
> [Configuration Problems and Solutions wiki page](https://github.com/carpentries/workshop-template/wiki/Configuration-Problems-and-Solutions).
>
{: .callout}

## Code and Data

In your bash terminal, you will need to
~~~
$ git clone https:://github.com/pletzer/python-aos-lesson
~~~
{: .language-bash}

Then change your folder to 
~~~
$ cd python-aos-lesson/code
~~~
{: .language-bash}

and create a `data` folder 
~~~
$ mkdir data
~~~
{: .language-bash}

In the `data` directory, download the following files:
   - [pr_Amon_ACCESS-CM2_historical_r1i1p1f1_gn_201001-201412.nc][pr_access-cm_file]
   - [pr_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_201001-201412.nc][pr_access-esm_file]
   - [sftlf_fx_ACCESS-CM2_historical_r1i1p1f1_gn.nc][sftlf_access-cm_file]
   - [sftlf_fx_ACCESS-ESM1-5_historical_r1i1p1f1_gn.nc][sftlf_access-esm_file]


> ## Installation of additional python packages: via the command line

(Windows users may need to open the Anaconda Prompt program
and run `conda init bash` to make conda available at the Bash Shell.)

 **Step 1**

Add the conda-forge channel:
~~~
$ conda config --add channels conda-forge
~~~
{: .language-bash}


Create a new environment called `pyaos-lesson` and install the packages there:
~~~
$ conda create -n pyaos-lesson jupyter xarray dask netCDF4 cartopy cmocean cmdline_provenance defopt
~~~
{: .language-bash}

You can activate this new environment as follows:
~~~
$ conda activate pyaos-lesson
~~~
{: .language-bash}

## Software check

To check that everything is installed correctly, follow the instructions below.

**Bash Shell**

* *Linux*: Open the Terminal program via the applications menu. The default shell is usually Bash. If you aren't sure what yours is, type `echo $SHELL`. If the shell listed is not bash, type `bash` and press Enter to access Bash.
* *Mac*: Open the Applications Folder, and in Utilities select Terminal.
* *Windows*: Open the Git Bash program via the Windows start menu.

**Git**

* At the Bash Shell, type `git --version`. You should see the version of your Git program listed. 

**Anaconda**

* At the Bash Shell, type `python --version`. You should see the version of your Python program listed, with a reference to Anaconda (i.e. the default Python program on your laptop needs to be the Anaconda installation of Python).



[pr_access-cm_file]: {{ "/data/pr_Amon_ACCESS-CM2_historical_r1i1p1f1_gn_201001-201412.nc" | relative_url }}
[pr_access-esm_file]: {{ "/data/pr_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_201001-201412.nc" | relative_url }}
[sftlf_access-cm_file]: {{"/data/sftlf_fx_ACCESS-CM2_historical_r1i1p1f1_gn.nc" | relative_url }}
[sftlf_access-esm_file]: {{ "/data/sftlf_fx_ACCESS-ESM1-5_historical_r1i1p1f1_gn.nc" | relative_url }}
