## Update Application Dashboards

Now we need to update three IoT Central aplication dashboards. Technically, you can create them from scratch, but some images already added on out visualisation via Template Export.

We will update (re-create) tiles otlined with yellow color.

Click on `Dashboard` item on IoT Central application menu. Check that you are on **01. Main Dasboard** page and then click `Edit` button on the top left corner of the window.

![](lab1/lab1-41.PNG)

Once edit option appears use `X` icon to remove tiles from dashboard.

![](lab1/lab1-42.PNG)

You dashboard shoold look like this now.

![](lab1/lab1-43.PNG)

Now you need add new tiles. <br>
In Dashboad menu choose `Multi Sensor Device v1` in *Device template* drop-down menu, then choose `Multi Sensor Device v1 - xxxxx` in *Device instance* drop-down menu. You will see list of all possible telemetry options that we are collecting.

Drag and Drop to dashboard following telemetry tiles:
 - Count1 (this is people counter sensor installed near cahs-desk #1)
 - Count2 (this is people counter sensor installed near cahs-desk #2)
 - Count3 (this is people counter sensor installed near cahs-desk #3)
 - Dwell Time 1 (this is time counter sensor installed near cahs-desk #1)
 - Dwell Time 2 (this is time counte sensor installed near cahs-desk #2)
 - Dwell Time 3 (this is time counter sensor installed near cahs-desk #3)
 - Temperature4 (this is temperature sensor installed in Frozen area -20-15 degrees)
 - Temperature5 (this is temperature sensor installed in Refrigerated area +5+10 degrees)
 
You can drag and drop and modify tiles one by one or drag and drop all tiles and then modify them.

 ![](lab1/lab1-44.PNG)
 
 Now click on `Save` button to see if our tiles show data from our devices.
 
 ![](lab1/lab1-45.PNG)
 
 If you see graphics on you tiles then eeverythin is correct and we need to do some design modifications for these tiles.<br>
 Click `Edit` button on top of Dashboard name.
 
 ![](lab1/lab1-46.PNG)
 
 ### Modify Count tiles
 
 Find tile **Count1** and hover on rulers icon, then choose `Last Known Value` option in drop-down list.
 
 ![](lab1/lab1-47.PNG)
 
**Configure last known value** menu will appear on the left side. Change name from **Count1** to **Queue Length (people)** and then click `Update` button.
 
 ![](lab1/lab1-48.PNG)
 
Repeat this for tiles Count2 and Count3, then Click  `Save` on the top left corner of Dashboard Menu.

Click `Edit`
 
### Modify Count tiles
