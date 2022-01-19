import pdb
import defopt

import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import cmocean
import cmdline_provenance as cmdprov
from typing import Literal


def convert_pr_units(darray):
    """Convert kg m-2 s-1 to mm day-1.
    
    Args:
      darray (xarray.DataArray): Precipitation data
    
    """
    
    assert darray.units == 'kg m-2 s-1', "Program assumes input units are kg m-2 s-1"
    
    darray.data = darray.data * 86400
    darray.attrs['units'] = 'mm/day'
    
    return darray


def apply_mask(darray, sftlf_file, realm):
    """Mask ocean or land using a sftlf (land surface fraction) file.
    
    Args:
      darray (xarray.DataArray): Data to mask
      sftlf_file (str): Land surface fraction file
      realm (str): Realm to mask
    
    """
   
    dset = xr.open_dataset(sftlf_file)
    if realm == 'land':
        masked_darray = darray.where(dset['sftlf'].data < 50)
    else:
        masked_darray = darray.where(dset['sftlf'].data > 50)   
   
    return masked_darray


def create_plot(clim, model, season, gridlines=False, levels=None):
    """Plot the precipitation climatology.
    
    Args:
      clim (xarray.DataArray): Precipitation climatology data
      model (str): Name of the climate model
      season (str): Season
      
    Kwargs:
      gridlines (bool): Select whether to plot gridlines
      levels (list): Tick marks on the colorbar    
    
    """

    if not levels:
        levels = np.arange(0, 13.5, 1.5)
        
    fig = plt.figure(figsize=[12,5])
    ax = fig.add_subplot(111, projection=ccrs.PlateCarree(central_longitude=180))
    clim.sel(season=season).plot.contourf(ax=ax,
                                          levels=levels,
                                          extend='max',
                                          transform=ccrs.PlateCarree(),
                                          cbar_kwargs={'label': clim.units},
                                          cmap=cmocean.cm.haline_r)
    ax.coastlines()
    if gridlines:
        plt.gca().gridlines()
    
    title = f'{model} precipitation climatology ({season})'
    plt.title(title)


def get_log_and_key(pr_file, history_attr, plot_type):
    """Get key and command line log for image metadata.
   
    Different image formats allow different metadata keys.
   
    Args:
      pr_file (str): Input precipitation file
      history_attr (str): History attribute from pr_file
      plot_type (str): File format for output image
   
    """
    
    valid_keys = {'png': 'History',
                  'pdf': 'Title',
                  'svg': 'Title',
                  'eps': 'Creator',
                  'ps' : 'Creator'}    

    assert plot_type in valid_keys.keys(), f"Image format not one of: {*[*valid_keys],}"
    log_key = valid_keys[plot_type]
    new_log = cmdprov.new_log(infile_logs={pr_file: history_attr})
    
    return log_key, new_log
   

#def main(pr_file: str, season: str, output_file: str, cbar_levels): #, cbar_levels, mask, gridlines: bool=False):
def main(pr_file: str, season: Literal['DJF', 'MAM', 'JJA', 'SON'], output_file: str, *, 
         gridlines: bool=False, cbar_levels: list[float]=None, mask: list[str]=None):
    """
    Plot the precipitation climatology for a given season.
    :param pr_file: Precipitation data file
    :param season: Season to plot
    :param output_file: Output file name
    :param cbar_levels: List of levels / tick marks to appear on the colorbar
    :param mask: Provide sftlf file and realm to mask
    :param gridlines:
    """

    dset = xr.open_dataset(pr_file)
    
    clim = dset['pr'].groupby('time.season').mean('time', keep_attrs=True)
    clim = convert_pr_units(clim)

    if mask:
        sftlf_file, realm = mask
        clim = apply_mask(clim, sftlf_file, realm)

    create_plot(clim, dset.attrs['source_id'], season,
                gridlines=gridlines, levels=cbar_levels)
                
    log_key, new_log = get_log_and_key(pr_file,
                                       dset.attrs['history'],
                                       output_file.split('.')[-1])
    plt.savefig(output_file, metadata={log_key: new_log}, dpi=200)


if __name__ == '__main__':
    defopt.run(main)