import datetime as dt
from datetime import timedelta
import pymysql

db = pymysql.connect(
    host="",
    user="",
    password="",
    database="",
    port=3306
    )

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE stockdatabase")
# mycursor.execute("SHOW TABLES FROM stockdatabase")
# mycursor.execute("CREATE TABLE NYSE_Threshold_Securities (Symbol VARCHAR(6) NOT NULL, Security_Name VARCHAR(200) NOT NULL, Trade_Date DATE NOT NULL, Market VARCHAR(20) NOT NULL)")
# mycursor.execute("CREATE TABLE Short_Sale_Volume (Date_Posted DATE NOT NULL, Symbol VARCHAR(6) NOT NULL, Short_Sale_Volume INT NOT NULL, Short_Exempt_Volume INT NOT NULL, Total_Volume INT NOT NULL, Market VARCHAR(20))")
# mycursor.execute("CREATE TABLE active_stock_posts (post_ID VARCHAR(20) NOT NULL UNIQUE, stock VARCHAR(6) NOT NULL, 1st_previous INT NOT NULL, 2nd_previous INT NOT NULL, 3rd_previous INT NOT NULL, 4th_previous INT NOT NULL)")
# mycursor.execute("INSERT INTO NYSE_Threshold_Securities (Symbol, Security_Name, Trade_Date, Market) VALUES(%s,%s,%s,%s)", mylist)
# mycursor.execute("INSERT INTO active_stock_posts (post_ID, 1st_previous, 2nd_previous, 3rd_previous, 4th_previous) VALUES(%s,%s,%s,%s,%s,%s)", IDList5)

# mycursor.execute("ALTER TABLE active_stock_posts CHANGE hour13ups hour12ups INT NOT NULL")

# mycursor.execute("DELETE FROM NYSE_Threshold_Securities")
# mycursor.execute("DELETE FROM Short_Sale_Volume")
# mycursor.execute("SELECT * FROM active_stock_posts WHERE post_ID='ccc333'")
# mycursor.execute("ALTER TABLE active_stock_posts DROP COLUMN hour19")
# mycursor.execute("CREATE TABLE stock_interactions (dtAdded DATETIME NOT NULL, stock VARCHAR(6), ups INT NOT NULL, coms INT NOT NULL)")
# mycursor.execute("CREATE TABLE stock_mentions (dtAdded DATE NOT NULL, stock VARCHAR(6), mentions INT NOT NULL)")
mycursor.execute("DESCRIBE stock_mentions")

#------------------------------------------------------------------

# now = dt.datetime.now()
# oneHourAgo = now - timedelta(hours=1)
# twoHoursAgo = now - timedelta(hours=2)
# threeHoursAgo = now - timedelta(hours=3)
# fourHoursAgo = now - timedelta(hours=4)

# firstPrevDigit = now.strftime("%H")
# secondPrevDigit = oneHourAgo.strftime("%H")
# thirdPrevDigit = twoHoursAgo.strftime("%H")
# fourthPrevDigit = threeHoursAgo.strftime("%H")
# fifthPrevDigit = fourHoursAgo.strftime("%H")

# firstPrevUps = 'hour' + firstPrevDigit + 'ups'
# secondPrevUps = 'hour' + secondPrevDigit + 'ups'
# thirdPrevUps = 'hour' + thirdPrevDigit + 'ups'
# fourthPrevUps = 'hour' + fourthPrevDigit + 'ups'
# fifthPrevUps = 'hour' + fifthPrevDigit + 'ups'

# firstPrevComs = 'hour' + firstPrevDigit + 'coms'
# secondPrevComs = 'hour' + secondPrevDigit + 'coms'
# thirdPrevComs = 'hour' + thirdPrevDigit + 'coms'
# fourthPrevComs = 'hour' + fourthPrevDigit + 'coms'
# fifthPrevComs = 'hour' + fifthPrevDigit + 'coms'

# mycursor.execute("ALTER TABLE active_stock_posts DROP COLUMN delta")
# mycursor.execute("ALTER TABLE active_stock_posts DROP COLUMN newUps")
# mycursor.execute("ALTER TABLE active_stock_posts DROP COLUMN newComs")
# #------------------------------------------------------------------------
# adds a zeroed column for the new scrape

# mycursor.execute("ALTER TABLE active_stock_posts ADD COLUMN %s INT NOT NULL" \
#                  % (firstPrevUps))

# mycursor.execute("ALTER TABLE active_stock_posts ADD COLUMN %s INT NOT NULL" \
#                  % (firstPrevComs))
# #------------------------------------------------------------------------
# #deletes the 5 hour column that we no longer need

# mycursor.execute("ALTER TABLE active_stock_posts DROP COLUMN %s" \
# 	             % (fifthPrevUps))

# mycursor.execute("ALTER TABLE active_stock_posts DROP COLUMN %s" \
# 	             % (fifthPrevComs))
# #-------------------------------------------------------------------------
# inserts new row for newID if it is new to db

# for post in post_ID_list:

# 	mycursor.execute("INSERT IGNORE INTO active_stock_posts(post_ID,stock)\
# 		             VALUES(%s,%s)", (post[0],post[1]))

# 	mycursor.execute("UPDATE active_stock_posts SET %s = %s WHERE post_ID = '%s'" \
# 	       % (firstPrevUps, post[2], post[0]))

# 	mycursor.execute("UPDATE active_stock_posts SET %s = %s WHERE post_ID = '%s'" \
# 	       % (firstPrevComs, post[3], post[0]))
# #-------------------------------------------------------------------------
# adds delta column and deletes posts that havent been interacted with

# mycursor.execute("ALTER TABLE active_stock_posts ADD COLUMN delta DOUBLE\
# 	             GENERATED ALWAYS AS\
# 	             (abs(%s-%s)\
# 	             +abs(%s-%s)\
# 	             +abs(%s-%s)) STORED"\
#                % (firstPrevUps,secondPrevUps,secondPrevUps,thirdPrevUps,thirdPrevUps,fourthPrevUps))

# mycursor.execute("ALTER TABLE active_stock_posts ADD COLUMN newUps DOUBLE\
# 	             GENERATED ALWAYS AS\
# 	             (%s-%s) STORED"\
#                % (firstPrevUps,secondPrevUps))

# mycursor.execute("ALTER TABLE active_stock_posts ADD COLUMN newComs DOUBLE\
# 	             GENERATED ALWAYS AS\
# 	             (%s-%s) STORED"\
#                % (firstPrevComs,secondPrevComs))

# mycursor.execute("DELETE FROM active_stock_posts WHERE delta = 0")