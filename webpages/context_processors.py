from .models import Career

# We write context processor coz it will be accessible in all template and it returns a dictionary


def career(request):
    careers = Career.objects.all()
    return {
        "careers": careers
    }
