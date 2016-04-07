import urllib2
import re
import csv
import MySQLdb

teamWebsites = ['http://www.dougstats.com/15-16RD.Team.txt',
				'http://www.dougstats.com/15-16.HomeRD.Team.txt',
				'http://www.dougstats.com/15-16.AwayRD.Team.txt',
				'http://www.dougstats.com/15-16RD.Team.Opp.txt',
				'http://www.dougstats.com/15-16.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/15-16.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/14-15RD.Team.txt',
				'http://www.dougstats.com/14-15.HomeRD.Team.txt',
				'http://www.dougstats.com/14-15.AwayRD.Team.txt',
				'http://www.dougstats.com/14-15RD.Team.Opp.txt',
				'http://www.dougstats.com/14-15.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/14-15.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/13-14RD.Team.txt',
				'http://www.dougstats.com/13-14.HomeRD.Team.txt',
				'http://www.dougstats.com/13-14.AwayRD.Team.txt',
				'http://www.dougstats.com/13-14RD.Team.Opp.txt',
				'http://www.dougstats.com/13-14.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/13-14.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/12-13RD.Team.txt',
				'http://www.dougstats.com/12-13.HomeRD.Team.txt',
				'http://www.dougstats.com/12-13.AwayRD.Team.txt',
				'http://www.dougstats.com/12-13RD.Team.Opp.txt',
				'http://www.dougstats.com/12-13.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/12-13.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/11-12RD.Team.txt',
				'http://www.dougstats.com/11-12.HomeRD.Team.txt',
				'http://www.dougstats.com/11-12.AwayRD.Team.txt',
				'http://www.dougstats.com/11-12RD.Team.Opp.txt',
				'http://www.dougstats.com/11-12.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/11-12.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/10-11RD.Team.txt',
				'http://www.dougstats.com/10-11.HomeRD.Team.txt',
				'http://www.dougstats.com/10-11.AwayRD.Team.txt',
				'http://www.dougstats.com/10-11RD.Team.Opp.txt',
				'http://www.dougstats.com/10-11.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/10-11.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/09-10RD.Team.txt',
				'http://www.dougstats.com/09-10.HomeRD.Team.txt',
				'http://www.dougstats.com/09-10.AwayRD.Team.txt',
				'http://www.dougstats.com/09-10RD.Team.Opp.txt',
				'http://www.dougstats.com/09-10.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/09-10.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/08-09RD.Team.txt',
				'http://www.dougstats.com/08-09.HomeRD.Team.txt',
				'http://www.dougstats.com/08-09.AwayRD.Team.txt',
				'http://www.dougstats.com/08-09RD.Team.Opp.txt',
				'http://www.dougstats.com/08-09.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/08-09.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/07-08RD.Team.txt',
				'http://www.dougstats.com/07-08.HomeRD.Team.txt',
				'http://www.dougstats.com/07-08.AwayRD.Team.txt',
				'http://www.dougstats.com/07-08RD.Team.Opp.txt',
				'http://www.dougstats.com/07-08.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/07-08.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/06-07RD.Team.txt',
				'http://www.dougstats.com/06-07.HomeRD.Team.txt',
				'http://www.dougstats.com/06-07.AwayRD.Team.txt',
				'http://www.dougstats.com/06-07RD.Team.Opp.txt',
				'http://www.dougstats.com/06-07.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/06-07.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/05-06RD.Team.txt',
				'http://www.dougstats.com/05-06.HomeRD.Team.txt',
				'http://www.dougstats.com/05-06.AwayRD.Team.txt',
				'http://www.dougstats.com/05-06RD.Team.Opp.txt',
				'http://www.dougstats.com/05-06.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/05-06.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/04-05RD.Team.txt',
				'http://www.dougstats.com/04-05.HomeRD.Team.txt',
				'http://www.dougstats.com/04-05.AwayRD.Team.txt',
				'http://www.dougstats.com/04-05RD.Team.Opp.txt',
				'http://www.dougstats.com/04-05.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/04-05.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/03-04RD.Team.txt',
				'http://www.dougstats.com/03-04.HomeRD.Team.txt',
				'http://www.dougstats.com/03-04.AwayRD.Team.txt',
				'http://www.dougstats.com/03-04RD.Team.Opp.txt',
				'http://www.dougstats.com/03-04.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/03-04.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/02-03RD.Team.txt',
				'http://www.dougstats.com/02-03.HomeRD.Team.txt',
				'http://www.dougstats.com/02-03.AwayRD.Team.txt',
				'http://www.dougstats.com/02-03RD.Team.Opp.txt',
				'http://www.dougstats.com/02-03.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/02-03.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/01-02RD.Team.txt',
				'http://www.dougstats.com/01-02.HomeRD.Team.txt',
				'http://www.dougstats.com/01-02.AwayRD.Team.txt',
				'http://www.dougstats.com/01-02RD.Team.Opp.txt',
				'http://www.dougstats.com/01-02.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/01-02.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/00-01RD.Team.txt',
				'http://www.dougstats.com/00-01.HomeRD.Team.txt',
				'http://www.dougstats.com/00-01.AwayRD.Team.txt',
				'http://www.dougstats.com/00-01RD.Team.Opp.txt',
				'http://www.dougstats.com/00-01.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/00-01.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/99-00RD.Team.txt',
				'http://www.dougstats.com/99-00.HomeRD.Team.txt',
				'http://www.dougstats.com/99-00.AwayRD.Team.txt',
				'http://www.dougstats.com/99-00RD.Team.Opp.txt',
				'http://www.dougstats.com/99-00.HomeRD.Team.Opp.txt',
				'http://www.dougstats.com/99-00.AwayRD.Team.Opp.txt',
				'http://www.dougstats.com/98-99RD.Team.txt',
				'http://www.dougstats.com/98-99RD.Team.Opp.txt',
				'http://www.dougstats.com/97-98RD.Team.txt',
				'http://www.dougstats.com/97-98RD.Team.Opp.txt']

