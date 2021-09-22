def returnRGB(colors):
    rgb_list = [x[0] for x in colors]
    return rgb_list




def nearestColour(subjects, query):
    return min(subjects, key = lambda subject: sum((s - q) ** 2 for s, q in zip( subject, query ) ) )
