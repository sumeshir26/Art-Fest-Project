# DATABASE FUNCTIONS
import tinydb

# Main DB Class
db = tinydb.TinyDB('db.json')

def add_user(phone_no):
    db.insert({phone_no: 0})
    print(f"Added {phone_no} to database")  
    print(db.all())

def clear_db():
    db.purge()

def add_tokens(phone_no, tokens):
    db.search(tinydb.where(phone_no) == phone_no)[0] += tokens

def subtract_tokens(phone_no, tokens):
    db.search(tinydb.where(phone_no) == phone_no)[0] -= tokens

def get_tokens(phone_no):
    try:
        return db.search(tinydb.where(phone_no) == phone_no)[0]
    except:
        add_user(phone_no)
        return db.search(tinydb.where(phone_no) == phone_no)[0]

def set_tokens(phone_no, tokens):
    db.search(tinydb.where(phone_no) == phone_no)[0] = tokens
