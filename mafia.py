import smtplib
import random 
gmail_user = 'gamesatiitropar@gmail.com'
gmail_password = 'collegesux'

sent_from = gmail_user

numOfVill = 0
numOfMaf = 2
numOfThief = 1
numOfAngel = 1
numOfDet = 1

agents = []
for i in range(numOfVill):
    agents.append('Villager')

for i in range(numOfMaf):
    agents.append('Mafia')

for i in range(numOfThief):
    agents.append('Thief')

for i in range(numOfAngel):
    agents.append('Angel')

for i in range(numOfDet):
    agents.append('Detective')

players = [
    '2018csb1075@iitrpr.ac.in',
    # '2018ceb1019@iitrpr.ac.in',
    # '2018ceb1006@iitrpr.ac.in',
    # '2018csb1107@iitrpr.ac.in',
    # '2018csb1082@iitrpr.ac.in',
    # '2018ceb1002@iitrpr.ac.in',
    # '2018meb1234@iitrpr.ac.in',
]

random.shuffle(agents)
print(agents)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    subject = "Welcome to Mafia"

    for i in range(len(players)):
        to = ['2018csb1075@iitrpr.ac.in']
        body = "Your Role is " + agents[i]

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)
        smtp_server.sendmail(sent_from, to, email_text)
        print ("Email sent to  " + players[i] + "successfully! with role " + agents[i])
    smtp_server.close()
    
except Exception as ex:
    print ("Something went wrong….",ex)
