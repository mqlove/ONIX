nuc_name_dic = {}

nuc_name_dic["Be"] = 4
nuc_name_dic["Ba"] = 56
nuc_name_dic["Bh"] = 107
nuc_name_dic["Bi"] = 83
nuc_name_dic["Bk"] = 97
nuc_name_dic["Br"] = 35
nuc_name_dic["Ru"] = 44
nuc_name_dic["Re"] = 75
nuc_name_dic["Rf"] = 104
nuc_name_dic["Rg"] = 111
nuc_name_dic["Ra"] = 88
nuc_name_dic["Rb"] = 37
nuc_name_dic["Rn"] = 86
nuc_name_dic["Rh"] = 45
nuc_name_dic["Tm"] = 69
nuc_name_dic["H"] = 1
nuc_name_dic["P"] = 15
nuc_name_dic["Ge"] = 32
nuc_name_dic["Gd"] = 64
nuc_name_dic["Ga"] = 31
nuc_name_dic["Os"] = 76
nuc_name_dic["Hs"] = 108
nuc_name_dic["Zn"] = 30
nuc_name_dic["Ho"] = 67
nuc_name_dic["Hf"] = 72
nuc_name_dic["Hg"] = 80
nuc_name_dic["He"] = 2
nuc_name_dic["Pr"] = 59
nuc_name_dic["Pt"] = 78
nuc_name_dic["Pu"] = 94
nuc_name_dic["Pb"] = 82
nuc_name_dic["Pa"] = 91
nuc_name_dic["Pd"] = 46
nuc_name_dic["Po"] = 84
nuc_name_dic["Pm"] = 61
nuc_name_dic["C"] = 6
nuc_name_dic["K"] = 19
nuc_name_dic["O"] = 8
nuc_name_dic["S"] = 16
nuc_name_dic["W"] = 74
nuc_name_dic["Eu"] = 63
nuc_name_dic["Es"] = 99
nuc_name_dic["Er"] = 68
nuc_name_dic["Md"] = 101
nuc_name_dic["Mg"] = 12
nuc_name_dic["Mo"] = 42
nuc_name_dic["Mn"] = 25
nuc_name_dic["Mt"] = 109
nuc_name_dic["U"] = 92
nuc_name_dic["Fr"] = 87
nuc_name_dic["Fe"] = 26
nuc_name_dic["Fm"] = 100
nuc_name_dic["Ni"] = 28
nuc_name_dic["No"] = 102
nuc_name_dic["Na"] = 11
nuc_name_dic["Nb"] = 41
nuc_name_dic["Nd"] = 60
nuc_name_dic["Ne"] = 10
nuc_name_dic["Zr"] = 40
nuc_name_dic["Np"] = 93
nuc_name_dic["B"] = 5
nuc_name_dic["Co"] = 27
nuc_name_dic["Cm"] = 96
nuc_name_dic["F"] = 9
nuc_name_dic["Ca"] = 20
nuc_name_dic["Cf"] = 98
nuc_name_dic["Ce"] = 58
nuc_name_dic["Cd"] = 48
nuc_name_dic["V"] = 23
nuc_name_dic["Cs"] = 55
nuc_name_dic["Cr"] = 24
nuc_name_dic["Cu"] = 29
nuc_name_dic["Sr"] = 38
nuc_name_dic["Kr"] = 36
nuc_name_dic["Si"] = 14
nuc_name_dic["Sn"] = 50
nuc_name_dic["Sm"] = 62
nuc_name_dic["Sc"] = 21
nuc_name_dic["Sb"] = 51
nuc_name_dic["Sg"] = 106
nuc_name_dic["Se"] = 34
nuc_name_dic["Yb"] = 70
nuc_name_dic["Db"] = 105
nuc_name_dic["Dy"] = 66
nuc_name_dic["Ds"] = 110
nuc_name_dic["La"] = 57
nuc_name_dic["Cl"] = 17
nuc_name_dic["Li"] = 3
nuc_name_dic["Tl"] = 81
nuc_name_dic["Lu"] = 71
nuc_name_dic["Lr"] = 103
nuc_name_dic["Th"] = 90
nuc_name_dic["Ti"] = 22
nuc_name_dic["Te"] = 52
nuc_name_dic["Tb"] = 65
nuc_name_dic["Tc"] = 43
nuc_name_dic["Ta"] = 73
nuc_name_dic["Ac"] = 89
nuc_name_dic["Ag"] = 47
nuc_name_dic["I"] = 53
nuc_name_dic["Ir"] = 77
nuc_name_dic["Am"] = 95
nuc_name_dic["Al"] = 13
nuc_name_dic["As"] = 33
nuc_name_dic["Ar"] = 18
nuc_name_dic["Au"] = 79
nuc_name_dic["At"] = 85
nuc_name_dic["In"] = 49
nuc_name_dic["Y"] = 39
nuc_name_dic["N"] = 7
nuc_name_dic["Xe"] = 54
nuc_name_dic["Cn"] = 112
nuc_name_dic["Fl"] = 114
nuc_name_dic["Lv"] = 116

