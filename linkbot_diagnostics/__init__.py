
import linkbot3
import json
import mysql.connector as sql
import os
import time

class Database() :
    DB_NAME = "linkbot_diagnostics"
    def __init__(self):
        # See if the config file exists
        try:
            config_path = os.path.join(
                os.environ['HOME'],
                '.local',
                'etc',
                'barobo_database.json')
            with open(config_path, 'r') as f:
                config = json.load(f)
                print(config)
                self.con = sql.connect(**config)
        except Exception as e:
            raise

        self.cursor = self.con.cursor()

        try:
            self.con.database = self.DB_NAME
        except sql.Error as err:
            if err.errno == sql.errorcode.ER_BAD_DB_ERROR:
                self.create_database()
                cnx.database = self.DB_NAME
            else:
                print(err)
                exit(1)

        self.initialize_tables()

    def create_database(self):
        cursor = self.cursor
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            sys.exit(1)

    def initialize_tables(self):
      try:
        cur = self.cursor
        cur.execute("CREATE TABLE IF NOT EXISTS robot_type (Id TEXT, "
              "formfactor TEXT)")
        cur.execute('CREATE TABLE IF NOT EXISTS speed_tests (Id TEXT, '
              'Date DATE, '
              'm1forward FLOAT, '
              'm1backward FLOAT, '
              'm2forward FLOAT, '
              'm2backward FLOAT)')

        cur.execute('CREATE TABLE IF NOT EXISTS linearity_tests (Id TEXT, '
              'Date DATE, '
              'm1forward_slope FLOAT, '
              'm1forward_R FLOAT, '
              'm1backward_slope FLOAT, '
              'm1backward_R FLOAT, '
              'm2forward_slope FLOAT, '
              'm2forward_R FLOAT, '
              'm2backward_slope FLOAT, '
              'm2backward_R FLOAT)')

        cur.execute('CREATE TABLE IF NOT EXISTS static_friction_tests(Id TEXT, '
              'Date DATE, '
              'Motor INT, '
              'Direction INT, '
              'Angle INT, '
              'Value INT)')

        """
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        rows = cur.fetchall()
        for row in rows:
          print row[0]
        """
        
      except sql.Error as e:
        print ("Error %s:" % e.args[0])
        sys.exit(1)

    def insert_robot_linearity( self, 
                   serial_id,
                   date,
                   f1_slope,
                   f1_r,
                   b1_slope,
                   b1_r,
                   f2_slope,
                   f2_r,
                   b2_slope,
                   b2_r,
                   notes='' ):
        self.cursor.execute("INSERT INTO linearity_tests "
            "VALUES('{}', '{}', {}, {}, {}, {}, {}, {}, {}, {}, '{}')".format(
        serial_id,
        date,
        f1_slope,
        f1_r,
        b1_slope,
        b2_r,
        f2_slope,
        f2_r,
        b2_slope,
        b2_r,
        notes) )

    def insert_robot_friction( self, 
                               serial_id, 
                               date, 
                               motor_num, 
                               direction,
                               angle,
                               value ):
        self.cursor.execute("INSERT INTO static_friction_tests "
            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(
                serial_id,
                date,
                motor_num,
                direction,
                angle,
                value))

    def check_robot_exists(self, linkbot):
        self.cursor.execute(
            'SELECT * FROM robot_type WHERE Id=\'{}\''.format(
                linkbot.serial_id) )
        rows = self.cursor.fetchall()
        formFactor = None
        if linkbot.form_factor() == linkbot3.FormFactor.I:
            formFactor = "Linkbot-I"
        elif linkbot.form_factor() == linkbot3.FormFactor.L:
            formFactor = "Linkbot-L"
        else:
          formFactor = "UNKNOWN"
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        if len(rows) == 0:
            self.cursor.execute('INSERT INTO robot_type VALUES(\'{}\', \'{}\')'.format(
                linkbot.serial_id, formFactor))

    def fetch_all(self, sql_statement):
        self.cursor.execute(sql_statement)
        return self.cursor.fetchall()
                
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.con.commit()
        self.con.close()


