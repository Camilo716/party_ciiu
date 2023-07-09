===================
Party Ciiu Scenario
===================

Imports::

    >>> from proteus import Model, Wizard
    >>> from trytond.tests.tools import activate_modules

Activate modules::

    >>> config = activate_modules('party_ciiu')

    >>> Party = Model.get('party.party')
    >>> party = Party()
    >>> party.ciiu_code = '0111' # valor real esperados
    >>> party.save()
    >>> party.ciiu_code
    '0111'
