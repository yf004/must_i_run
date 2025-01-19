import geocoder

def get_user_location():
    # Get the user's location based on their IP address
    g = geocoder.ip('me')  # 'me' will get the current user's IP address
    if g.ok:
        print(f"IP Address: {g.ip}")
        print(f"Location: {g.city}, {g.state}, {g.country}")
        print(f"Latitude: {g.latlng[0]}, Longitude: {g.latlng[1]}")
    else:
        print("Could not retrieve location.")

    return [g.latlng[0], g.latlng[1]]

get_user_location()