
def board(dim):
    """Fallið prentar út borðið m.v. vídd sem leikmaður gefur upp."""
    while number <= (dim*2):

    for number in range(1, (dim**2)+1):
        print ("{:>5d}".format(number), end= "")
        print ("\n")



dimension = int(input("Input dimension of the board: "))
board(dimension)

