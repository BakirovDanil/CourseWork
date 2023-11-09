def Proverka(firstCu, secondCu, maxCu, minCu):
    try:
        firstCu = float(firstCu.get())
        secondCu = float(secondCu.get())
        maxCu = float(maxCu.get())
        minCu = float(minCu.get())
        return True
    except Exception as e:
        return False