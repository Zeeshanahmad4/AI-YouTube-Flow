from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import mimetypes

def get_drive_service():
    """
    Creates a service object for Google Drive API

    :return: Google Drive service object
    """
    # Path to the service account credentials file
    SERVICE_ACCOUNT_FILE = 'path/to/service_account.json'

    # Define the scopes required
    SCOPES = ['https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        SERVICE_ACCOUNT_FILE, SCOPES)
    
    # Build the service object for the Drive API
    service = build('drive', 'v3', credentials=credentials)
    return service

def upload_file_to_drive(service, file_path, folder_id=None):
    """
    Uploads a file to Google Drive

    :param service: Google Drive service object
    :param file_path: Path of the file to be uploaded
    :param folder_id: ID of the Drive folder to upload the file to (optional)
    :return: File ID of the uploaded file
    """
    file_metadata = {'name': os.path.basename(file_path)}
    if folder_id:
        file_metadata['parents'] = [folder_id]

    mime_type = mimetypes.guess_type(file_path)[0] or 'application/octet-stream'
    media = MediaFileUpload(file_path, mimetype=mime_type)

    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()
    return file.get('id')

# Example usage
if __name__ == '__main__':
    drive_service = get_drive_service()
    file_path = 'path/to/your/file.mp4'  # Replace with the path to your video file
    uploaded_file_id = upload_file_to_drive(drive_service, file_path)
    print(f'File uploaded successfully, File ID: {uploaded_file_id}')

