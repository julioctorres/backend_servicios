from import_export import resources
from . import models as m
from facturas.models import Bill

class DatosResource(resources.ModelResource):
    class Meta:
        model = m.Client
        model_dos = Bill 
        fields = [
            'number_document',
            'first_name',
            'last_name',
            'id'
        ] 
        export_order = fields