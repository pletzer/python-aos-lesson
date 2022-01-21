import glob
import numpy as np
import xarray as xr
import dask
from dask.diagnostics import ProgressBar
import time


if __name__ == '__main__':

    tic = time.time()

    with dask.config.set(scheduler='processes'):

        pr_files = glob.glob('/nesi/nobackup/icshmo_python_aos/data/*.nc')

        ds = xr.open_mfdataset(pr_files, chunks={'time': 100})
        prmax_time = ds['pr'].max(('time', 'lat', 'lon'), keep_attrs=True)

        pr = prmax_time.compute()

    print(prmax_time.data)
    toc = time.time()
    print(f'max: {pr.values} took {toc - tic:.2f} sec')




