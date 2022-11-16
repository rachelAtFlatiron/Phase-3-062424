# Pet : name: string species: string breed: string temperament:string, owner_id:int

import sqlite3

CONN = sqlite3.connect('lib/resources.db')
CURSOR = CONN.cursor()

class Pet:
    
    pass