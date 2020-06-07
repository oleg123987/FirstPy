def explicit():
    from google.cloud import storage

    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json(
        'My Project 10862-dbf121f12194.json')

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)



def explicit_compute_engine(project):
    from google.auth import compute_engine
    from google.cloud import storage

    # Explicitly use Compute Engine credentials. These credentials are
    # available on Compute Engine, App Engine Flexible, and Container Engine.
    credentials = compute_engine.Credentials()

    # Create the client using the credentials and specifying a project ID.
    storage_client = storage.Client(credentials=credentials, project=project)

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)