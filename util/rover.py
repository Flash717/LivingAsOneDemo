import os.path
import requests

from model.picture import picture

class RoverService(object):

    def __init__(self, config):
        self.url = config.get('NASA_MARS_ROVER_API_URL')
        self.urlKey = config.get('NASA_MARS_ROVER_API_KEY')
        self.destination_folder = config.get('PICTURE_FOLDER')

    def getPicturesByDate(self, dateStr):
        pictureArray = []
        page = 1
        data = {}
        while len(data.get('photos', [])) > 0 or page == 1:
            requestUrl = self.url.format(dateStr, page, self.urlKey)
            r = requests.get(requestUrl)
            if r.status_code != 200:
                return pictureArray
            data = r.json()
            for i in data.get('photos', []):
                imgUrl = i.get('img_src')
                imgName, fileName = self.savePictureFromUrl(imgUrl, dateStr)
                pictureArray.append(picture(imgName, fileName, i['rover']['name'], i['camera']['name'], i['camera']['full_name']))
            page += 1
        return {
            'date': dateStr,
            'pictures': pictureArray
        }

    def savePictureFromUrl(self, imgUrl, dateStr):
        imgName = imgUrl.split('/')[-1]
        destFolder = self.destination_folder + '/' + dateStr 
        destFile = destFolder + '/' + imgName

        if not os.path.exists(destFolder):
            os.makedirs(destFolder)

        r = requests.get(imgUrl)

        with open(destFile, 'wb') as f:
            f.write(r.content)
        
        return imgName, destFile
