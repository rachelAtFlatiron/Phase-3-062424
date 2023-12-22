# Stretch Goal: Build Out Corresponding Owner Class Methods

# Owner Attributes: 
# name: string 
# phone: string 
# email: string 
# address: string

import sqlite3

CONN = sqlite3.connect('lib/resources.db')
CURSOR = CONN.cursor()

class Owner:
    
    def __init__(self, name, email, id="None"):
        self.name = name 
        self.email = email 
        self.id = id

    # ✅ 12. Create table

    # ✅ 13. Drop table

    # ✅ 14. Insert row

            # ✅ 14a. Update instance with new row's id


    # ✅ 15. Get all rows
    # ✅ 15a. Create helper method to turn a row into an owner instance

    # ✅ 16. Get row by id

    # ✅ 17. Delete row by id

    # ✅ 18. Update row by id

    def __repr__(self):
        return f'<Owner id={self.id} name={self.name} />'