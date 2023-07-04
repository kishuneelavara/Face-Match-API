# ADB-OCR-API
This is a simple OCR (Optical Character Recognition) API created using Flask framework in Python. The API allows you to extract necessary information from different documents such as health, education and family Development.

## **Prerequisites**
    Python 3.7.9 installed on your system. use this [python 3.7.9 ](https://www.python.org/downloads/release/python-379/)
    Installation of all libraries mentioned in the requirements.txt file.


## **Installation**
###### 1 Clone this repository to your local machine or server.
    git clone <repository_url>

###### 2 Navigate to the project directory.
    cd ocr-api

###### 3 Create a virtual environment (optional but recommended).
    python3 -m venv <your_env_name>
    or 
    python -m venv <your_env_name>
    
###### 4 Activate the virtual environment.
    For Windows:
        `<your_env_name>\Scripts\activate`
        
    For Unix/macOS:
        `source venv/bin/activate`
        
###### 5 Install the required libraries using pip.
    pip install -r requirements.txt
    or 
    pip3 install -r requirements.txt


## **Usage**
###### Start the Flask server (or OCR API) by running the following command:
    python app.py
    
###### Once the server is running, you can access the API using the following URLs:
    Local: http://localhost:5003/extract_document_api
    This endpoint or API is now available to access in local


## **How to Deploy the API in AWS Windows EC2 Server**
1 Create a Windows EC2 server with required storage and with security group such as custom TCP and mention your Port in this case it is 5003 also add new rule such as RDP, HTTP and HTTPS.

2 Change setting in Windows Ec2 System - Windows Defender Firewall -> Advanced Setting -> Windows Defender Firewall properties => change inbound connection as Allow for all the 3 tabs such as domain, private , public

3 Change setting in Windows Ec2 System - Windows Defender Firewall -> Advanced Setting -> Inbound Rules -> New Rule -> Port -> Next -> Select TCP and Mention your specific local port (here its 5003) -> Next -> select Allow the Connection -> Next -> check all check box (Domain , Private, Public) -> Next -> Give name -> Finish

4 Once after creating ec2 server and after setting  Follow the above installation procedure and usage procedure to start the Flask Server or OCR API

5 Once the server is running, you can access the API using the following URLs:
###### 
    Public IP: http://<public_ip_of_ec2>:<portnumber>/extract_document_api
    Public IP with port 5003: http://<public_ip_of_ec2>:5003/extract_document_api


##### 1 Make a POST request to the API endpoint with the image(document) you want to extract information from.
##### 2 Receive the JSON response containing the specific information of the document.


#### **How to run API once the Server is Up and running**
Demo : https://drive.google.com/file/d/1SSyx-NxW9NsJLyaIY70XuzHCt2v4y2Ir/view?usp=sharing 
    
    
    
    
