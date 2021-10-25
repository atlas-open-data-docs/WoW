---
title: "SaaS"
date: 2020-11-23T04:51:13+01:00
draft: false
hideLastModified: true
keepImageRatio: false
tags: ["Terraform", "Cloud", "notebooks", "Jupyter"]
summary: "Recipes for infrastructure deployment"
showInMenu: true
---


Welcome to the Automated Infrastructure Deployment Tool!
Did you ever wonder how to obtain a working, multi-user analysis environment for your students or your group?</br>
This page will guide you step by step in the setup of a [JupyterHub](https://jupyter.org/hub) (JH) hosted on a Cloud instance.

Here you have a advanced tool that allows **anyone** to deploy his/her own JH. </br>
Why anyone? Because no particular skills are required, it is sufficient to have a _basic knowledge of the linux bash terminal_, and the access to a _cloud provider_ onto which host the whole infrastructure.

## Features

Now, let's dive into the fundamental features of the tool: </br>
(if you don't care about the theory, just jump to the [dashboard](#deployment-dashboard) and start deploying!)

* **Notebooks flexibility**: your JH will not be bound to a specific notebook. If you have your own notebook image available on a registry, you can effortlessly deploy it. This allows both a great customizability, and the possibility to exploit JH for different analyses (not only ALTAS Open Data, but also ML applications, etc..)
* **Persistency of data**: your work will not be lost with the end of the session. No timeout for your notebooks. Data, plots and results always saved and accessible.
* **External/shared volumes**: if you have a big dataset, it is crucial to be able to share it with the users without having each of them to download the data. 
* **Speed**: this infrastructure is _fast_: the deploy time of the whole environment is of the order of 10 minutes (it only happens once); once JH is up and running, users will be able to obtain their notebook in a matter of _seconds_.

## Workflow

The deployment process relies on **two** fundamental services: [Docker](https://www.docker.com/) and [Terraform](https://www.terraform.io/). </br>
Docker provides the **modular** layout of the infrastructure, enabling most of the above mentioned features; together with agility and flexibility, thanks to the containerization, Docker also provides lightness to the whole environment. On the other hand, Terraform ensures the **automation** of the JH deployment. Below it is shown a flowchart of the deployment process.




&nbsp;

## Deployment dashboard

Just select the cloud provider that tickles your fancy (i.e. of which you actually have a working account), and follow the instructions!

| <h1><b>AWS instance</b></h1> | <h1><b>OpenStack@CERN instance</b></h1> | <h1><b>Google Cloud instance</b></h1> |
|        :---:        |        :---:       |        :---:       |
| [![AWS](./images/Amazon-Web-Services-AWS-Logo.png)](https://gitlab.cern.ch/atlas-open-data-iac-qt-2021/aws_automated_jh_deployment/-/blob/master/README.md) | [![openstack](./images/OpenStack-Logo-Vertical.png)](https://gitlab.cern.ch/atlas-open-data-iac-qt-2021/automated_jh_deployment/-/blob/master/README.md) | [![google](./images/Google-Cloud-Emblem_work_in_progress.png)]()|


