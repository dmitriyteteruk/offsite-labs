# LAB 1 - Retail Scenario

## Background story
You are at industry event and a visitor start discussion during networking session.
> Hello! 
My name is James Bond and I am owner of a retail store. It is important for me to be sure that environment in my store is good (not very cold and not too hot) and clients feels good. At the same time I need to be sure that dwell time is adequate and customers do not spend half of day in a queues. In addition, it is very important to be aware if temperatures in Frozen or Cold zones is out of normal range to avoid unnecessary lost from spoiled goods.
>
> What Microsoft can offer for me?

-	Our partner Contoso has new IoT solution that ideally fits with your needs.
-	Contoso device is certified as Plug and Play ready and you need just several minutes to start with it! You no need to be a programmer and cloud expert and it is very easy to calculate monthly cost of this solution, thanks to our Azure IoT Central SaaS offer.
-	Let me show you, how it works!

## What you need to do a live demo?
1. First of all, you need to prepare you laptop for demo using [this tutorial](link).
2. You need to copy code from following files and save them on your PC:
   - [Python Application](lab1/Multiple-Sensors-Devices_App.py) that will simulate device with multiple sensors
   - [Plug and Play device capability model](lab1/Multi_Thermostat_Occupancy%20-%20capability%20model.json) that contains all information about device that you will use for demo
3. Create IoT Central application (Azure subscription is required) using Application Template (via shared link)
4. Import PnP Device Capability model
5. Add Real device into your application and assign that device to your Device Capability model
6. Copy Credentials for your device into Python application code and save this application.
7. Run Python application and see how telemetry go to IoT Central App.

## 1. Prepare you laptop for demo
If you already prepared your laptop before, then skip step 1.
Please install required development environment on your laptop  (Python, IOTC client, VS Code) using this tutorial.

## 2. Copy required code to your laptop
### 2.1. Copy Python Application code
Open page with [Python Application code](ADD LINK TO RAW FILE) in a new browser Tab using `Ctrl + left mouse click`.

 - Copy entire code from the file
 
![](lab1/lab1-1.PNG)
![](lab1/lab1-2.PNG)

 - Open VS Code and create New File

![](lab1/lab1-3.PNG)

 - Paste code into new file. Code color is monochrome (white)
 
![](lab1/lab1-4.PNG) 
![](lab1/lab1-5.PNG) 

 - Save As file with Python Application extension `*.py`. 

![](lab1/lab1-6.PNG)
![](lab1/lab1-7.1.PNG)

- Code start to be colorful after files is saved.

![](lab1/lab1-7.2.PNG)

### 2.2. Copy Device Capability Model
Open page with [Device Capability Model](ADD LINK TO RAW FILE) in a new browser Tab using `Ctrl + left mouse click`.

- Copy entire code from the file

![](lab1/lab1-9.PNG)
![](lab1/lab1-10.PNG)

- Open VS Code and create New File and Paste code in it

![](lab1/lab1-11.PNG)

 - Save As file with JSON with Comments extension `*.json`. 
 ![](lab1/lab1-12.PNG)

- Code start to be colorful after files is saved.

![](lab1/lab1-13.PNG)

## Create Azure IoT Central application
 - Open [Azure IoT Central web-site](https://apps.azureiotcentral.com/)
 - Sign-in with your working Azure credentials (work account)
 
 ![](lab1/lab1-14.PNG)
 
 - Click on [this link](https://apps.azureiotcentral.com/build/new/a48aafe5-4649-4646-a7d8-4e116b6521f4) to get Application Template for Retail Solution
