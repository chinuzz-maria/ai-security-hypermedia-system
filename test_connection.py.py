import pyorient

client = pyorient.OrientDB("localhost", 2424)
session_id = client.connect("root", "root")
print("Connected to OrientDB!")

if not client.db_exists("AISecurityDB"):
    client.db_create("AISecurityDB",
                     pyorient.DB_TYPE_GRAPH,
                     pyorient.STORAGE_TYPE_PLOCAL)
    print("Database AISecurityDB created!")
else:
    print("Database already exists!")

client.db_open("AISecurityDB", "root", "root")
print("Ready to build your project!")
