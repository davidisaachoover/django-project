from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpRequest
from django.shortcuts import get_object_or_404, render
import time
from datetime import date
import datetime
import calendar
from growlerdeals.models import Brewery, site_header_set, User_added_deal, Displayed_prices, Graveyard_submissions, user_added_brewery
from .forms import NameForm, AddDeal, ContactForm, AddBrewery, SomethingWrong
from django.core.mail import send_mail

def addBrewery(request):
    if request.method == 'POST':
        form = AddBrewery({
            'brewery_name': request.POST['brewery'],
            'website': request.POST['website'],
            'address_line1': request.POST['address'],
            'city': request.POST['city'],
            'state': request.POST['state'],
            'zip_code': request.POST['zip_code'],
        })
        return_url = request.META['HTTP_REFERER']
        if form.is_valid():
            client_ip = request.META['HTTP_X_FORWARDED_FOR'] # another option for client ip http://stackoverflow.com/questions/27120895/how-to-get-user-public-ip-in-django
            my_model = user_added_brewery()
            my_model.brewery_name = form.cleaned_data['brewery_name']
            my_model.website = form.cleaned_data['website']
            my_model.address_line1 = form.cleaned_data['address_line1']
            my_model.city = form.cleaned_data['city']
            my_model.state = form.cleaned_data['state']
            my_model.zip_code = form.cleaned_data['zip_code']
            my_model.submitted_ip = client_ip
            my_model.save()
            message = "Thanks a bunch, we'll take a look at the submission and should have it available soon."
            return render(request, 'thanks.html', {'message' : message, 'return_url' : return_url})
        else: 
            return HttpResponseRedirect(return_url)
    else: 
        raise Http404
