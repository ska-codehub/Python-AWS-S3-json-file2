from s3 import AwsS3
import traceback

if __name__ == "__main__":
    try:
        aws_s3 = AwsS3()
        aws_s3.download_files()
    except Exception as e:
        print(f"Error in __main__: {e}", traceback.format_exc())