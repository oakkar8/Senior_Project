import sys
import os

sys.path.insert(0, os.path.abspath('.'))

from gplaycli import gplaycli
gpc = gplaycli.GPlaycli()

token_url = "https://matlink.fr/token/email/gsfid"

def test_default_settings():
	assert gpc.yes == False
	assert gpc.verbose == False
	assert gpc.progress_bar == False
	assert gpc.device_codename == 'bacon'

def test_connection_credentials():
	try: # You are travis
		if os.environ['TRAVIS_PULL_REQUEST'] != "false": # If current job is a Pull Request
			print("Job is pull request. Won't check credentials")
			return
	except KeyError: # You are not travis
		pass
	gpc.token_enable = False
	gpc.creds['gmail_address']  = os.environ['GMAIL_ADDR']
	gpc.creds['gmail_password'] = os.environ['GMAIL_PWD']
	success, error = gpc.connect()
	assert error is None
	assert success == True

def test_connection_token():
	gpc.token_enable = True
	gpc.token_url = token_url
	gpc.retrieve_token(force_new=True)
	success, error = gpc.connect()
	assert error is None
	assert success == True

def test_download_focus():
	gpc.progress_bar = True
	gpc.download_folder = os.path.abspath('.')
	gpc.download(['org.mozilla.focus'])