# From OpenMC
# Isotopic abundances from Meija J, Coplen T B, et al, "Isotopic compositions
# of the elements 2013 (IUPAC Technical Report)", Pure. Appl. Chem. 88 (3),
# pp. 293-306 (2013). The "representative isotopic abundance" values from
# column 9 are used except where an interval is given, in which case the
# "best measurement" is used.
NATURAL_ABUNDANCE = {
    'H1': 0.99984426, 'H2': 0.00015574, 'He3': 0.000002,
    'He4': 0.999998, 'Li6': 0.07589, 'Li7': 0.92411,
    'Be9': 1.0, 'B10': 0.1982, 'B11': 0.8018,
    'C12': 0.988922, 'C13': 0.011078, 'N14': 0.996337,
    'N15': 0.003663, 'O16': 0.9976206, 'O17': 0.000379,
    'O18': 0.0020004, 'F19': 1.0, 'Ne20': 0.9048,
    'Ne21': 0.0027, 'Ne22': 0.0925, 'Na23': 1.0,
    'Mg24': 0.78951, 'Mg25': 0.1002, 'Mg26': 0.11029,
    'Al27': 1.0, 'Si28': 0.9222968, 'Si29': 0.0468316,
    'Si30': 0.0308716, 'P31': 1.0, 'S32': 0.9504074,
    'S33': 0.0074869, 'S34': 0.0419599, 'S36': 0.0001458,
    'Cl35': 0.757647, 'Cl37': 0.242353, 'Ar36': 0.003336,
    'Ar38': 0.000629, 'Ar40': 0.996035, 'K39': 0.932581,
    'K40': 0.000117, 'K41': 0.067302, 'Ca40': 0.96941,
    'Ca42': 0.00647, 'Ca43': 0.00135, 'Ca44': 0.02086,
    'Ca46': 0.00004, 'Ca48': 0.00187, 'Sc45': 1.0,
    'Ti46': 0.0825, 'Ti47': 0.0744, 'Ti48': 0.7372,
    'Ti49': 0.0541, 'Ti50': 0.0518, 'V50': 0.0025,
    'V51': 0.9975, 'Cr50': 0.04345, 'Cr52': 0.83789,
    'Cr53': 0.09501, 'Cr54': 0.02365, 'Mn55': 1.0,
    'Fe54': 0.05845, 'Fe56': 0.91754, 'Fe57': 0.02119,
    'Fe58': 0.00282, 'Co59': 1.0, 'Ni58': 0.680769,
    'Ni60': 0.262231, 'Ni61': 0.011399, 'Ni62': 0.036345,
    'Ni64': 0.009256, 'Cu63': 0.6915, 'Cu65': 0.3085,
    'Zn64': 0.4917, 'Zn66': 0.2773, 'Zn67': 0.0404,
    'Zn68': 0.1845, 'Zn70': 0.0061, 'Ga69': 0.60108,
    'Ga71': 0.39892, 'Ge70': 0.2052, 'Ge72': 0.2745,
    'Ge73': 0.0776, 'Ge74': 0.3652, 'Ge76': 0.0775,
    'As75': 1.0, 'Se74': 0.0086, 'Se76': 0.0923,
    'Se77': 0.076, 'Se78': 0.2369, 'Se80': 0.498,
    'Se82': 0.0882, 'Br79': 0.50686, 'Br81': 0.49314,
    'Kr78': 0.00355, 'Kr80': 0.02286, 'Kr82': 0.11593,
    'Kr83': 0.115, 'Kr84': 0.56987, 'Kr86': 0.17279,
    'Rb85': 0.7217, 'Rb87': 0.2783, 'Sr84': 0.0056,
    'Sr86': 0.0986, 'Sr87': 0.07, 'Sr88': 0.8258,
    'Y89': 1.0, 'Zr90': 0.5145, 'Zr91': 0.1122,
    'Zr92': 0.1715, 'Zr94': 0.1738, 'Zr96': 0.028,
    'Nb93': 1.0, 'Mo92': 0.14649, 'Mo94': 0.09187,
    'Mo95': 0.15873, 'Mo96': 0.16673, 'Mo97': 0.09582,
    'Mo98': 0.24292, 'Mo100': 0.09744, 'Ru96': 0.0554,
    'Ru98': 0.0187, 'Ru99': 0.1276, 'Ru100': 0.126,
    'Ru101': 0.1706, 'Ru102': 0.3155, 'Ru104': 0.1862,
    'Rh103': 1.0, 'Pd102': 0.0102, 'Pd104': 0.1114,
    'Pd105': 0.2233, 'Pd106': 0.2733, 'Pd108': 0.2646,
    'Pd110': 0.1172, 'Ag107': 0.51839, 'Ag109': 0.48161,
    'Cd106': 0.01245, 'Cd108': 0.00888, 'Cd110': 0.1247,
    'Cd111': 0.12795, 'Cd112': 0.24109, 'Cd113': 0.12227,
    'Cd114': 0.28754, 'Cd116': 0.07512, 'In113': 0.04281,
    'In115': 0.95719, 'Sn112': 0.0097, 'Sn114': 0.0066,
    'Sn115': 0.0034, 'Sn116': 0.1454, 'Sn117': 0.0768,
    'Sn118': 0.2422, 'Sn119': 0.0859, 'Sn120': 0.3258,
    'Sn122': 0.0463, 'Sn124': 0.0579, 'Sb121': 0.5721,
    'Sb123': 0.4279, 'Te120': 0.0009, 'Te122': 0.0255,
    'Te123': 0.0089, 'Te124': 0.0474, 'Te125': 0.0707,
    'Te126': 0.1884, 'Te128': 0.3174, 'Te130': 0.3408,
    'I127': 1.0, 'Xe124': 0.00095, 'Xe126': 0.00089,
    'Xe128': 0.0191, 'Xe129': 0.26401, 'Xe130': 0.04071,
    'Xe131': 0.21232, 'Xe132': 0.26909, 'Xe134': 0.10436,
    'Xe136': 0.08857, 'Cs133': 1.0, 'Ba130': 0.0011,
    'Ba132': 0.001, 'Ba134': 0.0242, 'Ba135': 0.0659,
    'Ba136': 0.0785, 'Ba137': 0.1123, 'Ba138': 0.717,
    'La138': 0.0008881, 'La139': 0.9991119, 'Ce136': 0.00186,
    'Ce138': 0.00251, 'Ce140': 0.88449, 'Ce142': 0.11114,
    'Pr141': 1.0, 'Nd142': 0.27153, 'Nd143': 0.12173,
    'Nd144': 0.23798, 'Nd145': 0.08293, 'Nd146': 0.17189,
    'Nd148': 0.05756, 'Nd150': 0.05638, 'Sm144': 0.0308,
    'Sm147': 0.15, 'Sm148': 0.1125, 'Sm149': 0.1382,
    'Sm150': 0.0737, 'Sm152': 0.2674, 'Sm154': 0.2274,
    'Eu151': 0.4781, 'Eu153': 0.5219, 'Gd152': 0.002,
    'Gd154': 0.0218, 'Gd155': 0.148, 'Gd156': 0.2047,
    'Gd157': 0.1565, 'Gd158': 0.2484, 'Gd160': 0.2186,
    'Tb159': 1.0, 'Dy156': 0.00056, 'Dy158': 0.00095,
    'Dy160': 0.02329, 'Dy161': 0.18889, 'Dy162': 0.25475,
    'Dy163': 0.24896, 'Dy164': 0.2826, 'Ho165': 1.0,
    'Er162': 0.00139, 'Er164': 0.01601, 'Er166': 0.33503,
    'Er167': 0.22869, 'Er168': 0.26978, 'Er170': 0.1491,
    'Tm169': 1.0, 'Yb168': 0.00123, 'Yb170': 0.02982,
    'Yb171': 0.14086, 'Yb172': 0.21686, 'Yb173': 0.16103,
    'Yb174': 0.32025, 'Yb176': 0.12995, 'Lu175': 0.97401,
    'Lu176': 0.02599, 'Hf174': 0.0016, 'Hf176': 0.0526,
    'Hf177': 0.186, 'Hf178': 0.2728, 'Hf179': 0.1362,
    'Hf180': 0.3508, 'Ta180': 0.0001201, 'Ta181': 0.9998799,
    'W180': 0.0012, 'W182': 0.265, 'W183': 0.1431,
    'W184': 0.3064, 'W186': 0.2843, 'Re185': 0.374,
    'Re187': 0.626, 'Os184': 0.0002, 'Os186': 0.0159,
    'Os187': 0.0196, 'Os188': 0.1324, 'Os189': 0.1615,
    'Os190': 0.2626, 'Os192': 0.4078, 'Ir191': 0.373,
    'Ir193': 0.627, 'Pt190': 0.00012, 'Pt192': 0.00782,
    'Pt194': 0.32864, 'Pt195': 0.33775, 'Pt196': 0.25211,
    'Pt198': 0.07356, 'Au197': 1.0, 'Hg196': 0.0015,
    'Hg198': 0.1004, 'Hg199': 0.1694, 'Hg200': 0.2314,
    'Hg201': 0.1317, 'Hg202': 0.2974, 'Hg204': 0.0682,
    'Tl203': 0.29524, 'Tl205': 0.70476, 'Pb204': 0.014,
    'Pb206': 0.241, 'Pb207': 0.221, 'Pb208': 0.524,
    'Bi209': 1.0, 'Th230': 0.0002, 'Th232': 0.9998,
    'Pa231': 1.0, 'U234': 0.000054, 'U235': 0.007204,
    'U238': 0.992742
}


