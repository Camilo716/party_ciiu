from trytond.pool import PoolMeta
from trytond.model import fields


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'

    ciiu_code = fields.Char('CIIU CODE', required=False)