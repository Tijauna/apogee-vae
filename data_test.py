from astropy.io import fits
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Testing
print("Testing allstar")
with fits.open("allStar-r12-l33.fits") as allStar:
    allStar.info()

    for headers in allStar:
        print(headers)

    # Main header
    for items in allStar[0].header:
        print(items)

    #print(allStar[0].header)

    data = allStar[1].data
    print("Dimensions", data.shape)

print("\nTesting contspec")

with fits.open("contspec_dr16_final.fits") as contspec:
    contspec.info()

    print(contspec[0].header[0])
    print(contspec['PRIMARY'].data)

    data = contspec[0].data
    print("Dimensions", data.shape)
    print("Number of spectra: ", len(data))
    #plt.plot(data[15764])
    #plt.show()

print("\nTesting AstroNN catalog")
with fits.open("apogee_astroNN-DR16-v1.fits") as astroNNDR16:
    astroNNDR16.info()

    for headers in astroNNDR16:
        print(headers)

    # Main header
    for items in astroNNDR16[0].header:
        print(items)

    data = astroNNDR16[1].data
    print("Dimensions", data.shape)


print("\n ********************** Testing parameters, abundances, errors **********************")

star_hdus = fits.open('allStar-r12-l33.fits')
astroNN_hdus = fits.open('apogee_astroNN-DR16-v1.fits')
star_spec = fits.open('contspec_dr16_final.fits')

star = star_hdus[1].data
star_astroNN = astroNN_hdus[1].data
star_spectra = star_spec[0].data

star_hdus.close()
astroNN_hdus.close()
star_spec.close()

badbits = 2**23

print("\nAstroNN available fields:")
for name in star_astroNN.dtype.names:
    print(name)

# Get ASPCAP parameters, element abundances and errors for all stars 
# that were targeted as part of the main APOGEE survey

# Only grab target stars - criteria
criteria = (np.bitwise_and(star['aspcapflag'], badbits) == 0) & (star['extratarg']==0)
ind = np.where(criteria)[0]

print("Number of stars: ", len(star))

for i in range(10):
    # Title information
    print("\n**************** Looking at index ", i, " ****************")
    print("APSTAR ID: ", star['apstar_id'][i],\
         "\nTARGET_ID: ", star['target_id'][i],\
             "\nASPCAP_ID: ", star['aspcap_id'][i])
    
    print("\nBasic Stats:")
    print("SNR: ", star['snr'][i])
    print("Effective Temp (K) \t ASPCAP: ", star['teff_spec'][i], 'AstroNN:', star_astroNN['TEFF'][i])
    print("Surface G (log(cm/s^2) \t ASPCAP: ", star['logg_spec'][i], 'AstroNN:', star_astroNN['LOGG'][i])

    #j = ind[i]
    j = i

    plt.subplot(5, 2, j+1)
    plt.title(star['aspcap_id'][i])
    plt.xlabel('Wavelength')
    plt.ylabel('Relative Flux')
    # 7514 data points for each spectra
    plt.plot(star_spectra[j])

    spectra_df = pd.DataFrame(star_spectra[j])
    # Actual input data
    print("\nInput dataframe:")
    print(spectra_df)

    #print(len(star_spectra[j]))
    #plt.legend([star['aspcap_id'][i]])
    #plt.show()

    # Abundances, other info
    print("\nAbundances, additional info (ASPCAP):")
    print(star['ra'][j], star['dec'][j], star['glon'][j], star['glat'][j],\
        star['vhelio_avg'][j], star['vscatter'][j],\
        star['teff'][j], star['teff_err'][j],\
        star['logg'][j], star['logg_err'][j],\
        star['m_h'][j], star['m_h_err'][j],\
        star['alpha_m'][j], star['alpha_m_err'][j],\
        star['c_fe'][j], star['c_fe_err'][j],\
        star['cI_fe'][j], star['cI_fe_err'][j],\
        star['n_fe'][j], star['n_fe_err'][j],\
        star['o_fe'][j], star['o_fe_err'][j],\
        star['na_fe'][j], star['na_fe_err'][j],\
        star['mg_fe'][j], star['mg_fe_err'][j],\
        star['al_fe'][j], star['al_fe_err'][j],\
        star['si_fe'][j], star['si_fe_err'][j],\
        star['p_fe'][j], star['p_fe_err'][j],\
        star['s_fe'][j], star['s_fe_err'][j],\
        star['k_fe'][j], star['k_fe_err'][j],\
        star['ca_fe'][j], star['ca_fe_err'][j],\
        star['ti_fe'][j], star['ti_fe_err'][j],\
        star['v_fe'][j], star['v_fe_err'][j],\
        star['cr_fe'][j], star['cr_fe_err'][j],\
        star['mn_fe'][j], star['mn_fe_err'][j],\
        star['fe_h'][j], star['fe_h_err'][j],\
        star['co_fe'][j], star['co_fe_err'][j],\
        star['ni_fe'][j], star['ni_fe_err'][j],\
        star['cu_fe'][j], star['cu_fe_err'][j],\
        star['ge_fe'][j], star['ge_fe_err'][j],\
        star['rb_fe'][j], star['rb_fe_err'][j],\
        star['aspcapflags'][j], star['starflags'][j])

plt.subplots_adjust(hspace=1)
#plt.tight_layout()
plt.show()