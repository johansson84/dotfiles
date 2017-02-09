#!/usr/bin/python

#https://jira.fnox.se/rest/agile/1.0/board/89/sprint/
#https://jira.fnox.se/rest/agile/1.0/board/89/sprint/xxx/issue

#Content-Type   application/json
#Accept         application/json
#Authorization  Basic dmljdG9yLmpvaGFuc3NvbjpwUmFZYWRST1NU

import requests
import json

headers = {
	'Content-Type': 'application/json',
	'Accept': 'application/json',
	'Authorization': 'Basic dmljdG9yLmpvaGFuc3NvbjpwUmFZYWRST1NU'
}

def getBoard():
	url = 'https://jira.fnox.se/rest/agile/1.0/board/'
	r = requests.get(url, headers=headers)
	boardData = json.loads(r.text)

	for board in boardData['values']:
		if board['name'] == 'Team OOF':
			boardId = board['id']
			break

	return boardId

def getLastSprint(board):
	startAt = 0

	while True:
			url = 'https://jira.fnox.se/rest/agile/1.0/board/' + str(board) + '/sprint/?startAt=' + str(startAt)
			r = requests.get(url, headers=headers)
			sprintData = json.loads(r.text)
			if sprintData['isLast'] == True:
				break
			startAt = startAt + int(sprintData['maxResults'])

	activeSprint = sprintData['values'][-1]

	return {'id': activeSprint['id'], 'endDate': activeSprint['endDate']}

def getSprintIssues(sprint):
	payload = {'fields': 'resolution,status,project'}
	url = 'https://jira.fnox.se/rest/agile/1.0/board/' + str(board) + '/sprint/' +str(sprint) + '/issue'
	r = requests.get(url, headers=headers, params=payload)
	issueData = json.loads(r.text)

	return issueData

def formatOutput(issues, endDate):
	total = issues['total']
	totalLive = 0
	closedLive = 0
	closedOOF = 0

	for issue in issues['issues']:
		status = issue['fields']['status']['name']
		project = issue['fields']['project']['key']
		if status == 'Closed' or status == 'Rejected':
			if project == 'LIVE':
				closedLive = closedLive + 1
			else:
				closedOOF = closedOOF + 1
		if project == 'LIVE':
			totalLive = totalLive + 1

	totalOOF = total - totalLive

	output = {
		'OOF': {
			'Total_OOF': total - totalLive,
			'Closed_OOF': closedOOF,
			'Open_OOF': totalOOF - closedOOF
		},
		'LIVE': {
			'Total_LIVE': totalLive,
			'Closed_LIVE': closedLive,
			'Open_LIVE': totalLive - closedLive
		},
		'Total': total,
		'EndDate': endDate
	}

	return json.dumps(output, sort_keys=True)

board = getBoard()
sprint = getLastSprint(board)
issues = getSprintIssues(sprint['id'])
output = formatOutput(issues, sprint['endDate'])

print(output)
