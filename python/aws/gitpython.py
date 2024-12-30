from git import Repo
import zipfile
import pathlib
import boto3
    

def main():

    #repo = Repo.clone_from('git@ssh.dev.azure.com:v3/trungtinzz/cicd-integration/cicd-integration',
    #                       './cicd-integration', branch='main')
    
    # Build zip file from multiple files
    files = ["ec2.py", "s3.py"]
    with zipfile.ZipFile("files.zip", mode="w") as archive:
        for filename in files:
            archive.write(filename)

    try:
        with zipfile.ZipFile("files.zip") as archive:
            archive.printdir()
    except zipfile.BadZipFile as error:
        print(error)
    
    s3 = boto3.client('s3')

    # This command = aws s3 cp files.zip s3://tin-tf-bucket-01/files-cp, which will keep the file as correct .ZIP 
    res = s3.put_object(Bucket='tin-tf-bucket-01',
            Key="files-boto",
            Body=open("files.zip", 'rb'),
            ContentType='application/zip'
        )

#    # Build zip file from a directory
#    directory = pathlib.Path("./cicd-integration/")
#    with zipfile.ZipFile("directory.zip", mode="w") as archive:
#        for file_path in directory.iterdir():
#            archive.write(file_path, arcname=file_path.name)
#    with zipfile.ZipFile("directory.zip", mode="r") as archive:
#        archive.printdir()

    return 1

main()

