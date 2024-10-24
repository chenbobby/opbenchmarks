# Setup

1. Create a Ubuntu 22.04 VM.

2. Install `zsh`

```
sudo apt install zsh
```

3. Create non-root user with `zsh`

```
sudo useradd --create-home --shell /usr/bin/zsh NON_ROOT_USERNAME
echo NON_ROOT_USERNAME:PASSWORD | sudo chpasswd
usermod --append --groups sudo NON_ROOT_USERNAME
```

4. Enable SSH access for non-root user by copying `authorized_keys`.

```
mkdir -p /home/NON_ROOT_USERNAME/.ssh
sudo cp ~/.ssh/authorized_keys /home/NON_ROOT_USERNAME/.ssh/
sudo chown -R NON_ROOT_USERNAME:NON_ROOT_USERNAME /home/NON_ROOT_USERNAME/.ssh
```

15 Install specific Python version for Ubuntu.

```
# For better UX, create a symbolic link python -> python3.
sudo ln --symbolic /usr/bin/python3 /usr/bin/python

# Add the APT repository for specific Python versions on Ubuntu.
sudo add-apt-repository ppa:deadsnakes/ppa

# Update local APT index.
sudo apt update

# Install a specific version of Python.
sudo apt install python3.13

# Set your specific version an alternative of `python3`
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.13 13

# View and confirm your alternatives are configured correctly.
sudo update-alternatives --config python3

# Re-install Ubuntu packages with our specific version of Python.
sudo apt remove --purge python3-apt
sudo apt autoclean
sudo apt install python3-apt
sudo apt-get install python3.13-distutils python3.13-dev python3.13-venv

# Install `pip` with our specific version of Python.
curl -sS https://bootstrap.pypa.io/get-pip.py | python
```

6. Create a Python virtual environment.

```
python -m venv .venv
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

As of 2024-10-23, use these to fix dependency issues:
```
pip install MarkupSafe==3.0.2
pip install typing_extensions==4.12.2
pip install numpy==2.1.2 
```
