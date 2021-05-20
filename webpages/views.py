from django.shortcuts import render, get_object_or_404
from .models import CareerForm, Contact, Career, Hero, Team, OfficialSocialHandles, Testimonal
from . forms import CaForm
from django.urls import reverse_lazy
# Create your views here.
# Create your views here.


def index(request):
    test = Testimonal.objects.all()
    offs = OfficialSocialHandles.objects.all()
    teams = Team.objects.all()
    carousel = Hero.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if Contact.objects.filter(email=email):
            return render(request, 'webpages/error.html', {'name': name, 'email': email})

        else:

            contact = Contact(name=name,  email=email,
                              subject=subject, message=message)
            contact.save()
            return render(request, 'webpages/info.html', {'name': name})
    context = {
        'test': test,
        'offs': offs,
        'carousel': carousel,
        'teams': teams,
    }
    return render(request, 'webpages/index.html', context)


def career(request):
    careers = Career.objects.all()
    context = {'careers': careers}
    return render(request, 'webpages/index.html', context)


def careerDetail(request, career_detail=None):
    career = get_object_or_404(Career, slug=career_detail)
    # career = get_object_or_404(Career, pk=id)
    context = {
        'career': career
    }
    return render(request, 'webpages/career.html', context)


def careerForm(request, career_detail=None):
    career = get_object_or_404(Career, slug=career_detail)
    if request.method == "POST":
        first_Name = request.POST['first_Name']
        last_Name = request.POST['last_Name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        city = request.POST['city']
        state = request.POST['state']
        employment_Type = request.POST['employment_Type']
        position = request.POST['position']
        address = request.POST['address']
        about = request.POST['about']
        qualify = request.POST['qualify']
        pin_code = request.POST['pin_code']
        if CareerForm.objects.filter(email=email):
            return render(request, 'webpages/error.html', {'first_Name': first_Name, 'email': email})

        form = CareerForm(first_Name=first_Name, last_Name=last_Name, email=email, phone_number=phone_number, city=city, state=state,
                          employment_Type=employment_Type, position=position, address=address, about=about, qualify=qualify, pin_code=pin_code)
        form.save()
        return render(request, 'webpages/info.html', {'first_Name': first_Name})

        # form = CaForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     reverse_lazy('careerForm')
    else:
        form = CaForm()
    context = {
        'career': career,
        'form': form,
    }
    return render(request, 'webpages/forms.html', context)
