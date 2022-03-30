spin = str(input())
charge = str(input())

if charge == '-1/3':
    print('Strange', 'Quark')
elif charge == '2/3':
    print('Charm', 'Quark')
elif charge == '-1':
    print('Electron', 'Lepton')
elif spin == '1/2':
    print('Neutrino', 'Lepton')
elif spin == '1':
    print('Photon', 'Boson')