nuc_zz_dic = {v: k for k, v in list(nuc_name_dic.items())}

MT_dic = {102: '(n,gamma)', 18: 'fission', 16: '(n,2n)', 17:'(n,3n)', 22:'(n,a)', 105:'(n,t)'}

xs_key = ['(n,gamma)', '(n,gamma)X', '(n,2n)', '(n,2n)X', '(n,a)', '(n,p)', 'fisson', '(n,3n)', '(n,t)', 'removal']


fiss_nuc = ['902320', '922330', '922350', '922380', '942390', '942410', '962450', '982490']

# reac_product = {'(n,gamma)':[0,1,0],'(n,2n)':[0,-1,0],'(n,3n)':[0,-2,0],'(n,p)':[-1,0,0],'(n,a)':[-2,-3,0],'(n,2n)X':[0,-1,1],'(n,gamma)X':[0,1,1]}
# reac_product_fromX = {'(n,gamma)':[0,1,-1],'(n,2n)':[0,-1,-1],'(n,3n)':[0,-2,-1],'(n,p)':[-1,0,-1],'(n,a)':[-2,-3,-1],'(n,2n)X':[0,-1,0],'(n,gamma)X':[0,1,0]}

# decay_product = {'betaneg':[1,0,0], 'betanegX':[1,0,1], 'betapos':[-1,0,0], 'betaposX':[-1,0,1], 'alpha':[-2,-4,0], 'gamma':[0,0,-1]}
# decay_product_fromX = {'betaneg':[1,0,-1], 'betanegX':[1,0,0], 'betapos':[-1,0,-1], 'betaposX':[-1,0,0], 'alpha':[-2,-4,-1], 'gamma':[0,0,-1]}
        

