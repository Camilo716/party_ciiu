# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from . import party;

__all__ = ['register']


def register():
    Pool.register(
        module='party_ciiu', type_='model')
    Pool.register(
        module='party_ciiu', type_='wizard')
    Pool.register(
        module='party_ciiu', type_='report')
    Pool.register(
        party.Party,
        module='party_ciiu', type_='model')
