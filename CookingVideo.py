from asyncio import run_coroutine_threadsafe
import psycopg2
from random import randint
from config import config

#Define variable "Video"
Video = None
def watch():
    """ Connect to the PostgreSQL database server """
    
    #Define global variable "video"
    global Video

    conn = None
    try:
        # read connection parameters
        params = config('postgresql')

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)

        
        #Use random functions to get a random integer
        rannum = randint(1, 10)
        
        # create a cursor and execute the query
        cur = conn.cursor()
        cur.execute('select url from cookingvideo where cid ='+ str(rannum))
        conn.commit()
        video = cur.fetchall()
        Video = video[0][0]
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return Video

if __name__ == '__main__':
    watch()