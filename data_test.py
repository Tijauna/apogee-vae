from astropy.io import fits


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

# Testing
print("\nTesting contspec")

with fits.open("contspec_dr16_final.fits") as contspec:
    contspec.info()

    print(contspec[0].header[0])
    print(contspec['PRIMARY'].data)

    data = contspec[0].data
    print("Dimensions", data.shape)

    from matplotlib import pyplot as plt
    plt.plot(data[15764])
    plt.show()