from tkinter import *
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

def get_details():
    enter_number = entry.get()
    
    # Extract country code from the entered phone number
    number_info = phonenumbers.parse(enter_number, None)
    country_code = str(number_info.country_code)

    # Set default region for parsing
    default_region = phonenumbers.region_code_for_country_code(country_code)
    
    # Parse the phone number with the specified default region
    number = phonenumbers.parse(enter_number, default_region)
    
    locate = geocoder.description_for_number(number, "en")
    country.config(text=locate)
    operator = carrier.name_for_number(number, "en")
    sim.config(text=operator)
    time_zone = timezone.time_zones_for_number(number)
    zone.config(text=time_zone)

    geolocator = Nominatim(user_agent="phone")
    location = geolocator.geocode(locate)

    if location is not None:
        latitude_val = location.latitude
        longitude_val = location.longitude
        longitude_label.config(text=longitude_val)
        latitude_label.config(text=latitude_val)

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=longitude_val, lat=latitude_val)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        local_time = local_time.strftime("%H:%M:%S")
        clock.config(text=local_time)
    else:
        # Handle the case where the location is None
        longitude_label.config(text="Location not found")
        latitude_label.config(text="Location not found")
        clock.config(text="Time not available")

# Tk() is used to create a window
root = Tk()
# title() is used to give a title to the window
root.title("Phone Number Details")
# geometry() is used to set the width and height of the window
root.geometry("500x500")
# resizable() is used to set the fix size of the window
root.resizable(False, False)
# mainloop() is an infinite loop used to run the application when it's ready

# icon image
icon = PhotoImage(file="phone_icon.png")
# iconphoto() is used to set the icon of the window
root.iconphoto(False, icon)

# logo 
logo = PhotoImage(file="touch.png")
# label() is used to create a label
label = Label(root, image=logo).place(x=380, y=90)

# Ebackground = PhotoImage(file="search-bar.png")
# label = Label(root, image=Ebackground).place(x=100, y=220)

# heading
heading = Label(root, text="Phone Number Details", font=("Arial", 20, "bold")).place(x=40, y=100)

# bottom box
box = PhotoImage(file="bg.png")
label = Label(root, image=box).place(x=0, y=320)

# entry
entry = StringVar()
entry_widget = Entry(root, textvariable=entry, width=20, font=("Arial", 10, "bold"))
entry_widget.place(x=100, y=150) 

# search button
search_image = PhotoImage(file="search.png")
search = Button(root, image=search_image, bd=0, cursor="hand2", command=get_details)
search.place(x=100, y=190)

# label information
country = Label(root, text="Country", fg="black", bg="#57adff", font=("Arial", 10, "bold"))
country.place(x=50, y=350)

sim = Label(root, text="Sim", fg="black", bg="#57adff", font=("Arial", 10, "bold"))
sim.place(x=250, y=350)

zone = Label(root, text="Timezone", fg="black", bg="#57adff", font=("Arial", 10, "bold"))
zone.place(x=50, y=400)

clock = Label(root, text="Clock", fg="black", bg="#57adff", font=("Arial", 10, "bold"))
clock.place(x=250, y=400)

longitude_label = Label(root, text="Longitude", fg="black", bg="#57adff", font=("Arial", 10, "bold"))
longitude_label.place(x=50, y=450)

latitude_label = Label(root, text="Latitude", fg="black", bg="#57adff", font=("Arial", 10, "bold"))
latitude_label.place(x=250, y=450)

root.mainloop()
