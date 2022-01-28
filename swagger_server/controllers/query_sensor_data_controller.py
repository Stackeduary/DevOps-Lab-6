import connexion
import six
from flask import jsonify
from swagger_server import util
import json
import pandas as pd


def get_maximum(sensor):  # noqa: E501
    """Find maximum sensor data by ID

    Returns a list of sensor data # noqa: E501

    :param sensor: Device ID to search for the data
    :type sensor: str

    :rtype: Device
    """
    return 'do some magic!'


def get_sensor_by_id(deviceId):  # noqa: E501
    """Find sensor data by ID

    Returns a list of sensor data # noqa: E501

    :param deviceId: Device ID to search for the data
    :type deviceId: int

    :rtype: Device
    """
    try:
        df = pd.read_csv("/tmp/iot.csv")
        if deviceId in df['dev_id'].values:
            df_deviceId = df.loc[df['dev_id'] == deviceId]
            df_resp = df_deviceId[['dev_id', 'device_name', 'snr']]
            data = df_resp.to_json(orient="records")
            status = 200
        else:
            status = 400
            data = {"Error message": "Invalid device"}
    except Exception as e:
        data = {"Error message": str(e)}
        status = 400
    return json.loads(data), status


def getminimum(sensor):  # noqa: E501
    """Find minimum sensor data by ID

    Returns a list of sensor data # noqa: E501

    :param sensor: Device ID to search for the data
    :type sensor: str

    :rtype: Device
    """
    return 'do some magic!'
