from django.shortcuts import render
from .models import NewsLetterUser, NewsLetter
from .forms import NewsLetterUserSignUpForm, NewsLetterCreationForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings


def newsletter_signup(request):
    form = NewsLetterUserSignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, "Email Already Exists", "alert alert-warning alert-dismissible")
        else:
            instance.save()
            messages.success(
                request,
                "Your Email has been successfully submitted",
                "alert alert-success alert-dismissible"
            )
            subject = "Thanks you for joining our NewsLetter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/templates/signup_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject, signup_message, from_email, to_email)
            html_template = get_template('signup_email.html').render()
            message.attach_alternative(html_template, "text/html")
            message.send()
    context = {
        "form": form,
    }
    return render(request, 'newsletter_signup.html', context)


def newsletter_unsubscribe(request):
    form = NewsLetterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            NewsLetterUser.objects.filter(email=instance.email).delete()
            messages.success(request,
                             "Your Email has been successfully Removed from our Database",
                             "alert alert-warning alert-dismissible")
            subject = "You have been Unsubscribed"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            signup_message = "******** Sorry to go see you later *********\n" \
                             "If you have any issue you can contact via my blog please visit this link:" \
                             " http://127.0.0.1:8000/contact"
            send_mail(subject, signup_message, from_email, to_email, fail_silently=True)
        else:

            messages.warning(
                request,
                "Sorry but we didn't find your email address",
                "alert alert-success alert-dismissible"
            )

    context = {
        "form": form,
    }

    return render(request, 'newsletter_unsubscribe.html', context)


def control_newsletter(request):
    form = NewsLetterCreationForm(request.POST or None)
    if form.is_valid():
        #form.save(commit=False)
        instance = form.save()
        newsletter = NewsLetter.objects.get(id=instance.id)
        if newsletter.status == 'Published':
            subject = newsletter.subject
            body = newsletter.content
            from_email = settings.EMAIL_HOST_USER
            for email in newsletter.email.all():
                send_mail(subject=subject, from_email=from_email, recipient_list=[email], message=body, fail_silently=True)
                print(email, "Succesfully sent into this mail")
    context = {
        "form": form,
        "newsletter": NewsLetterUser.objects.all(),
        "newsletters2": NewsLetter.objects.all(),
    }
    return render(request, 'control_newsletter.html', context)
