from django.contrib.staticfiles.templatetags.staticfiles import static
from django.template.backends.utils import csrf_input_lazy


def defaults(request):
    context = {}

    context['csrf_input'] = csrf_input_lazy(request)
    context['static'] = static

    return context
