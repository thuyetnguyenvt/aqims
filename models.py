import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("maapp_cer.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://aqimonitoringsystem-default-rtdb.firebaseio.com/'
})

class MyNode():

    # a dict to store sensordata
    node_datetime = 0
    node_data = {}

    def __init__(self,name):

        self.node_name=name

    def get_last_data(self):
        snapshot = db.reference(self.node_name).order_by_key().limit_to_last(1).get()
        for key,val in snapshot.items():
            #for sub_key,sub_val in val.items():
                #print("{0} => {1}".format(key,val))
            self.node_datetime = str(key)
            self.node_data = val

        #print(self.date_time)
        #print(self.node_data)

if __name__=="__main__":
    sensor_node_2 = MyNode('node2')
    #sensor_node_2.get_last_data()
    print(sensor_node_2.node_data)
    print(sensor_node_2.node_datetime)
