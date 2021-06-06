import dropbox
class TransferData :
    def __init__(self,access_token):
             self.access_token=access_token
    def upload_files(self,file_from,file_to):
            dbx=dropbox.Dropbox(self.access_token)
            f=open(file_from,'rb')
            dbx.files_upload(f.read(), file_to)
def main ():
    access_token='lYZF9tvn6XIAAAAAAAAAAfJlIZ-SDlFJqM4OyXYX76uHKlElMm12_XPiSHWctyVz'
    transferdata=TransferData(access_token)
    file_from=input("enter file path to transfer")
    file_to=input("enter file path to upload")
    transferdata.upload_files(file_from,file_to)
    print("file has been moved")

main()