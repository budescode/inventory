from django.contrib import admin
from .models import Poster, PropertyType, Price


admin.site.register(PropertyType)
admin.site.register(Price)




class PosterAdmin(admin.ModelAdmin):
	list_display = ['user','id_user', 'created', 'active']

admin.site.register(Poster, PosterAdmin)


# class DataInput(forms.Form):
#     file = forms.FileField()
#     place = forms.ModelChoiceField(queryset=Place.objects.all())

#     def save(self):
#         records = csv.reader(self.cleaned_data["file"])
#         for line in records:
#             input_data = Data()
#             input_data.place = self.cleaned_data["place"]
#             input_data.time = datetime.strptime(line[1], "%m/%d/%y %H:%M:%S")
#             input_data.data_1 = line[2]
#             input_data.data_2 = line[3]
#             input_data.data_3 = line[4]
#             input_data.save()