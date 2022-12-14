from django.shortcuts import render
from .models import Player, Event
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from .forms import RegisterPlayerForm, EditPlayerForm
import datetime 
from django.db.models.expressions import RawSQL
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


def home(request):
    events = Event.objects.all()
    params = {'eventlist': events}
    return render(request, 'scheduler/home.html', params)

def event(request, pk): 
    dateformat = "%y/%m/%d"
    timeformat = "%H:%M"
    thisEvent=Event.objects.filter(id = pk).values()[0]
    event_name = thisEvent['event_name']
    event_date = datetime.datetime.strftime(thisEvent['event_date'], dateformat)
    event_start = datetime.time.strftime(thisEvent['event_start'], timeformat)
    event_end = datetime.time.strftime(thisEvent['event_end'], timeformat)
    event_comment = thisEvent['event_comment']
    event_status = thisEvent['event_status']

    params = {
        'event_count': Player.objects.filter(event=pk).filter(attendance_status = 'CO').count(),
        'event_name':event_name,
        'event_date':event_date,
        'event_start': event_start,
        'event_end': event_end,
        'event_comment':event_comment,
        'event_status':event_status,
        'players' : Player.objects.filter(event = pk).annotate(N=RawSQL('row_number() over ()', [])).values(),
        'form' : RegisterPlayerForm(initial={'event':pk}),
        }
    return render(request, 'scheduler/event.html', params)

def register(request):
    if request.method == 'POST':
        form = RegisterPlayerForm(request.POST)
        if form.is_valid():
            form.save()
        key = request.POST['event']
    else:
        print('something went wrong')
             
    return redirect(f'event/'+key+'/')

class EditPlayer(UpdateView):
    model = Player
    form_class = EditPlayerForm
    template_name = 'scheduler/edit_player_template.html'

    def get_success_url(self, **kwargs):
        event_key = self.request.POST['event']
        return ('/scheduler/event/'+event_key+'/')

class DeletePlayer(DeleteView):
    model = Player
    template_name = 'scheduler/confirmDelete.html'

    def get_success_url(self, **kwargs):
        event_key = self.request.POST['event']
        return ('/scheduler/event/'+event_key+'/')

    
    