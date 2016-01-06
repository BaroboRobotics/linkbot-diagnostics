#!/usr/bin/env python3

import sqlite3 as sql
import sys
import numpy
try:
    import pylab
except:
    pass

import os
import appdirs

db_file = os.path.join(appdirs.user_data_dir(), "linkbot-diagnostics","database.db")

def main():
  con = sql.connect(db_file)
  compareMotorSpecs(con.cursor())
  #data = LinkbotData(con.cursor())

class LinkbotDatabase:
  def __init__(self):
    self.con = sql.connect(db_file)
    self.con.row_factory = sql.Row
    self.cur = self.con.cursor()

  def getIDs(self):
    """Return list of all linkbot serial IDs"""
    self.cur.execute('SELECT Id FROM robot_type')
    ids = self.cur.fetchall()
    idlist = []
    for id in ids:
      idlist.append(id[0])
    return idlist

  def getLinkbotData(self, serialID):
    """ Only get the latest linkbot data """
    mydict = {}
    self.cur.execute('SELECT * FROM robot_type WHERE (ID is \'{}\')'.format(serialID))
    row = self.cur.fetchone()
    mydict['Id'] = serialId
    self.cur.execute('SELECT * FROM linearity_tests WHERE (ID is \'{}\') ORDER BY Date DESC'.format(serialID))
    row = self.cur.fetchone()
    date = row['Date']
    

    


def compareMotorSpecs(cursor):
  cur = cursor
  cur.execute('SELECT * FROM robot_type')
  rows = cur.fetchall()
  cur.execute('SELECT Id FROM robot_type WHERE formfactor = \'Linkbot-I\'')
  rows = cur.fetchall()
  linkboti_ids = list(map(lambda x: x[0].encode('ascii'), rows))
  print (linkboti_ids)
  cur.execute('SELECT Id FROM robot_type WHERE formfactor = \'Linkbot-L\'')
  rows = cur.fetchall()
  linkbotl_ids = list(map(lambda x: x[0].encode('ascii'), rows))
  print (len(list(linkbotl_ids)))
  rows = []
  '''
  for id in linkbotl_ids:
    cur.execute(
        'SELECT * FROM linearity_tests WHERE '
        '(Id IS \'{0}\') ORDER BY Date DESC'.format(id.decode()))
    row = cur.fetchone()
    print("Row: ", row)
    if row is not None:
        rows.append(row)
  _, _, lm1fspeeds, lm1fRs, lm1bspeeds, lm1bRs, lm2fspeeds, lm2fRs, lm2bspeeds, lm2bRs = zip(*rows)
  '''

  for id in linkboti_ids + linkbotl_ids:
    cur.execute(
        'SELECT * FROM linearity_tests WHERE '
        '(Id IS \'{}\') ORDER BY Date DESC'.format(id.decode()))
    rows.append(cur.fetchone())
  _, _, im1fspeeds, im1fRs, im1bspeeds, im1bRs, im2fspeeds, im2fRs, im2bspeeds, im2bRs = zip(*rows)

