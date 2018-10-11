
def board(dim):
    """Fallið prentar út borðið m.v. vídd sem leikmaður gefur upp."""
    # vil prenta línu sem er 1 uppí n, svo n+1 uppí 2n, 2n+1 uppí 3n osfrv.
    for number in range (1, (dim**2)+1):
        while number <= dim:
            for number in range(1, dim+1):      # gera meira global!
                print ("{:>5d}".format(number), end= "")
            for number in range((dim+1), (dim*2)+1):
                print ("{:>5d}".format(number), end= "")



dimension = int(input("Input dimension of the board: "))
board(dimension)

