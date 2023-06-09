import flask
from flask import jsonify
from flask import request
from sql import create_connection
from sql import execute_read_query
from sql import execute_query
import creds


#creating connection to mysql database
myCreds = creds.Creds()
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

#setting up an application name
app = flask.Flask(__name__) #sets up the application
app.config["DEBUG"] = True #allow to show errors in browser

#test commit

#default url without any routing as GET request
@app.route('/', methods=['GET'])
def home():
    return "<h1> WELCOME TO OUR FIRST API! </h1>"

#endpoint to get all gems http://127.0.0.1:5000/api/gem/all
@app.route('/api/gem/all', methods=['GET'])
def api_all():
    select_gems = "SELECT gem_type, gem_color, carat, price FROM gem_table"
    #print(select_gems)
    gems = execute_read_query(conn, select_gems)
    results =[]
    for gem in gems:
        results.append(gem)
    return jsonify(results)

#endpoint to get a single gem  : http://127.0.0.1:5000/api/gem?id=1
@app.route('/api/gem', methods=['GET'])
def api_id():
    if 'id' in request.args: #only if an id is provided as an argument, proceed
        id = int(request.args['id'])
        select_gems = "SELECT gem_type, gem_color, carat, price FROM gem_table WHERE id = %s" %(id)
        gems = execute_read_query(conn, select_gems)
        results =[]
        for gem in gems:
            if ['id'] == id:
                results.append(gem)
        return jsonify(results)
    else:
        return 'ERROR: No ID provided!'
  

#POST Statement 
@app.route('/api/gem', methods=['POST']) #Insert a new gem
def add_example():
    request_data = request.get_json()
    #newid = request_data['id']
    newgemtype = request_data['GemType']
    newgemcolor = request_data['GemColor']
    newcarat = request_data['Carat']
    newprice = request_data['Price']
    insert_gem = "INSERT INTO gem_table (gem_type, gem_color, carat, price) VALUES('%s', '%s', %s, %s) " % (newgemtype,newgemcolor, newcarat, newprice)
    execute_query(conn, insert_gem)
    return 'Add request was successful'

#Put Statement 
#http://127.0.0.1:5000/api/gem= # Add id you wish to update

@app.route('/api/gem/put', methods=['PUT']) # Use this input if you want to update
def put_example():
    request_data = request.get_json()
    newid = request_data['id']
    newgemtype = request_data['GemType']
    newgemcolor = request_data['GemColor']
    newcarat = request_data['Carat']
    newprice = request_data['Price']
    update_gem = "UPDATE gem_table SET gem_type ='%s', gem_color = '%s', carat = %s, price = %s " % (newgemtype, newgemcolor,newcarat, newprice)
    execute_query(conn, update_gem)
    return 'Update request was successful'

#Delete Statement 
@app.route('/api/gem/delete', methods=['DELETE']) #http://127.0.0.1:5000/api/gem/put?id=  #Add id you wish to delete
def delete_example():
    request_data = request.get_json()
    idToDelete = request_data['id']
    delete_gem = "Delete FROM gem_table WHERE id=%s"  % (idToDelete)
    execute_query(conn, delete_gem)
    return "Delete request successful"


#Users is the database nane # SQL
@app.route('/api/admin', methods=['GET'])
def api_users_id():
    if 'id' in request.args: 
        id = int(request.args['id'])
    else:
        return 'ERROR: No ID provided!'
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "SELECT * FROM admin"
    users = execute_read_query(conn, sql)
    results = []

    for user in users:
        if user['id'] == id:
            results.append(user)
    return jsonify(results)

app.run()

