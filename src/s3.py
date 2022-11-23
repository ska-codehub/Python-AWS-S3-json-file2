import json
import boto3
from multithread import MultiThread
import configparser
from queue import LifoQueue
from pathlib import Path

config = configparser.RawConfigParser()

config.read("config.properties")
AWS = dict(config.items("AWS"))
S3 = dict(config.items("S3"))
SETTINGS = dict(config.items("SETTINGS"))

filetypestobedownloaded = SETTINGS.get('filetypestobedownloaded').strip().split(",")
io_path = Path(SETTINGS.get("io"))
io_path.mkdir(exist_ok=True)

class AwsS3(object):
    def __init__(self) -> None:
        self.session = boto3.Session(
            aws_access_key_id=AWS.get("accesskeyid").strip(), 
            aws_secret_access_key=AWS.get("secretaccesskey").strip(), 
            region_name=AWS.get("region").strip()
        )
        self.s3 = self.session.resource("s3", region_name=S3.get("region").strip())
        self.queue = LifoQueue(maxsize=5000)

    def _download_single_file(self, bucket: object, prefix: any=None):
        for obj in bucket.objects.filter(Prefix=prefix):
            try:
                filename = obj.key
                print(f"Processing filename: {filename}")
                extension = filename.split(".")[-1]
                if extension not in filetypestobedownloaded:
                    print(f"Skiping {filename} as the extension doesn't fall under given File Types: {', '.join(filetypestobedownloaded)}")
                    continue
                file_obj = obj.get()
                body_obj = file_obj['Body']
                content = body_obj.read().decode("UTF-8")
                try:
                    if extension=='json':
                        json_content = json.loads(content) # Checking if file content is in proper JSON format
                    with open(file= io_path / filename, mode="w") as f:
                        f.write(content)
                    print(f"File with filename({filename}) downloaded in {io_path}")
                except json.decoder.JSONDecodeError:
                    print(f"Error in _download_single_file: Content of the file({filename}) is not in proper JSON format")        
                except Exception as e:
                    print(f"File with filename({filename}) failed to be downloaded in {io_path}")
            except Exception as e:
                print(f"Error in _download_single_file: {e}")

    def _download_files(self, bucket_name: str, prefixes: list) -> object:
        bucket = self.s3.Bucket(bucket_name)
        for prefix in prefixes:
            try:
                print(f"Processing Bucket Name: {bucket_name} Prefix: {prefix}")
                self.queue.put(prefix, block=True, timeout=None)   
                thread = MultiThread(
                            queue=self.queue, 
                            func=lambda: self._download_single_file(
                                                bucket=bucket,
                                                prefix=prefix
                                            )
                            )
                thread.start()
            except Exception as e:
                print(f"Error in _download_files: {e}")


    
    def download_files(self) -> None:
        print("Starting Download....")
        bucketnames = S3.get("bucketnames").strip().split("|")
        prefixes = S3.get("prefixes").strip().split("|")
        bucket_prefixes = dict(zip(bucketnames, [p.strip().split(",") for p in prefixes]))
        for bucket_name, prefixes in bucket_prefixes.items():
            print(f"Bucket Name: {bucket_name} Prefixes: {', '.join(prefixes)}")
            self.queue.put(bucket_name, block=True, timeout=None)
            thread = MultiThread(
                        queue=self.queue, 
                        func=lambda: self._download_files(
                                            bucket_name=bucket_name,
                                            prefixes=prefixes
                                        )
                        )
            thread.start()
        self.queue.join()
        print("Completed!")
