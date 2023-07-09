from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.i18n import gettext
from trytond.model.exceptions import ValidationError

class Party(metaclass=PoolMeta):
    # Definición de la clase Party, que representa el modelo party.party en Tryton

    __name__ = 'party.party'
    # Establece el nombre del modelo como 'party.party'

    ciiu_code = fields.Char('CIIU CODE', required=False)
    # Define el campo ciiu_code como un campo de tipo Char (cadena de texto) con etiqueta 'CIIU CODE'.
    # Se establece required=False, lo que significa que el campo no es obligatorio.

    @classmethod
    def validate_fields(cls, records, field_names):
        # Método de clase que se llama automáticamente durante la validación de los campos del modelo.

        super().validate_fields(records, field_names)
        # Llama al método validate_fields de la clase base para realizar las validaciones estándar.

        cls.check_fields(records, field_names)
        # Llama al método check_fields definido en esta clase para realizar validaciones adicionales.

    @classmethod
    def check_fields(cls, records, field_names):
        # Método de clase que verifica los campos específicos del modelo.

        if field_names and not (field_names & {'ciiu_code'}):
            # Si se especificaron nombres de campo y 'ciiu_code' no está en esos nombres de campo, no es necesario realizar ninguna validación adicional.
            return

        for record in records:
            # Itera sobre los registros (instancias) pasados como argumento.

            if not cls.allowed_ciiu_code(record.ciiu_code):
                # Verifica si el código ciiu_code en el registro no es permitido según las reglas establecidas.

                raise ValidationError(gettext('party_ciiu.ciiu_code_invalid'))
                # Lanza una excepción de Validación con un mensaje de error que se obtiene mediante gettext.
                # El mensaje de error se traduce utilizando las reglas de internacionalización (i18n).

    @classmethod
    def allowed_ciiu_code(cls, code):
        # Método de clase que verifica si un código ciiu_code es permitido según las reglas establecidas.

        # solo validamos los codigos de interes para nuestra implementacion
        codes = [None, '0111', '0170', '0210', '0240', '0311', '0510', '0520', '0610'] 
        # Lista de códigos permitidos

        return code in codes
        # Verifica si el código dado está presente en la lista de códigos permitidos.
