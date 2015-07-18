from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
#david's comment


closed_choices = (
    ('U', 'Unknown'),
    ('O', 'Open'),
    ('C', 'Closed'),
)
day_choices = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


# Create your models here.
class Brewery(models.Model):
    brewery_name = models.CharField(max_length=200)
    notes = models.CharField(max_length=250, default="", blank=True)
    address_line1 = models.CharField("Address line 1", max_length = 50, blank=True)
    city = models.CharField(max_length = 50, blank = True)
    state = models.CharField("State (abbreviation)", max_length = 2, blank = True)
    zip_code = models.CharField("Zip Code", max_length = 10, blank=True)
    price_today= models.CharField(blank=True, max_length=6)
    #full_address = models.CharField(max_length= 250, blank=True)
    #coordinates = models.CharField(max_length = 100, blank=True)
    website = models.CharField(max_length = 100, blank = True)
    search_tags = models.CharField(max_length = 250, blank = True)
    def __unicode__(self): #this names each object as the brewery name instead of the default "Brewery object"
        return self.brewery_name

class User_added_deal(models.Model):
    brewery = models.ForeignKey(Brewery)
    Sunday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null=True)
    Monday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null=True)
    Tuesday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null=True)
    Wednesday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null=True)
    Thursday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null=True)
    Friday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null=True)
    Saturday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null=True)
    TimeSubmitted = models.DateTimeField(auto_now_add=True)
    submitted_ip = models.GenericIPAddressField(null=True)
    def save_to_displayed(self):
        def mode(list): #returns list where list[0]= the most frequent number or numbers and list[1]=the number of occurences
            d = {}
            for elm in list:
                try:
                    d[elm] += 1
                except(KeyError):
                    d[elm] = 1
            keys = d.keys()
            max = d[keys[0]]
            for key in keys[1:]:
                if d[key] > max:
                    max = d[key]
            max_k = []      
            for key in keys:
                if d[key] == max:
                    max_k.append(key),
            return max_k,max
        #price = User_added_deal.objects.get(brewery=self.brewery)
        display = Displayed_prices.objects.get(brewery=self.brewery)
        other_deals = User_added_deal.objects.filter(brewery=self.brewery)
        if self.Sunday > 0: #if the submitted deal has a value for this day (THIS WILL HAVE TO BE RUN ON EVERY DAY OF THE WEEK)
            if display.Sunday > 0: #if the value in the Displayed prices object for the day is greater than 0
                #from other_deals, select all Sunday fields, put in list, get mode of list, and put in the Display prices
                day_prices_list = []#initialize empty list
                for deal_row in other_deals:
                    price = deal_row.Sunday
                    if deal > 0:
                        day_prices_list.append(price)
                #run mode algorithm on day_prices_list and store result in display.Sunday
                mode_price=mode(day_prices_list)[0][0]#this returns the most frequent number of the lowest value, we will probably change this later
                display.Sunday=mode_price
                 
            else:
                display.Sunday = self.Sunday

        if self.Monday > 0:
            if display.Monday > 0:
                display.Monday = self.Monday
        if self.Tuesday > 0:
            if display.Tuesday > 0:
                display.Tuesday = self.Tuesday
        if self.Wednesday > 0:
            if display.Wednesday > 0:
                display.Wednesday = self.Wednesday
        if self.Thursday > 0:
            if display.Thursday > 0:
                display.Thursday = self.Thursday
        if self.Friday > 0:
            if display.Friday > 0:
                display.Friday = self.Friday
        if self.Saturday > 0:
            if display.Saturday > 0:
                display.Saturday = self.Saturday
        display.save()



        


            
            
        display.save()
        display2 = Displayed_prices.objects.get(brewery=self.brewery)
        print display2.Sunday
        print display2.Monday
        print display2.Tuesday
        print display2.Wednesday 
        print display2.Thursday
        print display2.Friday 
        print display2.Saturday


class Displayed_prices(models.Model):
    brewery = models.OneToOneField(Brewery)
    Sunday = models.CharField(max_length=12, default="unknown")
    Monday = models.CharField(max_length=12, default="unknown")
    Tuesday = models.CharField(max_length=12, default="unknown")
    Wednesday = models.CharField(max_length=12, default="unknown")
    Thursday = models.CharField(max_length=12, default="unknown")
    Friday = models.CharField(max_length=12, default="unknown")
    Saturday = models.CharField(max_length=12, default="unknown")
    last_modified = models.DateTimeField(auto_now=True)
    brewery_confirmed = models.BooleanField(default=False)

class Graveyard_submissions(models.Model):
    brewery = models.ForeignKey(Brewery)
    Sunday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Monday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Tuesday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Wednesday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Thursday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Friday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Saturday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    TimeSubmitted = models.DateTimeField(auto_now_add=True)
    submitted_ip = models.GenericIPAddressField(null=True)

class user_added_brewery(models.Model):
    brewery_name =  models.CharField(max_length=200)
    website = models.CharField(max_length = 100, blank = True)
    address_line1 = models.CharField("Address line 1", max_length = 50, blank=True)
    city = models.CharField(max_length = 50, blank = True)
    state = models.CharField("State (abbreviation)", max_length = 2, blank = True)
    zip_code = models.CharField("Zip Code", max_length = 10, blank=True)
    time_submitted = models.DateTimeField(auto_now_add=True)
    submitted_ip = models.GenericIPAddressField(null=True)

class site_header_set(models.Model):
    header_set_name = models.CharField(max_length=25, default="default")
    Monday_line_1 = models.CharField(max_length=50, blank=True)
    Monday_line_2 = models.CharField(max_length=50, blank=True)
    Tuesday_line_1 = models.CharField(max_length=50, blank=True)
    Tuesday_line_2 = models.CharField(max_length=50, blank=True)
    Wednesday_line_1 = models.CharField(max_length=50, blank=True)
    Wednesday_line_2 = models.CharField(max_length=50, blank=True)
    Thursday_line_1 = models.CharField(max_length=50, blank=True)
    Thursday_line_2 = models.CharField(max_length=50, blank=True)
    Friday_line_1 = models.CharField(max_length=50, blank=True)
    Friday_line_2 = models.CharField(max_length=50, blank=True)
    Saturday_line_1 = models.CharField(max_length=50, blank=True)
    Saturday_line_2 = models.CharField(max_length=50, blank=True)
    Sunday_line_1 = models.CharField(max_length=50, blank=True)
    Sunday_line_2 = models.CharField(max_length=50, blank=True)
    def __unicode__(self): 
        return self.header_set_name
