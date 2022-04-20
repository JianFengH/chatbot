from asyncio import run_coroutine_threadsafe
import psycopg2
from config import config

#Define variable "route"
route = None
Photo = None
def checkroute3(routenum):
    """ Connect to the PostgreSQL database server """
    
    #Define global variable "route" and "Photo"
    global route
    global Photo
    #get the last number from command "/WILSON
    num = routenum[-1]
    
    conn = None
    try:
        # read connection parameters
        params = config('postgresql')

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
		
        # create a cursor and execute the query
        cur = conn.cursor()
        cur.execute('select route,url from wilson where rid ='+ num)
        conn.commit()
        route = cur.fetchall()
        Route = route[0][0]
        Photo = route[0][1]
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return Route, Photo

if __name__ == '__main__':
    checkroute3()