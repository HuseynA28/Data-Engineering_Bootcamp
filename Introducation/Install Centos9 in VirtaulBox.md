# Installing CentOS 9 on VirtualBox

## Step 1: Download CentOS 9 ISO

1. Go to the [official CentOS website](https://www.centos.org/).
2. Download the **CentOS Stream 9 ISO** from the download section.
3. Choose the appropriate ISO (`x86_64` architecture for most systems).

## Step 2: Create a New Virtual Machine

1. Open **VirtualBox** and click on **New**.
2. Enter a name (e.g., `CentOS9`), select **Type: Linux**, and **Version: Red Hat (64-bit)**.
3. Click **Next**.

## Step 3: Allocate Memory

- Assign at least **2048 MB (2 GB)** of RAM (Recommended: **4096 MB (4 GB)** for better performance).
- Click **Next**.

## Step 4: Create a Virtual Hard Disk

1. Select **Create a virtual hard disk now** and click **Create**.
2. Choose **VDI (VirtualBox Disk Image)** and click **Next**.
3. Select **Dynamically allocated**.
4. Set the disk size to at least **20 GB** and click **Create**.

## Step 5: Attach CentOS 9 ISO

1. Select the **CentOS9 VM** and click **Settings**.
2. Navigate to **Storage** > **Empty** (under Controller: IDE).
3. Click the **CD icon** and select **Choose a disk file**.
4. Locate and select the **CentOS 9 ISO**.
5. Click **OK**.

## Step 6: Configure Network Settings (Optional)

1. In **Settings > Network**, ensure **Adapter 1** is attached to **NAT**.
2. (Recommended) If you want a Bridged Adapter:
   - Change **Adapter 1** to **Bridged Adapter**.
   - Select your host’s network adapter.
   - Click **OK**.

## Step 7: Start the Installation

1. Click **Start** to boot the CentOS 9 VM.
2. Select **Install CentOS Stream 9** and press **Enter**.
3. Wait for the installer to load.

## Step 8: Configure Installation

1. Select your **language** and click **Continue**.
2. Click **Installation Destination**:
   - Select the virtual hard disk.
   - Click **Done**.
3. Click **Software Selection**:
   - Choose **Server with GUI** or **Minimal Install** based on your preference.
   - Click **Done**.
4. Set **Root Password** and create a user account.
5. Click **Begin Installation**.

## Step 9: Complete Installation

1. Once installation is complete, click **Reboot**.
2. Remove the CentOS 9 ISO:
   - Go to **Devices > Optical Drives** in VirtualBox.
   - Uncheck the ISO file and restart.

## Step 10: First Boot and Login

1. Login with the user account or root credentials.
2. If you installed a GUI, the CentOS desktop will load.
3. Run updates:

   ```bash
   sudo dnf update -y
   ```

