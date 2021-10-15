from astropy.io import fits


# Testing

print("Testing allstar")
with fits.open("allStar-r12-l33.fits") as allStar:
    # allStar.info()

    print(allStar[0].header[0])

    data = allStar[1].data
    print(data.shape)

# Testing
print("Testing contspec")

with fits.open("contspec_dr16_final.fits") as contspec:
    # allStar.info()

    print(contspec[0].header[0])

    data = contspec[0].data
    print(data.shape)