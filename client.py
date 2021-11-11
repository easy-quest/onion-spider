import os
from supabase_py import create_client, Client

url: str = os.environ.get("SUPABASE_TEST_URL")
key: str = os.environ.get("SUPABASE_TEST_KEY")
supabase: Client = create_client(url, key)
user = supabase.auth.sign_up(
    email='example@email.com',
    password='example-password',
)
###
import os
from supabase_py import create_client, Client

url: str = os.environ.get("SUPABASE_TEST_URL")
key: str = os.environ.get("SUPABASE_TEST_KEY")
supabase: Client = create_client(url, key)
user = supabase.auth.sign_in(
    email='example@email.com',
    password='example-password'
)

###
import os
from supabase_py import create_client, Client

url: str = os.environ.get("SUPABASE_TEST_URL")
key: str = os.environ.get("SUPABASE_TEST_KEY")
supabase: Client = create_client(url, key)

data = supabase.table('countries').select('name').execute()

###
data = supabase.table('cities').insert({'name': 'Gotham', 'country_id': 556 }).execute()
# assert if insert response is a success
assert data.get("status_code") in (200, 201)

# bulk insert 
data = supabase.table('cities').insert([
{'name': 'Gotham', 'country_id': 556 },
{'name': 'The Shire', 'country_id': 557 }
]).execute()