teamHTMLs =	   ['http://www.dougstats.com/96-97RD.Team.html',
				'http://www.dougstats.com/96-97RD.Team.Opp.html',
				'http://www.dougstats.com/95-96RD.Team.html',
				'http://www.dougstats.com/95-96RD.Team.Opp.html',
				'http://www.dougstats.com/94-95RD.Team.html',
				'http://www.dougstats.com/94-95RD.Team.Opp.html',
				'http://www.dougstats.com/93-94RD.Team.html',
				'http://www.dougstats.com/93-94RD.Team.Opp.html',
				'http://www.dougstats.com/92-93RD.Team.html',
				'http://www.dougstats.com/92-93RD.Team.Opp.html',
				'http://www.dougstats.com/91-92RD.Team.html',
				'http://www.dougstats.com/91-92RD.Team.Opp.html',
				'http://www.dougstats.com/90-91RD.Team.html',
				'http://www.dougstats.com/90-91RD.Team.Opp.html',
				'http://www.dougstats.com/89-90RD.Team.html',
				'http://www.dougstats.com/89-90RD.Team.Opp.html',
				'http://www.dougstats.com/88-89RD.Team.html',
				'http://www.dougstats.com/88-89RD.Team.Opp.html']


def teamTable(filename):
	mydb = MySQLdb.connect(host = 'server', user = 'username', passwd = '********', db = 'sys')
	cursor = mydb.cursor()
	csv_data = csv.reader(file(filename))
	cursor.execute('DROP TABLE IF EXISTS `'+filename[:-4]+'`')
	create = """CREATE TABLE """+filename[:-4]+""" (
				team VarChar(20) PRIMARY KEY, games_won INT, 
				games_lost INT, minutes INT, fg_made INT, fg_attempts INT, 3s_made INT, 
				3s_attempts INT, ft_made INT, ft_attempts INT, off_rebounds INT, 
				tot_rebounds INT, assists INT, steals INT, turnovers INT, blocks INT, 
				personal_fouls INT, points INT, technicals INT, ejections INT, 
				flagrant_fouls INT)"""
	cursor.execute(create)
	count = 0
	for row in csv_data:
		insert = """INSERT INTO """+filename[:-4]+"""(team, games_won,
					games_lost, minutes, fg_made, fg_attempts, 3s_made, 3s_attempts, 
					ft_made, ft_attempts, off_rebounds, tot_rebounds, assists, steals,
					turnovers, blocks, personal_fouls, points, technicals, ejections,
					flagrant_fouls)
					VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
					%s, %s, %s, %s, %s, %s)"""
		cursor.execute(insert, row)
		count += 1
	mydb.commit()
	cursor.close()

def oldTeamTable(filename):
	mydb = MySQLdb.connect(host = 'server', user = 'username', passwd = '*********', db = 'sys')
	cursor = mydb.cursor()
	csv_data = csv.reader(file(filename))
	cursor.execute('DROP TABLE IF EXISTS `'+filename[:-4]+'`')
	create = """CREATE TABLE """+filename[:-4]+""" (
				team VarChar(20) PRIMARY KEY, games_won INT, 
				games_lost INT, minutes INT, fg_made INT, fg_attempts INT, 3s_made INT, 
				3s_attempts INT, ft_made INT, ft_attempts INT, off_rebounds INT, 
				tot_rebounds INT, assists INT, steals INT, turnovers INT, blocks INT, 
				personal_fouls INT, points INT)"""
	cursor.execute(create)
	count = 0
	for row in csv_data:
		insert = """INSERT INTO """+filename[:-4]+"""(team, games_won,
					games_lost, minutes, fg_made, fg_attempts, 3s_made, 3s_attempts, 
					ft_made, ft_attempts, off_rebounds, tot_rebounds, assists, steals,
					turnovers, blocks, personal_fouls, points)
					VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
					%s, %s, %s)"""
		cursor.execute(insert, row)
		count += 1
	mydb.commit()
	cursor.close()

for n in range(len(teamWebsites)):
	filename = teamWebsites[n][25:]
	filename = filename[:-4]
	filename = filename.replace('.', '').replace('-', '')+'.csv'
	output = open(filename, "w")
	first_line = 1
	count = 0  
	for line in urllib2.urlopen(teamWebsites[n]):
		if first_line == 0:
			row = ''
			for word in line.split():
				'''if word in teamAbbr:
					row = row+teamAbbr[word]+','+word+','
				else:'''
				row = row+word+','
			output.write(row[:-1]+'\n')
			count += 1
		if count == 30:
			break	 
		first_line = 0
	output.close()
	teamTable(filename)

for n in range(len(teamHTMLs)):
	filename = teamHTMLs[n][25:]
	filename = filename[:-5]
	filename = filename.replace('.', '').replace('-', '')+'.csv'
	output = open(filename, "w")
	count = 0
	for line in urllib2.urlopen(teamHTMLs[n]):
		if len(line) > 7:
			if first_line <= 0:
				row = ''
				c = 0
				for word in line.split():
					if c < 18:
						row = row+word+','
					c+=1	
				output.write(row[:-1]+'\n')
				count+=1
			if count == 30:
				break
	output.close()
	oldTeamTable(filename)	
