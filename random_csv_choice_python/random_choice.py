import os
import csv
import random
import string

filename = 'choices.csv'
 #filepath to open

def get_file_path(filename):
	currentdirpath = os.getcwd()
	file_path = os.path.join(os.getcwd(), filename)
	return file_path

path = get_file_path(filename)

def get_random_sting():
	rnstring = ''
	for i in range(0,4):
		rnstring += random.choice(string.ascii_letters)
	return rnstring
	
def read_csv(filepath):
	with open(filepath, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if not "Email Address" in row:
				email, domain = row[0].split('@')
				print email, domain
				fake_email = email[:4] + get_random_sting() + "@" + domain
				print fake_email

read_csv(path)