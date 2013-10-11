#!/usr/bin/env python

import barobo
import ephem
import math
import time
from datetime import datetime

class LinkbotStarTracker(barobo.Linkbot):
  def __init__(self):
    barobo.Linkbot.__init__(self)

  def pointToBody(self, body):
    print "Moving to: {0} , {1}".format(float(body.alt)*180.0/math.pi, -1.0*float(body.az)*180.0/math.pi, 0)
    #self.moveTo(float(body.alt)*180.0/math.pi, -1.0*float(body.az)*180.0/math.pi, 0)
    self.driveToNB(float(body.alt)*180.0/math.pi, -1.0*float(body.az)*180.0/math.pi, 0)
#self.moveTo(float(body.az)*180.0/math.pi, 0, 0)
    #self.moveTo(0, 0, 0)


if __name__=="__main__":
  bot = LinkbotStarTracker()
  bot.connectWithSerialID("ZK53")
  observer = ephem.Observer()
  # The next three lines are used to set the observer's latitude, longitude,
  # and elevation (in meters). This information may be obtained from a GPS
  # unit, or from services such as google-maps, or even Wikipedia.
  observer.lat = ephem.degrees('37.5483')
  observer.lon =  ephem.degrees('-121.9875')
  observer.elevation = 20
  # Set the desired date; It does not have to be the current time if you are
  # interested in seeing where the celestial body was in the past, or will be in
  # the future.
  #d = ephem.Date('2013/7/19 22:34')
  d = ephem.Date(datetime.utcnow())
  observer.date = d

  # The next several lines demonstrate how to point to pre-configured Ephem
  # bodies, such as the Moon.
  #moon = ephem.Moon(observer)
  #bot.pointToBody(moon)

  #body = ephem.star('Polaris')
  #body = ephem.Venus()
  #body = ephem.Jupiter()
  body = ephem.Sun()
  body.compute(observer)
  bot.pointToBody(body)
  """
  # Loops such as the following can be used to track the path of a celestial
  # body in "fast forward".
  while True:
    d += 0.01
    observer.date = d
    body.compute(observer)
    bot.pointToBody(body)
    time.sleep(0.05)
  """
  raw_input('Press ENTER to begin tracking the International space station...')

  # To track certain objects such as the International Space Station, you need
  # an up-to-date "Two Line Element Set", or "TLE", obtained from websites such
  # as http://www.n2yo.com/satellite/?s=25544 . These do go out of date, so make
  # sure you grab a fresh one and copy/paste it into the lines below
  iss = ephem.readtle('ISS',
          '1 25544U 98067A   13200.66170009  .00016717  00000-0  10270-3 0  9002',
          '2 25544  51.6505 307.4145 0004709 206.6953 153.3956 15.49959633 39748'
      )
#raw_input('blah')
  while True:
    observer.date = datetime.utcnow()
    iss.compute(observer)
    bot.pointToBody(iss)
    time.sleep(1)
  while True:
    bot.pointToBody(polaris)
    d += 1
    observer.date = d
    print d
    sun.compute(observer)
    time.sleep(0.05)


