
def name():
    m = float (input (""))
    v = float (input(""))
    ke = kineticenergy (m.v)
    Display (ke)

def kineticenergy (m,v):
    ke= 0.5 * m *v*v
    return ke

def display (ke):
    print ("", ke)
