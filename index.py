from flask import render_template,request
from aqiapp import app
from models import *

@app.route("/")
def home():

    sensor_node_id_list = ['node2', 'node6']
    sensor_data = []
    sensor_data_pm25 = []
    sensor_data_temp = []
    sensor_data_hum = []
    sensor_name = 'node6'

    sensor_name=request.args.get("choose_node")

    #print(sensor_name)

    for sensor_node_id in sensor_node_id_list:
        sensor_node = MyNode(sensor_node_id)
        sensor_node.get_last_data()
        sensor_data.append(sensor_node.node_data)

        if sensor_node_id == sensor_name:
            #print(sensor_name)
            sensor_node.get_online_chart_data()
            sensor_data_pm25 = sensor_node.node_data_pm25
            sensor_data_temp = sensor_node.node_data_temp
            sensor_data_hum = sensor_node.node_data_hum



    print(sensor_data_pm25)
    print(sensor_data)
    return render_template('index.html',sensor_data=sensor_data,name=sensor_name,pm25=sensor_data_pm25,temp=sensor_data_temp,hum=sensor_data_hum)

@app.route("/test")
def test():
    return "WELCOME TO MY SITE!!!"

if __name__=="__main__":
    app.run(debug=True)

