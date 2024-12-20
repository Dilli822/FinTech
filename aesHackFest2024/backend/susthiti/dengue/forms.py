from django import forms

class PredictionForm(forms.Form):
    ndvi_ne = forms.FloatField(label="NDVI NE")
    year = forms.IntegerField(label="Year")
    ndvi_nw = forms.FloatField(label="NDVI NW")
    ndvi_se = forms.FloatField(label="NDVI SE")
    ndvi_sw = forms.FloatField(label="NDVI SW")
    temperature = forms.FloatField(label="Temperature")
    humidity = forms.FloatField(label="Humidity")
    wind_speed = forms.FloatField(label="Wind Speed")
    pressure = forms.FloatField(label="Pressure")
    ndvi_diff = forms.FloatField(label="NDVI Difference")
    ndvi_sum = forms.FloatField(label="NDVI Sum")
    rain = forms.FloatField(label="Rain")
    solar_radiation = forms.FloatField(label="Solar Radiation")
    precipitation = forms.FloatField(label="Precipitation")
    latitude = forms.FloatField(label="Latitude")
    longitude = forms.FloatField(label="Longitude")
    altitude = forms.FloatField(label="Altitude")
    daylight = forms.FloatField(label="Daylight")
    mean_temperature = forms.FloatField(label="Mean Temperature")
    temperature_variation = forms.FloatField(label="Temperature Variation")
    humidity_variation = forms.FloatField(label="Humidity Variation")
