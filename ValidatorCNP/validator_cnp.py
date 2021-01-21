def valideaza_sexul(cnp):
    sex = cnp[0]

    if int(sex) != 0:
        return sex


def valideaza_anul(cnp):
    an = cnp[1:3]

    if an.isnumeric() is False:
        return None
    elif cnp[0] in ['1', '2', '7', '8']:
        return int('19' + an)
    elif cnp[0] in ['3', '4']:
        return int('18' + an)
    elif cnp[0] in ['5', '6']:
        return int('20' + an)


def valideaza_an_bisect(an):
    if (an % 4) == 0:
        if (an % 100) == 0:
            if (an % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def valideaza_data(an, luna, zi):
    bisect = valideaza_an_bisect(an)

    if bisect is True:
        if (luna == '02' and int(zi) <= 29) is True or \
                (luna in ['01', '03', '05', '07', '08', '10', '12'] and int(zi) <= 31) is True or \
                (luna in ['04', '06', '09', '11'] and int(zi) <= 30) is True:
            return True
    elif bisect is False:
        if (luna == '02' and int(zi) <= 28) is True or \
                (luna in ['01', '03', '05', '07', '08', '10', '12'] and int(zi) <= 31) is True or \
                (luna in ['04', '06', '09', '11'] and int(zi) <= 30) is True:
            return True


def valideaza_luna(cnp):
    luna = cnp[3:5]

    if (int(luna[0]) == 0 and int(luna[1]) in range(1, 10)) or \
            (int(luna[0]) == 1 and int(luna[1]) in [0, 1, 2]):
        return luna


def valideaza_ziua(cnp):
    zi = cnp[5:7]

    if (int(zi[0]) == 0 and int(zi[1]) in range(1, 10)) or \
            (int(zi[0]) == 1 and int(zi[1]) in range(0, 10)) or \
            (int(zi[0]) == 2 and int(zi[1]) in range(0, 10)) or \
            (int(zi[0]) == 3 and int(zi[1]) in range(0, 2)):
        return zi


def valideaza_judet(cnp):
    judet = cnp[7:9]

    if (int(judet[0]) == 0 and int(judet[1]) in range(1, 10)) or \
            (int(judet[0]) == 0 and int(judet[1]) in range(1, 10)) or \
            (int(judet[0]) in range(1, 4) and int(judet[1]) in range(0, 10)) or \
            (int(judet[0]) == 4 and int(judet[1]) in range(1, 7)) or \
            (int(judet[0]) == 5 and int(judet[1]) in range(1, 3)):
        return judet


def valideaza_birou_evidenta(cnp):
    birou_evidenta = cnp[9:12]

    if (int(birou_evidenta[0]) == 0 and
        int(birou_evidenta[1]) in range(0, 10) and
        int(birou_evidenta[2]) in range(1, 10)) or \
            (int(birou_evidenta[0]) in range(1, 10) and
             int(birou_evidenta[1]) in range(0, 10) and
             int(birou_evidenta[2]) in range(0, 10)):
        return birou_evidenta


def valideaza_cifra_control(cnp):
    n = '279146358279'
    cifra = 0

    for i in range(len(n)):
        cifra += (int(n[i]) * int(cnp[i]))
    if (cifra / 11) == 10:
        return 1
    else:
        cifra = str(cifra % 11)
        return int(cifra[0])


def valideaza_cnp(cnp):
    if (cnp.isnumeric() is False) or len(cnp) != 13:
        return None

    s = valideaza_sexul(cnp)
    aa = valideaza_anul(cnp)
    ll = valideaza_luna(cnp)
    zz = valideaza_ziua(cnp)
    data = valideaza_data(aa, ll, zz)
    jj = valideaza_judet(cnp)
    nnn = valideaza_birou_evidenta(cnp)
    c = valideaza_cifra_control(cnp)

    if all(x is not None for x in [s, aa, ll, zz, jj, nnn, c]) and (c == int(cnp[-1])) is True and data is True:
        return cnp


if __name__ == '__main__':
    valid = None

    while valid is None:
        cnp = input('Intorduceti CNP-ul: ')
        valid = valideaza_cnp(cnp)
        if valid is None:
            print('CNP invalid: ' + cnp)
        else:
            print('CNP valid: ' + valid)