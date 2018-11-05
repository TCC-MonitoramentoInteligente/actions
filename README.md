# Actions
Actions sends an e-mail with a print of the event.

# Setup
1. Create virtualenv `$ virtualenv --system-site-packages -p python3 venv`
2. Activate virtualenv `$ source venv/bin/activate`
3. Install requirements `$ pip install -r requirements.txt`
4. Set up boto3 authentication credentials, following the [Boto 3 Docs](https://boto3.readthedocs.io/en/latest/guide/quickstart.html#installation)
5. Set valid and verified (by Amazon SES) e-mail adress to sender and receiver
