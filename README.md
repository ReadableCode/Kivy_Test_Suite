# Kivy_Test_Suite

Kivy Test Suite

## Running dev env with pipenv

* Install dependencies for system:

  * Install packages with Apt:

      ```bash

      sudo apt-get update
      sudo apt-get install -y \
          zlib1g-dev \
          openjdk-17-jdk \
          unzip \
          build-essential \
          autoconf \
          automake \
          libtool \
          git \
          python3-pip \
          python3-dev \
          libssl-dev \
          libffi-dev \
          libxml2-dev \
          libxslt1-dev \
          libncurses5-dev \
          libsqlite3-dev \
          libreadline-dev \
          libbz2-dev \
          liblzma-dev \
          libgdbm-dev \
          libdb-dev \
          libpcap-dev \
          cmake \
          pkg-config \
          zip
      ```

  * Install pipenv:

      ```bash
      pip install pipenv
      ```

* To install dependencies:

  ```bash
  pipenv install
  ```

  To run:

  ```bash
  pipenv run python src/main.py
  ```

* To make changes to requirements.txt, change the file and then:

  ```bash
  deactivate
  pipenv --rm
  rm Pipfile.lock
  rm Pipfile
  pipenv install # to use the new requirements.txt
  ```

* To enter bash in the virtual environment:

  ```bash
  pipenv shell
  ```

* To Activate or Source the environment and not have to prepend each command with pipenv:

  On Linux:

  ```bash
  source $(pipenv --venv)/bin/activate
  ```

* To Deactivate:

  ```bash
  deactivate
  ```

## Building for Android

```bash
buildozer init
```

Edit the buildozer.spec file to include the following:

```ini
```

```bash
buildozer -v android debug
```

If run into an issue with `.buildozer/android/platform/android-sdk/tools/bin/sdkmanager" does not exist, sdkmanager is notinstalled`:

* Remove the .buildozer directory:

  ```bash
  rm -r ~/.buildozer/
  ```

* Then run the buildozer command again:
  
  ```bash
  buildozer -v android debug
  ```
