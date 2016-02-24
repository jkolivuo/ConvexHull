from operator import itemgetter


TURN_LEFT, TURN_RIGHT, NONE = (1,-1,0)

def turning(p1,p2,p3):
    #liikkumisuunnan paattaminen
    return cmp((p2[0] - p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0]),0)


def _keep_right(hull, r):
    #Käännytään vain oikealle
    while len(hull) >1 and turning(hull[-2], hull[-1], r) != TURN_RIGHT:
        hull.pop()

    if not hull or hull[-1] != r:
        hull.append(r)
    return hull

def graham_scan(points):

    num = len(points)
    #Järjestetään koordinaatit y-akselin mukaan
    points.sort(key=itemgetter(1), reverse=False)
    

    l = reduce(_keep_right, points, [])
    u = reduce(_keep_right, reversed(points), [])

    #Ei otetan huomioon ensimmäistä ja viimeistä pistettä, koska niiden pitäisi olla sama
    l.extend(u[i] for i in xrange(1, len(u) -1 ))
    return l
    

