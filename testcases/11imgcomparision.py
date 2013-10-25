#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
image comparision library
depend:
<sudo apt-get install python-opencv>
options:
[sudo apt-get install python-numpy]
'''

import os
import urllib2
import commands
try:
    import cv2
    from cv2 import cv
except ImportError, e:
    print e
    #print 'denpendcy python-opencv: \n\tsudo apt-get install -y python-opencv'
    print 'installing denpendcy python-opencv: \n\tsudo apt-get install -y python-numpy '
    ret = commands.getoutput('sudo apt-get install -y python-opencv')
    print ret
    try:
        import cv2
        from cv2 import cv
    except ImportError, e:
        print e
        print 'installing denpendcy python-numpy: \n\tsudo apt-get install -y python-numpy '
        ret = commands.getoutput('sudo apt-get install -y python-numpy')
        print ret
        import cv2
        from cv2 import cv

__version__ = "1.0"
__author__ = "bhb"
__all__ = ['isMatch', 'getMatchedCenterOffset', 'isMatchFromUrl']

def isMatch(subPath, srcPath, threshold=0.01):
    '''
    check wether the subPath image exists in the srcPath image.
    @type subPath: string
    @params subPath: the path of searched template. It must be not greater than the source image and have the same data type.
    @type srcPath: string
    @params srcPath: the path of the source image where the search is running.
    @type threshold: float
    @params threshold: the minixum value which used to increase or decrease the matching threshold. 0.01 means at most 1% difference.
                       default is 0.01. 
    @rtype: boolean
    @return: true if the sub image founded in the src image. return false if sub image not found or any exception.
    '''
    for img in [subPath, srcPath]: assert os.path.exists(img) , 'No such image:  %s' % (img)
    method = cv2.cv.CV_TM_SQDIFF_NORMED #Parameter specifying the comparison method 
    try:
        subImg = cv2.imread(subPath) #Load the sub image
        srcImg = cv2.imread(srcPath) #Load the src image
        result = cv2.matchTemplate(subImg, srcImg, method) #comparision
        minVal = cv2.minMaxLoc(result)[0] #Get the minimum squared difference
        if minVal <= threshold: #Compared with the expected similarity
            return True
        else:
            return False
    except:
        return False
    
def getMatchedCenterOffset(subPath, srcPath, threshold=0.01):
    '''
    get the coordinate of the mathced sub image center point.
    @type subPath: string
    @params subPath: the path of searched template. It must be not greater than the source image and have the same data type.
    @type srcPath: string
    @params srcPath: the path of the source image where the search is running.
    @type threshold: float
    @params threshold: the minixum value which used to increase or decrease the matching threshold. 0.01 means at most 1% difference.
                       default is 0.01. 
    @rtype: tuple
    @return: (x, y) the coordniate tuple of the matched sub image center point. return None if sub image not found or any exception.
    '''
    for img in [subPath, srcPath]: assert os.path.exists(img) , "No such image:  %s" % (img)
    method = cv2.cv.CV_TM_SQDIFF_NORMED #Parameter specifying the comparison method 
    try:
        subImg = cv2.imread(subPath) #Load the sub image
        srcImg = cv2.imread(srcPath) #Load the src image
        result = cv2.matchTemplate(subImg, srcImg, method) #comparision
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result) #Get the minimum squared difference
        if minVal <= threshold: #Compared with the expected similarity
            minLocXPoint, minLocYPoint = minLoc
            subImgRow, subImgColumn = subImg.shape[:2]
            centerPoint = (minLocXPoint + int(subImgRow/2), minLocYPoint + int(subImgColumn/2))
            return centerPoint
        else:
            return None    
    except Exception,e:
        return None

def isMatchFromUrl(subUrl, srcUrl, threshold=0.01):
    '''
    check wether the subUrl image exists in the srcUrl image.
    @type subUrl: string
    @params subUrl: the url path of searched template. It must be not greater than the source image and have the same data type.
    @type srcUrl: string
    @params srcUrl: the url path of the source image where the search is running.
    @type threshold: float
    @params threshold: the minixum value which used to increase or decrease the matching threshold. 0.01 means at most 1% difference.
                       default is 0.01. 
    @rtype: boolean
    @return: true if the sub image founded in the src image. return false if sub image not found or any exception.
    '''
    subPath = download(subUrl)
    srcPath = download(srcUrl)
    for img in [subPath, srcPath]: assert os.path.exists(img) , 'No such image:  %s' % (img)
    method = cv2.cv.CV_TM_SQDIFF_NORMED #Parameter specifying the comparison method 
    try:
        subImg = cv2.imread(subPath) #Load the sub image
        srcImg = cv2.imread(srcPath) #Load the src image
        result = cv2.matchTemplate(subImg, srcImg, method) #comparision
        minVal = cv2.minMaxLoc(result)[0] #Get the minimum squared difference
        if minVal <= threshold: #Compared with the expected similarity
            return True
        else:
            return False
    except:
        return False

def download(url):
    '''
    return the abs path of donwloaded file. may throw any exceptions of urllib2.
    '''
    img_name = os.path.split(url)[-1]
    with open(img_name, 'wb') as f:
       f.write(urllib2.urlopen(url).read())
    return os.path.abspath(img_name)
    

#test method
if __name__ == '__main__':
    #print isMatch(subPath='sub1.png', srcPath='full1.png', threshold=0.1)
    #print getMatchCenterOffset(subPath='sub1.png', srcPath='full1.png', threshold=0.01)
    #print download("http://ats.borqs.com/smartserver/static/img/logo-s.png")
    print 'comparision result: %s' % isMatchFromUrl('http://ats.borqs.com/smartserver/static/sub1.png', 'http://ats.borqs.com/smartserver/static/full1.png')
    

