email_id="saketh@codegnan.com"
v=(email_id[7:15])
print(len(v))
email_ids=['saketh@codegnan.com','support@codegnan.com','ceo@codegnan.com','info@codegnan.com']
print(len(email_ids))
print(email_ids[1])

email_ids.extend(['dsa@codegnan.com','python@codegnan.com','frontend@codegnan.com'])
print(email_ids)
users={}
users=dict.fromkeys(email_ids)
print(users)
