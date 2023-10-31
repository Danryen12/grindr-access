from grindrUser import grindrUser
from xmpp import connect

user = grindrUser()
mail = input("Email: ")
password = input("Password: ")

user.login(mail, password)
print("------------------- profiles -------------------")
print(user.getProfiles(39.476916, -99.796235))
print("------------------- taps -------------------")
print(user.getTaps())
print("------------------- sessions -------------------")
print(user.sessions(mail))
print("------------------- xmpp -------------------")
connect(user.generatePlainAuth())
