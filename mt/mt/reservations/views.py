# reservations/views.py
from django.shortcuts import render
from .models import Reservation

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

def reservation_detail(request, id):
    reservation = Reservation.objects.get(id=id)
    return render(request, 'reservations/reservation_detail.html', {'reservation': reservation})

# reservations/views.py
from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm
from django.utils import timezone
from django.db.models import Q

def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data['customer']
            date = form.cleaned_data['date']
            table = form.cleaned_data['table']

            # Проверка на наличие брони для пользователя на тот же день
            if Reservation.objects.filter(customer=customer, date=date).exists():
                form.add_error(None, "User already has a reservation on this date")
                return render(request, 'reservations/reservation_form.html', {'form': form})
            
            # Проверка на доступность стола
            if not table.is_available:
                form.add_error(None, "Table is not available")
                return render(request, 'reservations/reservation_form.html', {'form': form})

            # Сохраняем бронь
            form.save()
            return redirect('reservation_list')  # Перенаправляем на список броней
    else:
        form = ReservationForm()
    return render(request, 'reservations/reservation_form.html', {'form': form})

# reservations/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import ReservationForm

def update_reservation_status(request, id):
    reservation = get_object_or_404(Reservation, id=id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['pending', 'confirmed', 'canceled']:
            reservation.status = new_status
            reservation.save()
            return redirect('reservation_list')  # Перенаправляем на список броней

    return render(request, 'reservations/reservation_status_update.html', {'reservation': reservation})


# reservations/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation

def delete_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    reservation.delete()  # Удаляем бронь
    return redirect('reservation_list')  # Перенаправляем на список броней




