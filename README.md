# Onion spider

## How to run
```
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
python parser.py
```
```
import os
from supabase_py import create_client, Client

url: str = os.environ.get("SUPABASE_TEST_URL")
key: str = os.environ.get("SUPABASE_TEST_KEY")
supabase: Client = create_client(url, key)
user = supabase.auth.sign_up(
    email='example@email.com',
    password='example-password',
)
```