from django.http import HttpResponse

from demo_tasks import tasks


def demo_view(request):
    tasks.demo_task.delay()
    return HttpResponse('Task created!')
