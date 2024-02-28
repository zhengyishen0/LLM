from google.cloud import storage


def upload_blob(file_name, bucket_name="whisper_salt_project", blob_name=None):
    """Uploads a file to the bucket."""
    blob_name = blob_name or file_name.split("/")[-1]
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_name)
    blob.make_public()
    print(f"File {file_name} uploaded to {blob_name}.")

    return blob.public_url
