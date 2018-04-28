from django.http import HttpResponse
from import_export import resources
from .models import Test, MathScoreConversion

def export(request, resource):
    resource = resource
    dataset = resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s.csv"' % (str(resource.Meta.model))
    return response

class MathScoreConversionResource(resources.ModelResource):
    class Meta:
        model = MathScoreConversion
