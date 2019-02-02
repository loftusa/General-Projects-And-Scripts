from chemspipy import ChemSpider
import urllib
import thermo
import os
import random

cs = ChemSpider('1eb28f6e-9627-41e6-abed-14bfc7a7503d')


def getImage(compound):
    c = cs.search(compound)[0]
    imgUrl = c.image_url
    urllib.request.urlretrieve(imgUrl, 'compound{}'.format(str(random.randint(1, 10))) + '.png')  # c.common_name


def getWeight(compound):
    c = cs.search(compound)[0]
    return str(c.molecular_weight)


def getBp(compound):
    c = cs.search(compound)[0]
    return float("{0:.3f}".format(thermo.Chemical(c.common_name).Tb - 273))


def getMp(compound):
    c = cs.search(compound)[0]
    return float("{0:.3f}".format(thermo.Chemical(c.common_name).Tm - 273))


def getDensity(compound):
    c = cs.search(compound)[0]
    return float(thermo.Chemical(c.common_name).rho * .001)


def getAll(compound):
    getImage(compound)
    print('Image created')
    print('Molecular Weight of ' + compound + ' is ' + getWeight(compound) + ' g/mol')
    print('Melting point of ' + compound + ' is ' + str(getMp(compound)) + ' C' + ' or ' + str(
        CToF(getMp(compound))) + ' F')
    print('Boiling point of ' + compound + ' is ' + str(getBp(compound)) + ' C' + ' or ' + str(
        CToF(getBp(compound))) + ' F')
    print('Density of ' + compound + ' is ' + str(getDensity(compound)) + ' g/ml')


def CToF(temp):
    return float("{0:.3f}".format(temp * 9 / 5 + 32))


def delPics():
    for i in os.listdir(os.getcwd()):
        if str(i).endswith('.png'):
            os.unlink(i)
        else:
            continue


compounds = 'CO2.h20.NaCl'.split('.')

delPics()

for i in compounds:
    try:
        getAll(i)
    except:
        print('no info for ' + str(i))
        continue