#pylab.hist([i_1_speeds+i_3_speeds, l_1_speeds + l_2_speeds], label="Linkbot-I Motor 1 speeds")
#pylab.hist(i_1_speeds + i_3_speeds + l_1_speeds + l_2_speeds)
#pylab.hist(i_3_speeds, label="Linkbot-I Motor 3 speeds")
#pylab.hist([l_1_speeds, l_2_speeds])
#  pylab.hist([i_1_speeds, i_3_speeds])
#pylab.hist([m1fRs, m1bRs, m2fRs, m2bRs])
#pylab.hist([im1fspeeds, map(abs, im1bspeeds), im2fspeeds, map(abs, im2bspeeds)])
#pylab.hist([lm1fspeeds, map(abs, lm1bspeeds), lm2fspeeds, map(abs, lm2bspeeds)])
  '''
  print ("LINKBOT-I")
  print ("Mean J1 Forward Speed: {}".format(numpy.mean(im1fspeeds)))
  print ("Std Dev J1 Forward Speed: {}".format(numpy.std(im1fspeeds)))
  print ("Mean J1 Forward R Value: {}".format(numpy.mean(im1fRs)))
  print ("Std Dev J1 Forward R Value: {}".format(numpy.std(im1fRs)))
  print ("Mean J1 Backward Speed: {}".format(numpy.mean(im1bspeeds)))
  print ("Std Dev J1 Backward Speed: {}".format(numpy.std(im1bspeeds)))
  print ("Mean J1 Backward R Value: {}".format(numpy.mean(im1bRs)))
  print ("Std DevJ1 Backward R Value: {}".format(numpy.std(im1bRs)))
  print ("Mean J3 Forward Speed: {}".format(numpy.mean(im2fspeeds)))
  print ("Std Dev J3 Forward Speed: {}".format(numpy.std(im2fspeeds)))
  print ("Mean J3 Forward R Value: {}".format(numpy.mean(im2fRs)))
  print ("Std Dev J3 Forward R Value: {}".format(numpy.std(im2fRs)))
  print ("Mean J3 Backward Speed: {}".format(numpy.mean(im2bspeeds)))
  print ("Std Dev J3 Backward Speed: {}".format(numpy.std(im2bspeeds)))
  print ("Mean J3 Backward Rs: {}".format(numpy.mean(im2bRs)))
  print ("Std Dev J3 Backward Rs: {}".format(numpy.std(im2bRs)))

  print ("LINKBOT-L")
  print ("Mean J1 Forward Speed: {}".format(numpy.mean(lm1fspeeds)))
  print ("Std Dev J1 Forward Speed: {}".format(numpy.std(lm1fspeeds)))
  print ("Mean J1 Forward R Value: {}".format(numpy.mean(lm1fRs)))
  print ("Std Dev J1 Forward R Value: {}".format(numpy.std(lm1fRs)))
  print ("Mean J1 Backward Speed: {}".format(numpy.mean(lm1bspeeds)))
  print ("Std Dev J1 Backward Speed: {}".format(numpy.std(lm1bspeeds)))
  print ("Mean J1 Backward R Value: {}".format(numpy.mean(lm1bRs)))
  print ("Std DevJ1 Backward R Value: {}".format(numpy.std(lm1bRs)))
  print ("Mean J3 Forward Speed: {}".format(numpy.mean(lm2fspeeds)))
  print ("Std Dev J3 Forward Speed: {}".format(numpy.std(lm2fspeeds)))
  print ("Mean J3 Forward R Value: {}".format(numpy.mean(lm2fRs)))
  print ("Std Dev J3 Forward R Value: {}".format(numpy.std(lm2fRs)))
  print ("Mean J3 Backward Speed: {}".format(numpy.mean(lm2bspeeds)))
  print ("Std Dev J3 Backward Speed: {}".format(numpy.std(lm2bspeeds)))
  print ("Mean J3 Backward Rs: {}".format(numpy.mean(lm2bRs)))
  print ("Std Dev J3 Backward Rs: {}".format(numpy.std(lm2bRs)))
  '''

  print ("Combined")
  speeds = im1fspeeds + im1bspeeds + im2fspeeds + im2bspeeds 
  speeds = list(map(abs, speeds))
  print ("Mean speeds: {}".format(numpy.mean(speeds)))
  print ("Std Dev speeds: {}".format(numpy.std(speeds)))
  Rvalues = im1fRs + im1bRs + im2fRs + im2bRs 
  print ("Mean R values: {}".format(numpy.mean(Rvalues)))
  print ("Std dev R values: {}".format(numpy.std(Rvalues)))

  try:
      #pylab.hist([list(im1fspeeds) + map(abs, im1bspeeds), list(lm1fspeeds) + map(abs, lm1bspeeds)])
      #pylab.hist([list(im1fspeeds) + map(abs, im1bspeeds), list(im2fspeeds) + map(abs, im2bspeeds)])
      #pylab.plot([numpy.mean(im1fspeeds), numpy.mean(im1bspeeds)])
      pylab.hist(speeds)
      pylab.show()
      pylab.hist(Rvalues)
      pylab.show()
  except:
      pass


def displayLinkbotData(serialid):
  ignore_keys = ['Id', 'Date']
  con = sql.connect(db_file)
  con.row_factory = sql.Row
  cur = con.cursor()
  cur.execute('SELECT * FROM linearity_tests WHERE (Id is \'{}\') ORDER BY Date DESC'.format(serialid))
  row = cur.fetchone()
  if row == None:
    print('No data for serial ID {}.'.format(serialid))
    return
  print(row['Date'])
  for k in row.keys():
    if k in ignore_keys:
      continue
    print('{}: {}'.format(k, row[k]))

  cur.execute('SELECT * FROM static_friction_tests WHERE (Id is \'{}\') ORDER BY Date DESC'.format(serialid))
  rows = cur.fetchall()
  for row in rows:
    if row == None:
      print('No data for serial ID {}.'.format(serialid))
      return
    for k in row.keys():
      if k in ignore_keys:
        continue
      print('{}: {}'.format(k, row[k]))

  con.close()
  

def findLopsidedMotors():
  """Return list of IDs of robots with lopsided motors"""
  con = sql.connect(db_file)
  con.row_factory = sql.Row
  cur = con.cursor()
  cur.execute('SELECT Id FROM robot_type')
  ids = cur.fetchall()
  ids_lopsided = []

  for id in ids:
    cur.execute(
        'SELECT * FROM linearity_tests WHERE '
        '(Id IS \'{}\') ORDER BY Date DESC'.format(id['Id']))
    row = cur.fetchone()
    if motorLopsided(row['m1forward_slope'], row['m1backward_slope']) or \
         motorLopsided(row['m2forward_slope'], row['m2backward_slope']):
      ids_lopsided.append(id['Id'])
  con.close()
  return ids_lopsided
    
def motorLopsided(fspeed, bspeed):
  if abs(abs(fspeed) - abs(bspeed)) > 30:
    return True
  else:
    return False

if __name__ == '__main__':
  if len(sys.argv) < 2: 
    main()
  else:
    displayLinkbotData(sys.argv[1])
