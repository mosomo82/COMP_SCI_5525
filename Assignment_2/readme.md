# Assignment 2 — Multi-Cloud Web Deployment

**Course:** CS 5525 — Cloud Computing
**Student:** Tony Nguyen
**Date:** March 2026
**University:** University of Missouri – Kansas City

---

## 📋 Overview

This assignment demonstrates deploying a personal web page across three major cloud providers — **Amazon Web Services (AWS)**, **Google Cloud Platform (GCP)**, and **Microsoft Azure** — using each platform's preferred hosting method. The goal is to compare Infrastructure-as-a-Service (IaaS) vs. Platform-as-a-Service (PaaS) approaches, understand IAM and access control policies, and practice real-world cloud deployment workflows.

---

## 🌐 Live Deployments

| Platform | URL | Hosting Method |
|----------|-----|----------------|
| **AWS** | [http://amzn-s3-cs5525-tonyn-bucket.s3-website-us-east-1.amazonaws.com](http://amzn-s3-cs5525-tonyn-bucket.s3-website-us-east-1.amazonaws.com) | S3 Static Website Hosting |
| **GCP** | [http://34.66.74.246](http://34.66.74.246) | Compute Engine VM + Apache2 |
| **Azure** | [https://cs5525tonynstorage.z19.web.core.windows.net](https://cs5525tonynstorage.z19.web.core.windows.net) | Blob Storage Static Website |

---

## 📄 Web Page

A simple personal portfolio HTML page (`index.html`) was created and deployed on all three platforms, featuring:

- Full name: **Tony Nguyen**
- Title: *Data Scientist & Cloud Architect*
- About Me section
- Skills and project highlights

---

## ☁️ Platform Deployment Details

---

### 1. Amazon AWS (30%)

**Method:** S3 Static Website Hosting *(PaaS)*

#### Steps Taken

1. Signed into the **AWS Management Console** at `console.aws.amazon.com`
2. Navigated to **S3** → Created a new bucket: `amzn-s3-cs5525-tonyn-bucket` (Region: us-east-1)
3. Enabled **Static Website Hosting** under the bucket **Properties** tab
4. Set `index.html` as the index document
5. Disabled "Block all public access" and updated the **Bucket Policy** to allow public reads:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [{
       "Effect": "Allow",
       "Principal": "*",
       "Action": "s3:GetObject",
       "Resource": "arn:aws:s3:::amzn-s3-cs5525-tonyn-bucket/*"
     }]
   }
   ```
6. Uploaded `index.html` to the bucket via the S3 console **Upload** button
7. Verified the live site at the S3 website endpoint URL

#### Screenshots

| Step | Description |
|------|-------------|
| Screenshot 1 | AWS Console — logged in with account name visible |
| Screenshot 2 | S3 bucket created and Static Website Hosting enabled |
| Screenshot 3 | Bucket Policy configured for public access |
| Screenshot 4 | `index.html` uploaded and listed in Objects tab |
| Screenshot 5 | Live site accessible at S3 endpoint |

---

### 2. Google Cloud Platform (30%)

**Method:** Compute Engine VM with Apache2 HTTP Server *(IaaS)*

#### Steps Taken

1. Signed into the **Google Cloud Console** at `console.cloud.google.com`
2. Created a new project: `cs5525-tonyn`
3. Navigated to **Compute Engine** → **VM Instances** → Created a new VM:
   - **Machine type:** `e2-micro` (free tier eligible)
   - **Boot disk:** Ubuntu 22.04 LTS
   - **Firewall:** Checked *Allow HTTP traffic* and *Allow HTTPS traffic*
4. SSH'd into the VM using the **Cloud Shell SSH** button
5. Installed and started Apache2 web server:
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install apache2 -y
   sudo systemctl start apache2
   sudo systemctl enable apache2
   ```
6. Verified Apache default page via the external IP
7. Transferred the `index.html` content to the web root:
   ```bash
   sudo nano /var/www/html/index.html
   # Pasted HTML content, saved with Ctrl+O, exited with Ctrl+X
   ```
8. Confirmed the live page at `http://34.66.74.246`

#### Screenshots

| Step | Description |
|------|-------------|
| Screenshot 1 | GCP Console — logged in with account email visible |
| Screenshot 2 | Compute Engine VM instance running (external IP shown) |
| Screenshot 3 | SSH terminal — Apache2 installation and systemctl output |
| Screenshot 4 | SSH terminal — writing `index.html` to `/var/www/html/` |
| Screenshot 5 | Live site accessible at GCP external IP |

---

### 3. Microsoft Azure (30%)

**Method:** Azure Blob Storage Static Website *(PaaS)*

#### Steps Taken

1. Signed into the **Azure Portal** at `portal.azure.com`
2. Created a **Storage Account**: `cs5525tonynstorage`
   - **Region:** East US
   - **Performance:** Standard
   - **Redundancy:** LRS (Locally Redundant Storage)
3. Navigated to **Data management** → **Static website**
4. Enabled static website hosting and configured:
   - **Index document name:** `index.html`
   - **Error document path:** `404.html`
5. Noted the auto-generated primary endpoint URL
6. Navigated to the auto-created **`$web`** container
7. Uploaded `index.html` via the **Upload** button in the container view
8. Verified the live site at the Azure static website endpoint

#### Screenshots

| Step | Description |
|------|-------------|
| Screenshot 1 | Azure Portal — logged in with account name visible |
| Screenshot 2 | Storage account `cs5525tonynstorage` created |
| Screenshot 3 | Static website feature enabled with index document set |
| Screenshot 4 | `index.html` uploaded to the `$web` container |
| Screenshot 5 | Live site accessible at Azure endpoint |

---

## 📊 Platform Comparison

| Feature | AWS S3 | GCP Compute Engine | Azure Blob Storage |
|---------|--------|--------------------|--------------------|
| **Deployment Type** | PaaS (Managed) | IaaS (Virtual Machine) | PaaS (Managed) |
| **Setup Complexity** | ⭐ Low | ⭐⭐⭐ High | ⭐ Low |
| **Server Management** | None required | Full (Apache2) | None required |
| **HTTPS Support** | Via CloudFront CDN | Manual cert installation | Built-in ✅ |
| **Free Tier** | 5 GB storage / 20K requests | 1× e2-micro VM/month | 5 GB storage / month |
| **Deployment Speed** | ~5 minutes | ~20 minutes | ~5 minutes |
| **File Transfer Method** | S3 Console / AWS CLI | SCP / SSH / Cloud Shell | Azure Portal / Storage Explorer |
| **IAM / Access Config** | Bucket Policy (JSON) | Firewall Rules + IAM Roles | Blob access level + RBAC |
| **Custom Domain** | Via Route 53 | Via DNS A record | Via Azure CDN |

---

## 📝 Epilog

Deploying a simple personal web page across AWS, Google Cloud Platform, and Microsoft Azure was both an illuminating and challenging experience. The most important lesson learned was that each provider offers multiple pathways to the same result: AWS S3 and Azure Blob Storage made static hosting effortless through a simple toggle and bucket/container policy, requiring minimal configuration for public access and producing a live URL in minutes; GCP, by contrast, required provisioning a full Compute Engine VM and manually installing and configuring Apache2, which was the most hands-on but also the most educational step in understanding how web servers actually function at the infrastructure level. The most difficult part across all three platforms was navigating IAM policies, bucket permissions, and firewall rules — a misconfigured firewall rule on GCP blocked all HTTP traffic until port 80 was explicitly opened in the VPC firewall settings, and AWS's "Block Public Access" default required careful policy overrides to serve content publicly. AWS S3 was the most enjoyable method for its simplicity, speed, and clean endpoint URL out of the box, while GCP Compute Engine was the most rewarding in terms of understanding real infrastructure management. In future classes, I would recommend a dedicated session on cloud networking fundamentals — VPCs, security groups, and firewall rules — as understanding these concepts upfront would have saved significant troubleshooting time across all three deployments, along with an introduction to infrastructure-as-code tools like Terraform for standardizing and automating multi-cloud workflows.

---

## 🛠️ Technologies Used

- **HTML / CSS** — Static personal portfolio web page
- **Amazon S3** — Object storage with static website hosting (AWS)
- **Google Compute Engine** — Ubuntu 22.04 LTS virtual machine (GCP)
- **Apache2** — HTTP web server installed on GCP VM
- **Azure Blob Storage** — Object storage with static website hosting (Azure)
- **Google Cloud Shell / SSH** — Remote VM access and file transfer
- **AWS Management Console** — S3 bucket creation and management
- **Azure Portal** — Storage account and container management

---

## 📂 Repository Structure

```
Assignment_2/
├── index.html              # Web page deployed to all three platforms
├── readme.md               # This file
└── screenshots/
    ├── aws/
    │   ├── 01_aws_console_login.png
    │   ├── 02_s3_bucket_static_hosting.png
    │   ├── 03_bucket_policy.png
    │   ├── 04_file_upload.png
    │   └── 05_live_site.png
    ├── gcp/
    │   ├── 01_gcp_console_login.png
    │   ├── 02_vm_instance_running.png
    │   ├── 03_ssh_apache_install.png
    │   ├── 04_file_transfer_webroot.png
    │   └── 05_live_site.png
    └── azure/
        ├── 01_azure_portal_login.png
        ├── 02_storage_account_created.png
        ├── 03_static_website_enabled.png
        ├── 04_file_upload_web_container.png
        └── 05_live_site.png
```

---

## 👤 Author

**Tony Nguyen**
Master of Science in Data Science and Analytics
University of Missouri – Kansas City
CS 5525 — Cloud Computing | Spring 2026
