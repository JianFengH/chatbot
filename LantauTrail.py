from asyncio import run_coroutine_threadsafe
import psycopg2
from config import config

#Define variable "route"
route = None

def checkroute2(routenum):
    """ Connect to the PostgreSQL database server """
    
    #Define global variable "route"
    global route
    #get the last number from command "/MACLEHOSE"
    num = routenum[-1]
    
    conn = None
    try:
        # read connection parameters
        params = config('postgresql')

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
		
        # create a cursor and execute the query
        cur = conn.cursor()
        cur.execute('select route from lantau where rid ='+ num)
        conn.commit()
        route = cur.fetchall()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return route

if __name__ == '__main__':
    checkroute2()