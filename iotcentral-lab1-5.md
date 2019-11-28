## 5. Copy device credentials into Python application and run it

Open file **Multiple-Sensors-Devices_App.py** in VS Code and paste Device credentials into it, then click `File -> Save` to save the file.

![](lab1/lab1-23.PNG)

Then Click on `Run` icon on top right corner of VS Code window.

![](lab1/lab1-24.PNG)

Your Python application should run now and you will see logs in Terminal window.
Once you see `sendTelemetry :: { .....` text - it means that telemetry start go to IoT Central application.

![](lab1/lab1-25.PNG)

Now go to IoT Central application and check if telemetry is visible.
Click on `Devices` -> `Multi Sensor Device V1 - xxxx` name.

![](lab1/lab1-26.PNG)

You should see default device Dashboard with numbers and timestamps in some tiles.<br>
*Please note.* Some tiles will look not good, because Application Template feature does not copying files (images) related in particular devices. We will fix broken tiles during next steps.

![](lab1/lab1-27.PNG)

### Lab Navigation Menu
[Go forward - 6. Update Application Dashboard](/iotcentral-lab1-6.md)<br>
[Go back - 4. Add Real device into your application](/iotcentral-lab1-4.md)<br>
[Go to main page of the LAB](/iotcentral-lab1-0.md)
