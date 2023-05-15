---
title: "Set up your environment"
date: 2020-11-23T04:51:13+01:00
draft: false
hideLastModified: true
keepImageRatio: false
showInMenu: false
---

# Setup Your Environment

Watch the video ['Setup your environment'](https://www.youtube.com/watch?v=qy6s_CeBi5M) to give you an idea what you will have to do.

We have provided the datasets and software in a variety of formats.  You choose how you want to use them:

* If you want to have a quick look at the data, not investing too much time, you can use the **small virtual machine (06-Feb-2017)**, which contains 10% of the data.  This takes about 15 minutes to download and setup.  Read on.

* If you want to invest more time, or are setting up a lab for students, then we recommend you use the **large virtual machine** which contains all the data.  This takes 1-2 hours to download and setup.  [Go to the Virtual Machine Book](https://cheatham1.gitbooks.io/atlasdatatools/content).

* If you are a student in a lab and the virtual machine is already setup for you, go straight to the next chapter [Take a look at the data](https://cheatham1.gitbooks.io/openatlasdatatools/content/take_a_look_at_the_data.html).

* If you are a physicist, it is likely you already have ROOT installed, so you can download the [software](http://atlas-opendata.web.cern.ch/atlas-opendata/extendedanalysis/software.php) **and** [datasets](http://atlas-opendata.web.cern.ch/atlas-opendata/extendedanalysis/datasets.php) separately if you wish.
Please take into account that Python2 is recommended. Python 2.7 is the version distributed into the VMs. Python3 could give you some issues.

## What is a virtual machine ?

A virtual machine will transform your computer into an analysis machine!

Your physical computer will be the "host", while the virtual machine will be a "guest". Most of the guest code runs unmodified, directly on the host computer, and the guest operating system "thinks" it's running on a real machine.

A virtual machine allows an unmodified operating system with all of its installed software to run in a special environment, on top of your existing operating system. 

There are five virtual machines available.
We suggest you start with the **small** version.  It contains everything you need to start looking at the data.

**Now you will learn how to download and prepare a virtual machine to run on your computer**.  This will then enable you to take a look at ATLAS data. 

You have to download and install VirtualBox **and** a virtual machine.  To save time, start downloading the  virtual machine.  This can then download whilst you are installing VirtualBox.

There are three steps to setup your environment:
1. Download a virtual machine.
2. Download and install VirtualBox.
3. Setup your virtual machine.

**If your session goes to sleep and requires the atlas password, it is 'atlas'.**

<CENTER>
<img src="./pictures/Pictures/atlasSaver.png" width="200" />
</CENTER>

# Step 1: Download the Small Virtual Machine (VM Version S 06-Feb-2017)

A small virtual machine using Lubuntu in conjunction with ROOT-5.34.14 and 10% of the data has been prepared. This is 1.7Gb in size so can be downloaded fairly quickly. 

Select **Virtual Machines**


[<img src="./pictures/Pictures/VMbutton.jpg"/>](http://atlas-opendata.web.cern.ch/atlas-opendata/extendedanalysis/vm-toolbox.php)


Select **VM Version S** to download the **small** virtual machine.
This can then download whilst you are installing VirtualBox.

Make sure you choose **Lubuntu_ATLAS_Outreach_DataAndTools_February_2017-size_S.ova **

# Step 2: Download and install VirtualBox

Use the VirtualBox website to download the software

<a href="https://www.virtualbox.org/" target="_blank"> Go to the VirtualBox website</a>

Select **Download VirtualBox**
 
![](pictures/Pictures/VB5.1.jpg)

Take care to select the appropriate **VirtualBox platform package**.


![](pictures/Pictures/DownloadVB.jpg)
 
Proceed with the installation of VirtualBox:

![](pictures/Pictures/VBinstall1.png)


![](pictures/Pictures/VBinstall2.png)


![](pictures/Pictures/VBinstall3.png)


## Step 3: Set up your Virtual Machine

In this step the downloaded virtual machine is being imported to VirtualBox to give the virtual machine a platform to run on.

Look for the VirtualBox icon in your Applications (folder). Double click to get the main interface of VirtualBox:


![](pictures/Pictures/VMempty.png)

Select **File** then **Import Appliance**

![](pictures/Pictures/VMimportAppliance.png)

An empty text box will appear

![](pictures/Pictures/VMimportApplianceSelect.png)

Use the yellow folder icon on the right hand-side of the empty text box to select your virtual machine (the .ova file you downloaded at the start of this chapter).  

**Make sure you have downloaded the small virtual machine.**  It will be called **ATLASOpenDataSmall.ova**

Then press **Continue**.


![](pictures/Pictures/VMselectOVA.png)

The default settings are displayed.  We recommend you use these.  Press **Import**.

![](pictures/Pictures/VMapplianceSettings.png)

Import will take afew minutes

![](pictures/Pictures/VMimporting.png)

Select your virtual machine **ATLASOpenDataSmall** (which is powered off)

**If your VM is not called ATLASOpenDataSmall you have not downloaded the small virtual machine.**  You need to be using the small VM for these instructions.

![](pictures/Pictures/VMpoweredOff.png)

Your VM will be displayed as shown below

**Check that the name of your virtual machine displayed on the right is ATLASOpenDataSmall**

![](pictures/Pictures/VMATLASopenDataSmall.png)


Press the green **Start** arrow.

**WAIT** afew minutes whilst the virtual machine sets up.  

When it has completed you will see 
the terminal for using the code, with the Readme file opened using the atom editor.

![](pictures/Pictures/VMrunningREADME.png)

In the menu on the left handside, you see the contents of the root directory.

In the root directory there are five directories (Analysis, Configurations, Input, Plotting and Output), the README file plus two python scripts. The python scripts are RunScript.py and PlotResults.py. 

At the bottom of your window, you will notice a tab labelled **atlas@atlas-vm**.

![](pictures/Pictures/VM-atlas.png)

Select this tab, circled in red in the screen-shot.  A terminal window will then be available. 

List the folders and files in your main directory by typing

    ls
    
You will notice that these are the same names as you saw in the menu (screen-shot above).    

![](pictures/Pictures/VMterminalWindow.png)

You are now ready to start looking at the ATLAS data.
