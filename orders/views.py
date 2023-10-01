from datetime import datetime, timedelta
from http import HTTPStatus
from tempfile import NamedTemporaryFile

from django.db.models import Count
from django.http import FileResponse
from django.views.decorators.http import require_http_methods

from orders.utils import make_excel_report
from robots.models import Robot


@require_http_methods(['GET'])
def week_report(request):
    queryset = Robot.objects.filter(
        created__gte=(datetime.now() - timedelta(days=7))
    ).values_list('model', 'version').distinct().annotate(count=Count('model'))
    robots_list = list(queryset)
    report = make_excel_report(robots_list)
    file = NamedTemporaryFile(prefix='week_report-', suffix='.xlsx')
    report.save(file.name)
    return FileResponse(
            open(file.name, 'rb'),
            as_attachment=True,
            filename=file.name,
            status=HTTPStatus.OK
        )
