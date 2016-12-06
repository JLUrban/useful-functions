"""

"""
class gust:
    open_sea = np.array([1.3, 1.3,1.3])
    isolated_hilltops = np.array([1.4, 1.4,1.5])
    flat_open_country = np.array([1.6, 1.4,1.8] )
    rolling_country_few_wind_breaks = np.array([1.7, 1.5, 2.0])
    rolling_country_many_wind_breaks =np.array( [1.9, 1.7, 2.1])
    center_of_large_cities = np.array([2.1, 1.9, 2.3])
    
    
def heavi(x):
    return np.sign(x)*.5+.5

def rect(x,dx):
    return heavi(x-dx*0.5)*heavi(dx*0.5 - x)


class pcolor:
    RED        = "\x1b[31m"
    TEST       = "\x1b[72m"
    REDHIGHLIGHT       = "\x1b[41m"
    GREY       = "\x1b[37m"
    GRAY       = "\x1b[37m"
    CYAN       = "\x1b[36m"
    PURPLE     = "\x1b[35m"
    BLUE       = "\x1b[34m"
    YELLOW     = "\x1b[33m"
    GREEN      = "\x1b[32m"
    WARNING    = "\x1b[93m"
    FAIL       = "\x1b[91m"
    ENDCc      = "\x1b[0m"
    BOLD       = "\x1b[101m"
    NOBOLD       = "\x1b[00m"
    UNDERLINE  = "\X1b[04m"
    BLACK      = "\x1b[0m"