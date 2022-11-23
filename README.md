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