from flask import Flask, request, render_template, url_for

from model.picture import picture
from util.helper import parseDate, getDatesFromFile, getLocalImages, serialize
from util.rover import RoverService

import json

app = Flask(__name__)

@app.route('/')
def index():
    picList = getLocalImages(app.config)
    return render_template('index.html', pictureList=picList)

@app.route('/picture/<date_str>', methods=("GET",))
def getPicturesByDate(date_str):
    """
    Endpoint to get pictures for a specific date
    """
    dateToMars = parseDate(date_str)
    if not dateToMars:
        return 'Invalid date {0}'.format(date_str), 404
    result = app.roverService.getPicturesByDate(dateToMars)
    return json.dumps(result, default=serialize)

@app.route('/acceptance', methods=("GET",))
def getAcceptance():
    """
    Endpoint for Living As One Acceptance Criteria
    """

    dateList = getDatesFromFile(app.config.get('RESOURCE_DATES_FILE'))
    picList = []

    for dateStr in dateList:
        dateToMars = parseDate(dateStr)
        if dateToMars:
            picList.append(app.roverService.getPicturesByDate(dateToMars))
        else:
            picList.append({'date': dateStr, 'pictures': []})

    return json.dumps({
        'dates': dateList,
        'pics': picList
    }, default=serialize)

def initApp():
    print('initializing app')
    app.config.from_object('config.DefaultConfig')
    app.roverService = RoverService(app.config)

if __name__ == '__main__':
    initApp()
    app.run(host='0.0.0.0', port=8081)
