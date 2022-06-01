from import_export import resources
from . import models as m

class DatosResource(resources.ModelResource):
    class Meta:
        model = m.Client
        fields = [
            'number_document',
            'first_name',
        ] 
        export_order = fields