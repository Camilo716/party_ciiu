from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.pool import Pool
from trytond.model.exceptions import ValidationError

class PartyCiiu_ciiu_code_TestCase(ModuleTestCase):
    "Test Party Ciiu campo ciiu_code"
    module = 'party_ciiu'

    @with_transaction()
    def test_para_entrada_invalida_UserError(self):
        pool = Pool()
        Party = pool.get('party.party')

        party, = Party.create([{'name': 'CIIU'}])

        with self.assertRaises(ValidationError):
            party.ciiu_code = '99999'
            party.save()
        
        with self.assertRaises(ValidationError):
            party.ciiu_code = '0'
            party.save()

        with self.assertRaises(ValidationError):
            party.ciiu_code = '9999'
            party.save()

del ModuleTestCase