# *Python-AWS-S3-json-file2*

## Client

Yaki Noe

## Repo owner or admin

Sk Khurshid Alam

## Dependencies 

* [**Python 3.9**](https://www.python.org/downloads/release/python-3911/) 
* <a id="packages"></a> Python Packages:

    ```bash
        boto3==1.26.14
        botocore==1.29.14
        jmespath==1.0.1
        python-dateutil==2.8.2
        s3transfer==0.6.0
        six==1.16.0
        urllib3==1.26.12
    ```

## Local Setup of Environment and Run Utility

### Configure the *src > config.properties*

#### Configure *AWS* section
* Set AccessKeyID to *Your AWS Access Key ID*
* Set SecretAccessKey to *Your AWS Secret Access Key*
* Region to *Your AWS Region*

#### Configure *S3* section
* Set Region to *Your AWS S3 Region*
* Set BucketNames to *Your AWS S3 Bucket Name/s* <br>
**Note: You can use multiple bucket names with '|' seperated delimeter**
* Set Prefixes to *Your AWS S3 Object Prefix/es* <br>
**Note: You can use multiple prefix items with '|' seperated delimeter, and for each item you can further user ',' seperated prefix for corresponding bucket**


#### Configure *SETTINGS* section
* Set IO to *Input/Output folder* for storing the downloaded files
* Set FileTypesToBeDownloaded to the *File Types which need to be downloaded* from S3 <br>
**Note: You can use multiple file types with ',' seperated delimeter**

#### For your reference please go through *example1-config.properties*, *example2-config.properties*, *example3-config.properties* to have more clarity.

### Unix Setup

#### If pip is not in your system install pip

```bash
sudo apt-get install -y python3-pip
```

#### Install series of packages to make your programming environment more consistent

```bash
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
```

#### Install virtualenv

##### <a id="virtualenv"></a> Either

```bash
pip3 install virtualenv
```

##### <a id="venv"></a> OR

```bash
sudo apt-get install -y python3-venv
```

#### Navigate to Python-AWS-S3-json-file2 folder in terminal

```bash
cd <parent dir>/Python-AWS-S3-json-file2
```

#### Create virtual environment

##### [Either with](#virtualenv)

```bash
virtualenv -p python3 venv
```

##### [OR with](#venv)

```bash
python3 -m venv venv
```

#### <a id="activate-venv"></a>Activate virtual environment

```bash
source venv/bin/activate
```

#### <a id="requirements"></a> Install python packages using [*requirements.txt*](#packages) file

```bash
pip install -r requirements.txt
```

#### Navigate to *src* folder in terminal

```bash
cd src
```

***

## Python Command to run the utility
**NOTE: [*Activate virtual environment*](#activate-venv) each time while running the below command**

```bash
    python main.py
```