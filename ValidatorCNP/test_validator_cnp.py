import unittest
import Exercises.ValidatorCNP.validator_cnp as c


class TestValidatorCNP(unittest.TestCase):

    def test_valideaza_sex(self):
        self.assertEqual(c.valideaza_sexul('1841223385565'), '1')
        self.assertEqual(c.valideaza_sexul('9841223385565'), '9')
        self.assertEqual(c.valideaza_sexul('0841223385565'), None)

    def test_valideaza_an(self):
        self.assertEqual(c.valideaza_anul('1841223385565'), 1984)
        self.assertEqual(c.valideaza_anul('3f41223385565'), None)
        self.assertEqual(c.valideaza_anul('3841223385566'), 1884)
        self.assertEqual(c.valideaza_anul('6841223385566'), 2084)

    def test_valideaza_an_bisect(self):
        self.assertEqual(c.valideaza_an_bisect(1984), True)
        self.assertEqual(c.valideaza_an_bisect(1500), False)

    def test_valideaza_data(self):
        self.assertEqual(c.valideaza_data(1984, '02', '29'), True)
        self.assertEqual(c.valideaza_data(1983, '02', '29'), None)
        self.assertEqual(c.valideaza_data(1983, '02', '28'), True)
        self.assertEqual(c.valideaza_data(1984, '04', '31'), None)
        self.assertEqual(c.valideaza_data(1984, '05', '31'), True)
        self.assertEqual(c.valideaza_data(1984, '05', '32'), None)

    def test_valideaza_luna(self):
        self.assertEqual(c.valideaza_luna('1841223385565'), '12')
        self.assertEqual(c.valideaza_luna('1840023385565'), None)
        self.assertEqual(c.valideaza_luna('1841323385565'), None)

    def test_valideaza_zi(self):
        self.assertEqual(c.valideaza_ziua('1841223385565'), '23')
        self.assertEqual(c.valideaza_ziua('1841200385565'), None)
        self.assertEqual(c.valideaza_ziua('1841231385565'), '31')
        self.assertEqual(c.valideaza_ziua('1841232385565'), None)

    def test_valideaza_judet(self):
        self.assertEqual(c.valideaza_judet('1841223385565'), '38')
        self.assertEqual(c.valideaza_judet('1841223005565'), None)
        self.assertEqual(c.valideaza_judet('1841223465565'), '46')
        self.assertEqual(c.valideaza_judet('1841223475565'), None)
        self.assertEqual(c.valideaza_judet('1841223505565'), None)
        self.assertEqual(c.valideaza_judet('1841223535565'), None)

    def test_valideaza_birou(self):
        self.assertEqual(c.valideaza_birou_evidenta('1841223385565'), '556')
        self.assertEqual(c.valideaza_birou_evidenta('1841223380005'), None)

    def test_valideaza_cifra_control(self):
        self.assertEqual(c.valideaza_cifra_control('1841223385565'), 5)
        self.assertEqual(c.valideaza_cifra_control('1841223385566'), 5)
        self.assertEqual(c.valideaza_cifra_control('3841223385566'), 9)
        self.assertEqual(c.valideaza_cifra_control('6841223385566'), 4)

    def test_valideaza_cnp(self):
        self.assertEqual(c.valideaza_cnp('1841223385565'), '1841223385565')
        self.assertEqual(c.valideaza_cnp('1841223385566'), None)
        self.assertEqual(c.valideaza_cnp('1500229286662'), None)
        self.assertEqual(c.valideaza_cnp('184122338556654564'), None)
        self.assertEqual(c.valideaza_cnp(''), None)
        self.assertEqual(c.valideaza_cnp(' '), None)
        self.assertEqual(c.valideaza_cnp('adafdsafdsfdg'), None)
        self.assertEqual(c.valideaza_cnp('18f12h3385566'), None)


if __name__ == '__main__':
    unittest.main()