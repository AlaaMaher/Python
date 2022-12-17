"""
----------------------
--- Dictionary ---
----------------------
[1]Dic Items Are Enclosed in Curly Braces
[2] Dic Items contains Key:value
[3] Dic Key need to be immutable -> (Numbers,String,Tuple)
[4] Dic Value Can Have Any Data Type
[5] Dic Key Needs To Be Unique
[6] Dic is Not ordered access it by element with name of Key
"""
user = {'name': 'AbdelMalik', 'password': '123$', 'age': 14.5,
        'skills': ['Programming', 'Sport']}  # Can't Show Error  #Error
print(user)
print(user['password'])
print(user.get('age'))
print(user.keys())
print(user.values())