# There are four type of dic for reaction production. First, depending on whether the father nuclide is excited or not. Then it depends 
# if the son is excited or not. Overall there should be four dic: stable to stable, stable to excited, excited to stable, and excited to excited

xs_prod_fromS_toS = {'(n,gamma)':[0,1,0],'(n,2n)':[0,-1,0],'(n,3n)':[0,-2,0],'(n,p)':[-1,0,0],'(n,a)':[-2,-3,0], '(n,t)': [-1,-2,0]}
xs_prod_fromS_toX = {'(n,2n)X':[0,-1,1],'(n,gamma)X':[0,1,1]}
xs_prod_fromX_toS = {'X(n,gamma)':[0,1,-1],'X(n,2n)':[0,-1,-1],'X(n,3n)':[0,-2,-1],'X(n,p)':[-1,0,-1],'X(n,a)':[-2,-3,-1], 'X(n,t)':[-1,-2,-1]}
xs_prod_fromX_toX = {'X(n,2n)X':[0,-1,0],'X(n,gamma)X':[0,1,0]}


decay_prod_fromS_toS = {'betaneg':[1,0,0], 'betapos':[-1,0,0], 'alpha':[-2,-4,0], 'neutron':[0,-1,0], 'proton':[-1,-1,0]}
decay_prod_fromS_toX = {'betanegX':[1,0,1], 'betaposX':[-1,0,1], 'alphaX':[-2,-4,1],'neutronX':[0,-1,1],'protonX':[-1,-1,1]}
decay_prod_fromX_toS = {'Xbetaneg':[1,0,-1], 'Xbetapos':[-1,0,-1],'Xalpha':[-2,-4,-1],'Xgamma':[0,0,-1],'Xneutron':[0,-1,-1],'Xproton':[-1,-1,-1]}
decay_prod_fromX_toX = {'XbetanegX':[1,0,0], 'XbetaposX':[-1,0,0],'XalphaX':[-2,-4,0], 'XneutronX':[0,-1,0], 'XprotonX':[-1,-1,0]}



#Old and erroneous dic (10e3y while it should be 1e3y, and I forgot to convert to second)
#time_dic = {'s': 1, 'm': 60, 'h':3600, 'd': 24*3600, 'y': 24*3600*365, '10e3y':10e3, '10e6y':10e6, '10e9y':10e9}

# New and correct dic
#time_dic = {'s': 1, 'm': 60, 'h':3600, 'd': 24*3600, 'y': 24*3600*365, '1e3y':1e3*24*3600*365, '1e6y':1e6*24*3600*365, '1e9y':1e9*24*3600*365}
time_dic = {'s': 1, 'm': 60, 'h':3600, 'd': 24*3600, 'y': 24*3600*365.25, '1e3y':1e3*24*3600*365.25, '1e6y':1e6*24*3600*365.25, '1e9y':1e9*24*3600*365.25}

unit_dic = {'m':1e-3, 'c':1e-2, 'd':1e-1, 'k':1e3, 'M':1e6, 'G':1e9}

nucl_FAM = ['Actinides', 'Fission Products', 'Activation Products']

stable_dic_b = ['n/a', 0., 'stable', 0.,  0.,  0.,  0.,  0.,  0.]

