from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpRequest
from django.shortcuts import get_object_or_404, render
import time
from datetime import date
import datetime
import calendar
from growlerdeals.models import Brewery, site_header_set, User_added_deal, Displayed_prices, Graveyard_submissions, user_added_brewery
from .forms import NameForm, AddDeal, ContactForm, AddBrewery
from django.core.mail import send_mail
breweries = Brewery.objects.all()
for brewery in breweries:
	price_model = Displayed_prices()
	price_model.brewery = brewery
	price_model.Sunday = "?"
	price_model.Monday = "?"
	price_model.Tuesday = "?"
	price_model.Wednesday = "?"
	price_model.Thursday = "?"
	price_model.Friday = "?"
	price_model.Saturday = "?"
	price_model.save()