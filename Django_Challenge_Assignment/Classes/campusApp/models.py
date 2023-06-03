from django.db import models


# Create your models here.
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(null=False, blank=True, default=None)

    #Creates the model manager
    object = models.Manager()

    #Display the output values as a string to make them more readable in the menu
    def __str__(self):
        display_campus = '{0.campus_name}, {0.state}'
        return display_campus.format(self)

    #Sets the name that is visable in the admin console
    class Meta:
        verbose_name_plural = "University Campus"
