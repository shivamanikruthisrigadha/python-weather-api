import requests


# ---------------------------------------
# CITY COORDINATES
# ---------------------------------------

cities = {
    "hyderabad": (17.3850, 78.4867),
    "vijayawada": (16.5062, 80.6480),
    "visakhapatnam": (17.6868, 83.2185),
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "chennai": (13.0827, 80.2707),
    "bangalore": (12.9716, 77.5946),
    "kolkata": (22.5726, 88.3639)
}


# ---------------------------------------
# FETCH WEATHER DATA
# ---------------------------------------

def get_weather(city):

    city = city.lower().strip()

    if city not in cities:
        print("\n❌ City not available.")
        print("Available cities:")

        for available_city in cities:
            print("-", available_city.title())

        return

    latitude, longitude = cities[city]

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,relative_humidity_2m,"
        "apparent_temperature,wind_speed_10m"
    )

    try:

        response = requests.get(url, timeout=10)

        # Check whether request was successful
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        current_weather = data["current"]

        temperature = current_weather["temperature_2m"]
        humidity = current_weather["relative_humidity_2m"]
        apparent_temperature = current_weather["apparent_temperature"]
        wind_speed = current_weather["wind_speed_10m"]

        print("\n======================================")
        print(f"       WEATHER REPORT - {city.title()}")
        print("======================================")

        print(f"Temperature        : {temperature} °C")
        print(f"Humidity           : {humidity} %")
        print(f"Feels Like         : {apparent_temperature} °C")
        print(f"Wind Speed         : {wind_speed} km/h")

        print("======================================")

    except requests.exceptions.RequestException as error:

        print("\n❌ Error while connecting to weather API.")
        print("Error:", error)


# ---------------------------------------
# SEARCH / FILTER
# ---------------------------------------

def search_city():

    search = input(
        "\nEnter city name to search: "
    ).lower().strip()

    matching_cities = [
        city for city in cities
        if search in city
    ]

    if matching_cities:

        print("\nMatching cities:")

        for city in matching_cities:
            print("-", city.title())

    else:

        print("\n❌ No matching city found.")


# ---------------------------------------
# MAIN PROGRAM
# ---------------------------------------

print("======================================")
print("       PYTHON WEATHER API")
print("======================================")

while True:

    print("\nChoose an option:")
    print("1. Get Weather")
    print("2. Search City")
    print("3. Show Available Cities")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        city = input("Enter city name: ")
        get_weather(city)

    elif choice == "2":

        search_city()

    elif choice == "3":

        print("\nAvailable Cities:")

        for city in cities:
            print("-", city.title())

    elif choice == "4":

        print("\nThank you for using Python Weather API!")
        break

    else:

        print("\n❌ Invalid choice. Please select 1, 2, 3 or 4.")