def somethingwrong(request):
    if request.method == 'POST':
        return_url = request.META['HTTP_REFERER']
        form = SomethingWrong(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            source = form.cleaned_data['source'] 
            brewery = request.POST['brewery']
            send_mail(
                'Something Wrong with %s' % brewery, 
                "email address: %s \n message: %s \n source: %s" % (email,  message, source), 
                'growlerdeals@gmail.com', 
                ['growlerdeals@gmail.com']
            )
            message="Thanks for the heads up, we'll check on it"
            return render(request, 'thanks.html', {'message' : message, 'return_url' : return_url})
        else: 
            return HttpResponseRedirect(return_url)
    else: 
        raise Http404


def index(request):
    today = date.today()
    current_day = date.weekday(today) #returns digit 0-6 (0 is Monday, 1 is Tuesday, etc...)
    returned_header_set=site_header_set.objects.get(header_set_name='default')
    header_line_1 = ""
    header_line_2 = ""
    if current_day == 0: 
        header_line_1 = getattr(returned_header_set, 'Monday_line_1')
        header_line_2 = getattr(returned_header_set, 'Monday_line_2')
    elif current_day == 1:
        header_line_1 = getattr(returned_header_set, 'Tuesday_line_1')
        header_line_2 = getattr(returned_header_set, 'Tuesday_line_2') 
    elif current_day == 2:
        header_line_1 = getattr(returned_header_set, 'Wednesday_line_1')
        header_line_2 = getattr(returned_header_set, 'Wednesday_line_2')
    elif current_day == 3:
        header_line_1 = getattr(returned_header_set, 'Thursday_line_1')
        header_line_2 = getattr(returned_header_set, 'Thursday_line_2')
    elif current_day == 4:
        header_line_1 = getattr(returned_header_set, 'Friday_line_1')
        header_line_2 = getattr(returned_header_set, 'Friday_line_2')
    elif current_day == 5:
        header_line_1 = getattr(returned_header_set, 'Saturday_line_1')
        header_line_2 = getattr(returned_header_set, 'Saturday_line_2')
    elif current_day == 6:
        header_line_1 = getattr(returned_header_set, 'Sunday_line_1')
        header_line_2 = getattr(returned_header_set, 'Sunday_line_2')     
    else: 
        header_line_1 = "There's great beer near you. Find it." 
    return render(request, 'index.html', {'header_line_1' : header_line_1, 'header_line_2' : header_line_2, 'current_day': current_day})

def donate(request):
    return render(request, 'donate.html')
def about(request):
    return render(request, 'about.html')
def forbreweries(request):
    return render(request, 'forbreweries.html')

def now(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def search(request):
    today = date.today()
    current_day = date.weekday(today) #returns digit 0-6
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    week_day = week_days[current_day]
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q: 
            error = True
        else: 
            breweries = Brewery.objects.filter(search_tags__icontains=q)
            results_count = breweries.count()
            known_price_breweries = []
            unknown_price_breweries = []
            closed_breweries = []

            for brewery in breweries:
                try:
                    price_object = Displayed_prices.objects.get(brewery=brewery)
                    today_price = getattr(price_object, week_day)#http://stackoverflow.com/questions/763558/django-object-get-set-field
                    if today_price == '0':
                        today_price = 'closed'
                        brewery.price_today=today_price
                        closed_breweries.append(brewery)
                    elif today_price == '?':
                        brewery.price_today='unknown'
                        unknown_price_breweries.append(brewery)
                    elif today_price > 0:
                        brewery.price_today=today_price
                        known_price_breweries.append(brewery)
                    else:
                        raise Http404
                except:
                    brewery.price_today='unknown'
                    unknown_price_breweries.append(brewery)
                
            known_price_breweries = sorted(known_price_breweries, key=lambda Brewery: Brewery.price_today) #sorts by price today ascending
            context_data = {
                'known_price_breweries' : known_price_breweries,
                'unknown_price_breweries' : unknown_price_breweries,
                'closed_breweries' : closed_breweries,
                'results_count' : results_count,
                'query' : q
            }
            return render(request, 'search_results.html', context_data)
    return render(request, 'index.html', {'error': error}) #this only renders "if not q"

def details(request, breweryID):
    try:
        breweryID = int(breweryID)
    except ValueError:
        return HttpResponseRedirect("")
    brewery = get_object_or_404(Brewery, pk=breweryID)
    prices = Displayed_prices.objects.filter(brewery=brewery)
    #prices.change_to_closed()
    form = AddDeal
    message = ""
    context_data = {'brewery': brewery, 'id': breweryID, 'prices' : prices, 'form' : form}
    if request.method == 'POST':
        form = AddDeal({
            'Sunday': request.POST['Sunday'],
            'Monday': request.POST['Monday'],
            'Tuesday': request.POST['Tuesday'],
            'Wednesday': request.POST['Wednesday'],
            'Thursday': request.POST['Thursday'],
            'Friday': request.POST['Friday'],
            'Saturday': request.POST['Saturday'],
        })
        if form.is_valid():
            now = datetime.datetime.now()
            client_ip = request.META['HTTP_X_FORWARDED_FOR'] # another option for client ip http://stackoverflow.com/questions/27120895/how-to-get-user-public-ip-in-django
            then = now - datetime.timedelta(minutes=4)#going to determine the quality of the submission
            number_of_ok_submissions_by_client = User_added_deal.objects.filter(submitted_ip=client_ip, TimeSubmitted__range=(then, now)).count()#pulls count of objects(or rows)
            number_of_graveyards_by_client = Graveyard_submissions.objects.filter(submitted_ip=client_ip, TimeSubmitted__range=(then, now)).count()#pulls number of bad submissions from client's IP
            total_submissions_by_client = number_of_ok_submissions_by_client + number_of_graveyards_by_client
            if number_of_ok_submissions_by_client < 7 and number_of_graveyards_by_client < 3 and total_submissions_by_client < 7:
                submitted_deals = User_added_deal.objects.filter(brewery=brewery) 
                total_num_of_submissions_by_all = submitted_deals.count()
                if total_num_of_submissions_by_all > 100: #if we already have up to 100 submissions for this brewery
                    return HttpResponseRedirect("") #if we already have 100 submissions for this brewery, we fake a submission
                else:
                # full example here http://stackoverflow.com/questions/11923317/creating-django-forms
                    my_model = User_added_deal()
                    my_model.brewery = brewery
                    my_model.Sunday = form.cleaned_data['Sunday']
                    my_model.Monday = form.cleaned_data['Monday']
                    my_model.Tuesday = form.cleaned_data['Tuesday']
                    my_model.Wednesday = form.cleaned_data['Wednesday']
                    my_model.Thursday = form.cleaned_data['Thursday']
                    my_model.Friday = form.cleaned_data['Friday']
                    my_model.Saturday = form.cleaned_data['Saturday']
                    my_model.submitted_ip = client_ip
                    my_model.save()
                    return HttpResponseRedirect("")


            #    submitted_deals = User_added_deal.objects.filter(brewery=brewery) 
             #   total_num_of_submissions_by_all = User_added_deal.objects.filter(brewery=brewery).count()
              #  total_num_of_submissions_by_all = submitted_deals.count()
               # if total_num_of_submissions_by_all < 100: #if have less than 100 submissions already 
                #    #this is where we save the fields
                 #   # full example here http://stackoverflow.com/questions/11923317/creating-django-forms
                  #  my_model.brewery = brewery
                   # my_model.Sunday = form.cleaned_data['Sunday']
                    #my_model.Monday = form.cleaned_data['Monday']
                    #my_model.Tuesday = form.cleaned_data['Tuesday']
                    #my_model.Wednesday = form.cleaned_data['Wednesday']
                    #my_model.Thursday = form.cleaned_data['Thursday']
                    #my_model.Friday = form.cleaned_data['Friday']
                    #my_model.Saturday = form.cleaned_data['Saturday']
                    #my_model.submitted_ip = client_ip
                    #my_model.save()
                    #return HttpResponseRedirect("")
                #else:
                #    return HttpResponseRedirect("") #if we already have 100 submissions for this brewery, we fake a submission
            else: #else if we've gotten too many or too many bad ones from this client's ip address 
                message = "You're doing that a bit more often than we're comfortable with, have a beer and come back in a bit"
                context_data = {'brewery': brewery, 'id': breweryID, 'prices' : prices, 'message': message}
                return render(request, 'details.html', context_data)
        else: # if form submission wasn't valid
            form = AddDeal()
            message = "Try again"
            context_data = {'brewery': brewery, 'id': breweryID, 'prices' : prices, 'message': message}
            return render(request, 'details.html', context_data)

    return render(request, 'details.html', context_data)








            #if request.method == 'POST':
                #form = AddDeal(request.POST)
                #if form.is_valid(): #process the data in form.cleaned_data as required
                    #values = request.META['REMOTE_ADDR']
                    #form = AddDeal()
                   # message = "Thanks"
                  #  return render(request, 'details.html', {'brewery': brewery, 'id': breweryID,'form': form, 'message': message})
                    #values = request.META.items()
                    #Sunday = form.cleaned_data['Sunday']
                ##     #form = AddDeal()
              #      #return HttpResponse(post.id, post.brewery)
             #   else:
            #        message = "Try again"
           #         form = AddDeal()
           #     return render(request, 'details.html', {'brewery': brewery, 'id': breweryID,'form': form, 'message': message})
           # else:
           #     form = AddDeal()
           # return render(request, 'details.html', {'brewery': brewery, 'id': breweryID, 'form': form})
 


def gmap(request):
    return render(request, 'gmap.html')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL: could change to http response
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def adddeal(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddDeal(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL: could change to http response
            return render(request, 'details.html', {'form': form,})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddDeal()

    return render(request, 'details.html', {'form': form})

def contact(request):
    """
        can send email from growlerdeals@gmail.com by using this format:
        from django.core.mail import send_mail
        send_mail('fuck yes.', 'I think i just got the email working, I just sent this from the command prompt', 'growlerdeals@gmail.com', ['kvnllnbrgr@gmail.com'])
        could use for autoresponse emails
    """   
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(
                'contact from %s' % email, 
                "Sender's name: %s: \n email address: %s \n subject: %s \n message: %s " % (name, email, subject, message), 
                'growlerdeals@gmail.com', 
                ['growlerdeals@gmail.com']
            )
            return_url = request.META['HTTP_REFERER']
            message="Thanks, we'll get back to you as soon as possible. Cheers"
            return render(request, 'thanks.html', {'message' : message, 'return_url' : return_url})
        else: 
            errors = []
            if not request.POST.get('subject', ''):
                errors.append('Enter a subject.')
            if not request.POST.get('message', ''):
                errors.append('Enter a message.')
            if request.POST.get('email') and '@' not in request.POST['email']:
                errors.append('Enter a valid e-mail address.')
            if not errors:
                response_message = "try again"
            return render(request, 'contact.html', {'response_message' : errors})
    else: 
        return render(request, 'contact.html')


def thanks(request):
    return render(request, 'thanks.html')