decay_key_b = ['unit','total', 'half-life', 'betaneg', 'betanegX', 'betapos', 'betaposX', 'alpha', 'gamma']

stable_dic_a = [ 0., 'stable', 0.,  0.,  0.,  0.,  0.,  0.]

decay_key_a = ['total', 'half-life', 'betaneg', 'betanegX', 'betapos', 'betaposX', 'alpha', 'gamma']

xs_lib_object_name_dict = {'ngamma': '(n,gamma)', 'n2n': '(n,2n)', 'n3n':'(n,3n)', 'nalpha':'(n,alpha)', 'fission': 'fission', 'removal': 'removal'}

# NAX nuclides list
# This is a list of useful and potentially useful isotopes for forensic and nuclear archaeology
# Part of these nuclides have been gathered from papers on forensic and nuclear archaeology and the other
# from my own research

NAX_nucl_list = ['30060', '30070', '40100', '50100', '50110', '60140', '110220', '170350', '170360', '170370', '200410', '200420', '220460', '220470', '220480', '220490', '220500', '240530', '240540', '260540', '260550', '260560', '260570', '260580', '280590', '280610', '280620', '280630', '280640', '320720', '340760', '340770', '340780', '370850', '380860', '380870', '380880','380890' ,'380900', '400900', '400910', '400920', '400930','400940','400950', '400960', '410930', '420940', '420950', '420960', '420970', '420980','420990', '421000', '430980', '440980', '440990', '441000', '441010', '441020','441030','441040','441050', '441060', '451010', '451020', '461040', '461050', '461060','461070','461080','461090', '461100', '471090', '471101', '481080','481090', '481100', '481110', '481120', '481130', '481140', '491130','491140', '491150', '501150', '501160', '501170', '501180', '501190', '501191', '501200','501210','501220','501230','501240','501250', '501260', '511230','511240', '511250', '521220', '521230', '521240', '521250', '521260', '521271', '521300', '531270', '551330', '551340', '551350', '551370', '551440', '561320', '561340', '561370', '561380', '571380', '571390', '581400', '581420', '581440', '601430', '601440', '601480', '611460', '611470', '621470', '621490', '621500', '631510', '631530', '641520', '641530', '641540', '641550', '641560', '641570', '641580', '661600', '661610', '661620', '661630', '661640', '681660', '681670', '681680', '721740', '721760', '721770', '721780', '721790', '721800', '741800', '741820', '741830', '741840', '741860', '751861', '761840', '761860', '761870', '761880', '761890', '761900', '761920', '781900', '781920', '781940', '781950', '781960', '781980', '801980', '801990', '802000', '802010', '802020', '822050', '822060', '822070', '832101']

# This is the list of atomic number which have isotopes used in NAX
NAX_z_list = [3, 5, 17, 22, 24, 26, 28, 34, 38, 40, 42, 44, 46, 47, 48, 49, 50, 51, 52, 55, 56, 57, 58, 60, 62, 63, 64, 66, 68, 72, 74, 76, 78, 80, 82]

