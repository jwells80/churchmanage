from django.db import models


US_STATE_CHOICES = (
 	    ('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'),
 	    ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'),
 	    ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'),
 	    ('DC', 'District Of Columbia'), ('FM', 'Federated States of Micronesia'),
        ('FL', 'Flordia'),  ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'),
        ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
        ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'),
 	    ('ME', 'Maine'), ('MH', 'Marshall Islands'), ('MD', 'Maryland'),
        ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'),
        ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'),
 	    ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'),
 	    ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'),
        ('NC', 'North Carolina'), ('ND', 'North Dakota'),
 	    ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'),
 	    ('OR', 'Oregon'), ('PW', 'Palau'), ('PA', 'Pennsylvania'),
        ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
 	    ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'),
 	    ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'),
 	    ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'),
 	    ('WI', 'Wisconsin'), ('WY', 'Wyoming'),
        )

class member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    spouse = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=2, choices=US_STATE_CHOICES)
    zip = models.IntegerField()

    def __str__(self):
        ret = self.last_name + ', ' + self.first_name
        return ret


class child(models.Model):
    member_id = models.ForeignKey(member, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name