import botocore, boto3, os, logging, json
import zipfile, pathlib

# Add this line before importing git to avoid error "Bad git executable"
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import git

# Define Git executable to use from git-lambda layer
os.environ["GIT_PYTHON_GIT_EXECUTABLE"] = "/opt/bin/git"

# Init logger
logging.basicConfig(format="[%(levelname)s]\t%(message)s",level=logging.INFO)
logger = logging.getLogger()


# Clone git repository and upload repo zip to S3
def cloneRepo(sourceRepo:str, downloadDir:str, branch:str, bucket:str):
  try:
    git.Repo.clone_from(sourceRepo, downloadDir, branch=branch)
    logger.info(f"Repo cloned to {downloadDir}")
    #os.system(f'/bin/ls {downloadDir}/')
    os.system(f'rm -rf {downloadDir}/.git*')
  except Exception as e:
      logger.info(f"Function get error at: {e}")

  # Build zip file from a directory
  directory = pathlib.Path(downloadDir)
  with zipfile.ZipFile(f"{downloadDir}.zip", mode="w") as archive:
    for file_path in directory.rglob("*"):
      archive.write(file_path, arcname=file_path.relative_to(directory))
  with zipfile.ZipFile(f"{downloadDir}.zip", mode="r") as archive:
      archive.printdir()

  # Upload zip file to S3
  s3_upload = boto3.client('s3').put_object(
      Bucket=bucket,
      Key="repositories",
      Body=f"{downloadDir}.zip",
      ContentType='application/zip'
  )
  logger.info(json.dumps(s3_upload))

  return {
      'statusCode': s3_upload['ResponseMetadata']['HTTPStatusCode'],
      'body': json.dumps(s3_upload)
  }


def main():
  ## Print all current Lambda layers
  #os.system('/bin/ls /opt/')
  ## Check PATH and GIT_PYTHON_GIT_EXECUTABLE to debug GitPython
  #print(os.environ["PATH"])
  #print(os.environ["GIT_PYTHON_GIT_EXECUTABLE"])
