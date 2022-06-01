from . import models as m
from . import resources as r

def descargar_formato():
    resource = r.DatosResource()
    return resource.export(
        m.Client.objects.all()
    )