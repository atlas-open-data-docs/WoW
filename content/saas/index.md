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
This page will guide you step by step in the setup of a [JupyterHub](https://jupyter.org/hub) (JH) hosted on a Cloud instance, and will provide an overview of few notebooks solutions, to implement both **standalone or in combination** with JH.

Here you have an advanced tool that allows **anyone** to deploy his/her own JH. </br>
Why anyone? Because no particular skills are required, it is sufficient to have a _basic knowledge of the linux bash terminal_, and access to a _cloud provider_ onto which host the whole infrastructure.

## Features

Now, let's dive into the fundamental features of the tool: </br>
(if you don't care about the theory, just jump to the [dashboard](#deployment-dashboard) and start deploying!)

* **Notebooks flexibility**: your JH will not be bound to a specific notebook. We do provide a [standard notebook](#single-user-solutions), but if you have your own notebook image available on a registry, you can effortlessly deploy it. This allows both great customizability, and the possibility to exploit JH for different analyses (not only ALTAS Open Data, but also ML applications, etc..)
* **Persistency of data**: your work will not be lost at the end of the session, neither you will have a timeout for your notebooks. Data, plots and results are always saved and accessible.
* **External/shared volumes**: if you have a big dataset, it is crucial to be able to share it with the users without having each of them to download the data. 
* **Speed**: this infrastructure is _fast_: the deploy time of the whole environment is of the order of 10 minutes (it only happens once); once JH is up and running, users will be able to obtain their notebook in a matter of _seconds_.

## Workflow

The deployment process relies on **two** fundamental services: [Docker](https://www.docker.com/) and [Terraform](https://www.terraform.io/). </br>
Docker provides the **modular** layout of the infrastructure, enabling most of the above-mentioned features; together with agility and flexibility, thanks to the containerization, Docker also provides lightness to the whole environment. On the other hand, Terraform ensures the **automation** of the JH deployment. Below it is shown a flowchart of the deployment process.

{{< rawhtml >}}
<div align="center">
  <img src="./images/workflow.png" />
</div>
{{< /rawhtml >}}

## Single user solutions

### Jupyter Notebooks
[Jupyter notebooks](https://jupyter.org/) are the core of the analysis effort of ATLAS Open Data. </br>
Here we present a notebook built on top of the latest [scipy](https://hub.docker.com/r/jupyter/scipy-notebook) version, in which we embed the installation of the [ROOT](https://root.cern/) framework used at CERN, available in both python and C++ kernels. Other versions of the notebook are in development, in order to gradually increase the analysis potential of this tool.</br>
You can run the notebook both **standalone or in combination** with the JH infrastructure descripted above. Try it out on your pc by simply running the following docker command:
```
docker run -it --rm -p8888:8888 atlasopendata/root_notebook:latest
```
Then access the notebook via the browser by pasting the url provided by the terminal. It should be something like
(The token will be different for you)
```
To access the notebook, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/nbserver-15-open.html
    Or copy and paste one of these URLs:
        http://4c61742ed77c:8888/?token=34b7f124f6783e047e796fea8061c3fca708a062a902c2f9
     or http://127.0.0.1:8888/?token=34b7f124f6783e047e796fea8061c3fca708a062a902c2f9
```

### Virtual Machine(s)
ATLAS Open Data also provides a [virtual machine](http://opendata.atlas.cern/release/2020/documentation/vm/index.html), which allows you to test the 13 TeV ATLAS Open Data on your own host machine.

Take a closer look to our resources:

| <h1><b>Jupyter Notebooks</b></h1> | <h1><b>Virtual Machine</b></h1> |
|        :---:        |        :---:       |
| [![JN](./images/jn.png)](https://hub.docker.com/r/atlasopendata/root_notebook) | [![VM](./images/vm.png)](http://opendata.atlas.cern/release/2020/documentation/vm/index.html) |

&nbsp;

## Deployment dashboard

Just select the cloud provider that tickles your fancy (i.e. of which you actually have a working account), and follow the instructions!

| <h1><b>AWS instance</b></h1> | <h1><b>OpenStack@CERN instance</b></h1> | <h1><b>Google Cloud instance</b></h1> |
|        :---:        |        :---:       |        :---:       |
| [![AWS](./images/Amazon-Web-Services-AWS-Logo.png)](https://gitlab.cern.ch/atlas-open-data-iac-qt-2021/aws_automated_jh_deployment/-/blob/master/README.md) | [![openstack](./images/OpenStack-Logo-Vertical.png)](https://gitlab.cern.ch/atlas-open-data-iac-qt-2021/automated_jh_deployment/-/blob/master/README.md) | [![google](./images/Google-Cloud-Emblem_work_in_progress.png)]()|


