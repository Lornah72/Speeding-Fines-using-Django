from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.http import HttpResponse
from .models import Drivers, Officer
from django.core.mail import send_mail
def login_officer(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,('Error'))
            return redirect('login_officer')
    else:
        return render (request,'login.html')

def get_drivers_by_license_plate(license_plate):
    drivers = Drivers.objects.filter(license_plate=license_plate)
    return drivers

def home(request):
    if request.method == 'POST':
        license_plate = request.POST.get('license_plate')
        drivers = get_drivers_by_license_plate(license_plate)
        if drivers.exists():
            message = f"Drivers found for license plate {license_plate}:"
            driver_names = [f"{driver.First_name} {driver.Last_name}" for driver in drivers]
            speeding_fine = 0
            speed = int(request.POST.get('speed', 0))
            if speed > 100:
                speeding_fine = (speed - 100) * 30
                speeding_message = f"Speeding fine: ${speeding_fine}"
                if speeding_fine > 0:
                    driver_emails = [driver.email for driver in drivers]
                    subject = "Overspeeding fine"
                    message1 = f"Dear driver,\n\nYou have been caught overspeeding. Your fine is ${speeding_fine}.\n\nSincerely,\nThe Traffic Department"
                    from_email = "lornahsanga72@gmail.com"
                    send_mail(
                    subject,
                    message1,
                    from_email,
                    driver_emails)
            else:
                speeding_message = ""
            context = {
                'message': message,
                'driver_names': driver_names,
                'speeding': speeding_message,
            }
            return render(request, 'home.html', context)
        else:
            message = f"No drivers found for license plate {license_plate}."
            context = {'message': message}
            return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')
