import connexion
import six
from flask import jsonify
from swagger_server import util
import pandas as pd
import json


def upload_post(upfile):  # noqa: E501
    """Uploads a file.

     # noqa: E501

    :param upfile: The file to upload.
    :type upfile: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    df = pd.read_csv(upfile)
    df.to_csv("/tmp/iot.csv")
    data = {"message": "File successfully uploaded"}
    return data, 200
