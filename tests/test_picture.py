import pytest

from model.picture import picture

@pytest.mark.parametrize("imgName,imgSrc,roverName,cameraName,cameraFullName",
                         [('test1', 'resources/test1.jpg', '', '', ''),
                         ('test2', 'resources/test2.jpg', 'LandRover', 'CAM', 'Camera At Mars')])
def test_pictureConstructor(imgName, imgSrc, roverName, cameraName, cameraFullName):
    p = picture(imgName, imgSrc, roverName, cameraName, cameraFullName)
    assert(p is not None)
    assert(p.imgName == imgName)
    assert(p.imgSrc == imgSrc)
    assert(p.roverName == roverName)
    assert(p.cameraName == cameraName)
    assert(p.cameraFullName == cameraFullName)

