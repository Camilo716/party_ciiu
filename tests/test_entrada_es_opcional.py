from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.pool import Pool
from trytond.model.exceptions import RequiredValidationError

class PartyCiiu_EntradasRequeridas_TestCase(ModuleTestCase):
    "Test Party Ciiu module"
    module = 'party_ciiu'

    @with_transaction()
    def test_ciiud_code_es_opcional(self):
        pool = Pool()
        Party = pool.get('party.party')
        try:
            party, = Party.create([{}])
        except RequiredValidationError:
            self.fail('se espera campo `ciiu_code` como opcional')

del ModuleTestCase