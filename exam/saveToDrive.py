from google import drive_service 
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client_secret_googleCloudDemo.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = drive_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '1hnJJMZuuWkcbzZ0x-7FbZrCrNo2OmE7U'
file_names = 'realText.txt'
mime_types = 'text/plain'

# for file_name, mime_type in zip(file_names, mime_types):
#     # file_metadata = {
#     #     'name': file_name,
#     #     'parents':[folder_id],
#     # }
#     # media = MediaFileUpload('./saveToDriveProj/{0}'.format(file_name), minetype=mime_type )

#     service.files().create(
#         body = file_metadata,
#         media_body = media,
#         fields = 'id'
        
#     ).execute()

file_metadata = {'name': file_names}
media = MediaFileUpload('saveToDriveProj/realText.txt', mimetype=mime_types)
file = drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
# print 'File ID: %s' % file.get('id')