# This list has been obtained from ENDFVIII libraries and by only keeping the nuclides that belong to the network tree
reduced_nucl_set= ['10010', '10020', '10030', '20030', '20040', '30060', '30070', '40070', '40090', '40100', '50100', '50110', '60120', '60130', '60140', '70140', '70150', '80160', '80170', '80180', '90190', '100200', '100210', '100220', '110220', '110230', '120240', '120250', '120260', '130261', '130270', '140280', '140290', '140300', '140310', '140320', '150310', '150320', '160320', '160330', '160340', '160350', '160360', '170350', '170360', '170370', '180360', '180370', '180380', '180390', '180400', '180410', '190390', '190400', '190410', '200400', '200410', '200420', '200430', '200440', '200450', '200460', '200470', '200480', '210450', '210451', '210470', '210480', '220460', '220470', '220480', '220490', '220500', '220660', '230490', '230500', '230510', '230660', '230670', '230680', '230690', '240500', '240510', '240520', '240530', '240540', '240660', '240670', '240680', '240690', '240710', '250540', '250550', '250660', '250670', '250680', '250690', '250700', '250710', '250720', '250730', '250740', '260540', '260550', '260560', '260570', '260580', '260660', '260670', '260680', '260690', '260700', '260710', '260720', '260730', '260740', '260750', '260770', '270580', '270581', '270590', '270660', '270670', '270680', '270690', '270700', '270710', '270720', '270730', '270740', '270750', '270760', '270770', '270780', '270790', '280580', '280590', '280600', '280610', '280620', '280630', '280640', '280660', '280670', '280680', '280690', '280700', '280710', '280720', '280730', '280740', '280750', '280760', '280770', '280780', '280790', '280800', '280810', '290630', '290640', '290650', '290660', '290670', '290680', '290681', '290690', '290700', '290701', '290710', '290720', '290730', '290740', '290750', '290760', '290770', '290780', '290790', '290800', '290810', '290820', '290830', '290840', '300640', '300650', '300660', '300670', '300680', '300690', '300691', '300700', '300710', '300711', '300720', '300730', '300740', '300750', '300760', '300770', '300780', '300790', '300800', '300810', '300820', '300830', '300840', '300850', '300860', '300870', '310660', '310670', '310680', '310690', '310700', '310710', '310720', '310721', '310730', '310740', '310741', '310750', '310760', '310770', '310780', '310790', '310800', '310810', '310820', '310830', '310840', '310850', '310860', '310870', '310880', '310890', '320680', '320690', '320700', '320710', '320711', '320720', '320730', '320731', '320740', '320750', '320751', '320760', '320770', '320771', '320780', '320790', '320791', '320800', '320810', '320811', '320820', '320830', '320840', '320850', '320860', '320870', '320880', '320890', '320900', '320910', '320920', '330710', '330720', '330730', '330740', '330741', '330750', '330760', '330770', '330780', '330790', '330800', '330810', '330820', '330821', '330830', '330840', '330841', '330850', '330860', '330870', '330880', '330890', '330900', '330910', '330920', '330930', '330940', '340730', '340731', '340740', '340750', '340760', '340770', '340771', '340780', '340790', '340791', '340800', '340810', '340811', '340820', '340830', '340831', '340840', '340850', '340851', '340860', '340870', '340880', '340890', '340900', '340910', '340920', '340930', '340940', '340950', '340960', '340970', '350750', '350770', '350771', '350780', '350790', '350791', '350800', '350801', '350810', '350820', '350821', '350830', '350840', '350841', '350850', '350860', '350861', '350870', '350880', '350890', '350900', '350910', '350920', '350930', '350940', '350950', '350960', '350970', '350980', '350990', '351000', '360770', '360780', '360790', '360791', '360800', '360810', '360811', '360820', '360830', '360831', '360840', '360850', '360851', '360860', '360870', '360880', '360890', '360900', '360910', '360920', '360930', '360940', '360950', '360960', '360970', '360980', '360990', '361000', '361010', '361020', '370790', '370810', '370830', '370840', '370850', '370860', '370861', '370870', '370880', '370890', '370900', '370901', '370910', '370920', '370930', '370940', '370950', '370960', '370970', '370980', '370990', '371000', '371010', '371020', '371030', '371040', '371050', '371060', '380830', '380840', '380850', '380851', '380860', '380870', '380871', '380880', '380890', '380900', '380910', '380920', '380930', '380940', '380950', '380960', '380970', '380980', '380990', '381000', '381010', '381020', '381030', '381040', '381050', '381060', '381070', '381080', '381090', '390850', '390870', '390871', '390880', '390890', '390891', '390900', '390901', '390910', '390911', '390920', '390930', '390931', '390940', '390950', '390960', '390961', '390970', '390971', '390980', '390981', '390990', '391000', '391010', '391020', '391030', '391040', '391050', '391060', '391070', '391080', '391090', '391100', '391110', '400870', '400880', '400890', '400891', '400900', '400901', '400910', '400920', '400930', '400940', '400950', '400960', '400970', '400980', '400990', '401000', '401010', '401020', '401030', '401040', '401050', '401060', '401070', '401080', '401090', '401100', '401110', '401120', '401130', '401140', '410890', '410900', '410910', '410911', '410920', '410930', '410931', '410940', '410941', '410950', '410951', '410960', '410970', '410971', '410980', '410981', '410990', '410991', '411000', '411001', '411010', '411020', '411021', '411030', '411040', '411041', '411050', '411060', '411070', '411080', '411090', '411100', '411110', '411120', '411130', '411140', '411150', '411160', '420910', '420920', '420930', '420931', '420940', '420950', '420960', '420970', '420980', '420990', '421000', '421010', '421020', '421030', '421040', '421050', '421060', '421070', '421080', '421090', '421100', '421110', '421120', '421130', '421140', '421150', '421160', '421170', '421180', '430950', '430951', '430970', '430971', '430980', '430990', '430991', '431000', '431010', '431020', '431021', '431030', '431040', '431050', '431060', '431070', '431080', '431090', '431100', '431110', '431120', '431130', '431140', '431150', '431160', '431170', '431180', '431190', '431200', '431210', '440960', '440970', '440980', '440990', '441000', '441010', '441020', '441030', '441040', '441050', '441060', '441070', '441080', '441090', '441091', '441100', '441110', '441120', '441130', '441140', '441150', '441160', '441170', '441180', '441190', '441200', '441210', '441220', '441230', '450990', '451010', '451011', '451020', '451021', '451030', '451031', '451040', '451041', '451050', '451051', '451060', '451061', '451070', '451080', '451081', '451090', '451091', '451100', '451101', '451110', '451120', '451130', '451140', '451150', '451160', '451170', '451180', '451190', '451200', '451210', '451220', '451230', '451240', '451250', '461010', '461020', '461030', '461040', '461050', '461060', '461070', '461071', '461080', '461090', '461091', '461100', '461110', '461111', '461120', '461130', '461140', '461150', '461160', '461170', '461180', '461190', '461200', '461210', '461220', '461230', '461240', '461250', '461260', '461270', '461280', '461290', '461300', '461310', '471050', '471051', '471060', '471061', '471070', '471071', '471080', '471081', '471090', '471091', '471100', '471101', '471110', '471111', '471120', '471130', '471131', '471140', '471150', '471151', '471160', '471161', '471170', '471171', '471180', '471181', '471190', '471200', '471201', '471210', '471220', '471221', '471230', '471240', '471250', '471260', '471270', '471280', '471290', '471300', '471310', '471320', '471330', '481060', '481070', '481080', '481090', '481100', '481110', '481111', '481120', '481130', '481131', '481140', '481150', '481151', '481160', '481170', '481171', '481180', '481190', '481191', '481200', '481210', '481211', '481220', '481230', '481240', '481250', '481260', '481270', '481280', '481290', '481300', '481310', '481320', '481330', '481340', '481350', '481360', '491090', '491110', '491120', '491121', '491130', '491131', '491140', '491141', '491150', '491151', '491160', '491161', '491170', '491171', '491180', '491181', '491190', '491191', '491200', '491201', '491210', '491211', '491220', '491221', '491230', '491231', '491240', '491241', '491250', '491251', '491260', '491261', '491270', '491271', '491280', '491281', '491290', '491291', '491300', '491301', '491310', '491311', '491320', '491330', '491340', '491350', '491360', '491370', '491380', '501110', '501120', '501130', '501131', '501140', '501150', '501160', '501170', '501171', '501180', '501190', '501191', '501200', '501210', '501211', '501220', '501230', '501231', '501240', '501250', '501251', '501260', '501270', '501271', '501280', '501281', '501290', '501291', '501300', '501301', '501310', '501311', '501320', '501330', '501340', '501350', '501360', '501370', '501380', '501390', '501400', '501410', '511150', '511170', '511180', '511181', '511190', '511200', '511201', '511210', '511220', '511221', '511230', '511240', '511241', '511250', '511260', '511261', '511270', '511280', '511281', '511290', '511291', '511300', '511301', '511310', '511320', '511321', '511330', '511340', '511341', '511350', '511360', '511370', '511380', '511390', '511400', '511410', '511420', '511430', '521180', '521190', '521200', '521210', '521211', '521220', '521230', '521231', '521240', '521250', '521251', '521260', '521270', '521271', '521280', '521290', '521291', '521300', '521310', '521311', '521320', '521330', '521331', '521340', '521350', '521360', '521370', '521380', '521390', '521400', '521410', '521420', '521430', '521440', '521450', '521460', '531210', '531230', '531250', '531260', '531270', '531280', '531290', '531300', '531301', '531310', '531320', '531321', '531330', '531331', '531340', '531341', '531350', '531360', '531361', '531370', '531380', '531390', '531400', '531410', '531420', '531430', '531440', '531450', '531460', '531470', '531480', '541230', '541240', '541250', '541251', '541260', '541270', '541271', '541280', '541290', '541291', '541300', '541310', '541311', '541320', '541330', '541331', '541340', '541341', '541350', '541351', '541360', '541370', '541380', '541390', '541400', '541410', '541420', '541430', '541431', '541440', '541450', '541460', '541470', '541480', '541490', '541500', '541510', '551270', '551290', '551310', '551320', '551330', '551340', '551341', '551350', '551351', '551360', '551361', '551370', '551380', '551381', '551390', '551400', '551410', '551420', '551430', '551440', '551450', '551460', '551470', '551480', '551490', '551500', '551510', '551520', '551530', '551540', '561300', '561310', '561320', '561330', '561340', '561350', '561351', '561360', '561361', '561370', '561371', '561380', '561390', '561400', '561410', '561420', '561430', '561440', '561450', '561460', '561470', '561480', '561490', '561500', '561510', '561520', '561530', '561540', '561550', '561560', '571330', '571350', '571370', '571380', '571390', '571400', '571410', '571420', '571430', '571440', '571450', '571460', '571461', '571470', '571480', '571490', '571500', '571510', '571520', '571530', '571540', '571550', '571560', '571570', '571580', '571590', '581350', '581360', '581370', '581371', '581380', '581390', '581391', '581400', '581410', '581420', '581430', '581440', '581450', '581460', '581470', '581480', '581490', '581500', '581510', '581520', '581530', '581540', '581550', '581560', '581570', '581580', '581590', '581600', '581610', '591390', '591400', '591410', '591420', '591421', '591430', '591440', '591441', '591450', '591460', '591470', '591480', '591481', '591490', '591500', '591510', '591520', '591530', '591540', '591550', '591560', '591570', '591580', '591590', '591600', '591610', '591620', '591630', '591640', '601400', '601410', '601420', '601430', '601440', '601450', '601460', '601470', '601480', '601490', '601500', '601510', '601520', '601530', '601540', '601550', '601560', '601570', '601580', '601590', '601600', '601610', '601620', '601630', '601640', '601650', '601660', '601670', '611430', '611440', '611450', '611460', '611470', '611480', '611481', '611490', '611500', '611510', '611520', '611521', '611530', '611540', '611541', '611550', '611560', '611570', '611580', '611590', '611600', '611610', '611620', '611630', '611640', '611650', '611660', '611670', '611680', '611690', '621440', '621450', '621460', '621470', '621480', '621490', '621500', '621510', '621520', '621530', '621540', '621550', '621560', '621570', '621580', '621590', '621600', '621610', '621620', '621630', '621640', '621650', '621660', '621670', '621680', '621690', '621700', '621710', '621720', '631470', '631490', '631510', '631520', '631521', '631530', '631540', '631541', '631550', '631560', '631570', '631580', '631590', '631600', '631610', '631620', '631630', '631640', '631650', '631660', '631670', '631680', '631690', '631700', '631710', '631720', '641490', '641500', '641510', '641520', '641530', '641540', '641550', '641560', '641570', '641580', '641590', '641600', '641610', '641620', '641630', '641640', '641650', '641660', '641670', '641680', '641690', '641700', '641710', '641720', '651530', '651550', '651560', '651561', '651570', '651580', '651581', '651590', '651600', '651610', '651620', '651621', '651630', '651640', '651650', '651660', '651670', '651680', '651690', '651700', '651710', '651720', '661540', '661550', '661560', '661570', '661580', '661590', '661600', '661610', '661620', '661630', '661640', '661650', '661651', '661660', '661670', '661680', '661690', '661700', '661710', '661720', '671590', '671591', '671610', '671611', '671620', '671621', '671630', '671631', '671640', '671641', '671650', '671660', '671661', '671670', '671680', '671690', '671700', '671701', '671710', '671720', '681610', '681620', '681630', '681640', '681650', '681660', '681670', '681671', '681680', '681690', '681700', '681710', '681720', '691650', '691660', '691670', '691680', '691690', '691700', '691710', '691720', '701670', '701680', '701690', '701691', '701700', '701710', '701720', '701730', '701740', '701750', '701760', '711710', '711711', '711720', '711721', '711750', '711760', '721740', '721750', '721760', '721770', '721780', '721790', '721800', '721810', '721820', '731800', '731810', '731820', '741800', '741810', '741820', '741830', '741840', '741850', '741860', '751850', '751860', '751861', '751870', '761840', '761850', '761860', '761870', '761880', '761890', '761900', '761910', '761920', '771910', '771911', '771920', '771930', '771940', '771941', '781900', '781910', '781920', '781930', '781940', '781950', '781960', '781970', '781980', '791970', '791971', '801960', '801970', '801971', '801980', '801990', '802000', '802010', '802020', '802030', '802040', '802060', '812030', '812040', '812050', '812060', '812070', '812080', '812090', '812100', '822040', '822050', '822060', '822070', '822080', '822090', '822100', '822110', '822120', '822140', '832080', '832090', '832100', '832101', '832110', '832120', '832130', '832140', '832150', '842080', '842090', '842100', '842110', '842120', '842130', '842140', '842150', '842160', '842180', '852150', '852170', '852180', '852190', '862170', '862180', '862190', '862200', '862220', '872210', '872220', '872230', '882220', '882230', '882240', '882250', '882260', '882280', '892250', '892260', '892270', '892280', '902260', '902270', '902280', '902290', '902300', '902310', '902320', '902330', '902340', '912290', '912300', '912310', '912320', '912330', '912340', '912341', '922300', '922310', '922320', '922330', '922340', '922350', '922351', '922360', '922370', '922380', '922390', '922400', '922410', '932340', '932350', '932360', '932361', '932370', '932380', '932390', '932400', '932401', '932410', '942360', '942370', '942380', '942390', '942400', '942410', '942420', '942430', '942440', '942450', '942460', '952400', '952410', '952420', '952421', '952430', '952440', '952441', '952450', '952461', '962400', '962410', '962420', '962430', '962440', '962450', '962460', '962470', '962480', '962490', '962500', '972450', '972460', '972470', '972480', '972490', '972500', '972510', '982460', '982470', '982480', '982490', '982500', '982510', '982520', '982530', '982540', '992510', '992520', '992530', '992540', '992541', '992550', '1002540', '1002550']

# Main plutonium isotopes
Pu_isotopes_name  = ['Pu-238', 'Pu-239', 'Pu-240', 'Pu-241', 'Pu-242', 'Pu-243']
Pu_isotopes_zamid = ['94238', '94239', '94240', '94241', '94242', '94243']

# Avogadro number
NA = 6.02214076E+23