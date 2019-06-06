import pyowm

owm = pyowm.OWM('f348c282b8a9db792250e7df04604cf0', language="ru")

observation = owm.weather_at_place('Алматы')
w = observation.get_weather()
temperature = w.get_temperature('celsius')["temp"]
wStatus = w.get_detailed_status()

global weatherText
weatherText = "Температура: " + str(temperature) + "\n" + "Статус: " + wStatus
print("Температура: " + str(temperature) + "\n" + "Статус: " + wStatus)
