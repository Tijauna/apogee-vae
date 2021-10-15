from astropy.io import fits


# Testing

print("Testing allstar")
with fits.open("allStar-r12-l33.fits") as allStar:
    allStar.info()

    for headers in allStar:
        print(headers)

    print(allStar[0].header)
    data = allStar[1].data
    print("Dimensions", data.shape)

# Testing
print("\nTesting contspec")

with fits.open("contspec_dr16_final.fits") as contspec:
    contspec.info()

    print(contspec[0].header[0])
    print(contspec['PRIMARY'].data)

    data = contspec[0].data
    print("Dimensions", data.shape)