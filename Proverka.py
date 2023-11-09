def Proverka(WaterTime, wateringInterval, temperature, humidity, impurityLevel):
    try:
        WaterTime = int(WaterTime.get())
        wateringInterval = int(wateringInterval.get())
        temperature = float(temperature.get())
        humidity = int(humidity.get())
        impurityLevel = int(impurityLevel.get())
        return True
    except Exception as e:
        return False