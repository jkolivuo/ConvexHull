TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)
 
def turn(x, y, z):
    #Liikkumissuunnan päättäminen
    return cmp((y[0] - x[0])*(z[1] - x[1]) - (z[0] - x[0])*(y[1] - x[1]), 0)
 
def dist(p1, p2):
    #Kahden vektorin pistetulo esim v * u
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    return dx * dx + dy * dy
 
def next_point(points, p):
    #Selvitetään seuraava piste, eli käännytään oikealle tai ei ollenkaan.
    q = p
    for r in points:
        t = turn(p, q, r)
        if t == TURN_RIGHT or t == TURN_NONE and dist(p, r) > dist(p, q):
            q = r
    return q
 
def jarvis_march(points):
    #käydään läpi pisteet
    hull = [min(points)]
    for point in hull:
        x = next_point(points, point)
        if x != hull[0]:
            hull.append(x)
    return hull
    

  

    
