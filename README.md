# Python Chatroom Example

This is a very simple example of how to setup a chat room using Python.  
For this example, we'll be using the Python web microframework [Quart](https://pgjones.gitlab.io/quart/).  

If you're familiar with [Flask](http://flask.pocoo.org/), then you pretty much know Quart.  In fact, Quart presents itself as ["an evolution of Flask"](https://pgjones.gitlab.io/quart/discussion/flask_evolution.html#flask-evolution) utilizing the latest features in Python such as [asyncio](https://docs.python.org/3/library/asyncio.html) and it comes with [out-of-the-box Websocket support](https://pgjones.gitlab.io/quart/how_to_guides/websockets.html).  

In addition to introducing how you can build a Python chat room using Python, this example also introduces you to [Node.js](https://nodejs.org/en/) and uses it to build the UI for the user.  
While Node.js may not be strictly necessary to build a UI as simple as this and it may seem a bit over-engineered, exposure to Node.js is very important because, as of the time of writing, JavaScript is the *lingua franca* of the web UIs (and possibly UIs in general).  So this exposure will only benefit you in the long-run.  
The UI isn't very complicated, just a textfield, a send button, and an area where messages render.  
The chat UI uses no frameworks, just simple [jQuery](https://jquery.com/) for functionality and [Bootstrap](https://getbootstrap.com/) for styling.  

<hr>

**WARNING**: This is a work in progress.  Once this is complete this warning will be removed.  Thank you for your patience.  

<hr>

## License

This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.  
![Creative Commons License](./by-sa.svg)  

## Requirements

To run this project you'll need the following:

- A (mostly) up to date Mac (Windows PCs will soon be supported)
- A (mostly) up to date modern browser.  [Chrome](https://www.google.com/chrome/) or something [Chrome-like](https://brave.com/) or [Firefox](https://www.mozilla.org/en-US/firefox/) or any other major browser should be good enough.  
- Some familiarity with the command line terminal.  
- The command-line package manager [Homebrew](https://brew.sh/).  
- The runtime agnostic version management tool [ASDF VM](https://asdf-vm.com/) and it's plugins for [Python](https://github.com/danhper/asdf-python) and [Node.js](https://github.com/asdf-vm/asdf-nodejs).  
- A code editor.  It doesn't matter which one because a well structured project should be agnostic to which code editor the developer chooses.  However, in this case we'll recommend [Visual Studio Code](https://code.visualstudio.com/) (not to be confused with Visual Studio).  

## Setup Development Environment (Mac)

The following steps will show you how to setup a development environment for the Mac.  
This step only needs to be done once per machine and will only need to be occasionally updated.  
Meaning that once you set up your machine for Python and Node.js, you can run other Python or Node.js projects without worrying about this step again (barring occasional updates).  

### Install Xcode Select

Not to be mistaken for [Xcode](https://developer.apple.com/xcode/) itself, a full IDE for the Mac, Xcode Select is a collection of standard developer tools (mostly command-line) from Apple for the Mac (and other Apple products).  Xcode Select is used by Xcode, but Xcode Select can be used independently of Xcode.  

Install Xcode Select with the following command:  

```sh
```

### Install Homebrew

### Use Homebrew to Install ASDF VM

### Install ASDF Python Plugin

### Install ASDF NodeJS Plugin

### Install Visual Studio Code

## Setup Development Environment (Windows)

*Coming soon: As of now this project doesn't support windows, but it shall soon.*

## Bootstrapping the Project

The following steps will show you how to bootstrap the project.  
Simply downloading the project isn't sufficient, you need to perform a series of steps to initialize it, such as ensuring the proper runtimes are installed and are in use, ensuring that dependencies are installed, the project builds the application, etc.  
However, this step only needs to be done once per project.  Meaning that if you make changes to the source code you don't need to re-run this step (except maybe the build step).  

### 1. Clone or Download the Project

It's recommended that you clone this project with [Git](https://git-scm.com/), however if you're not familiar with Git, you can download the zip file of this project and unzip it.  

To clone with Git run the following command:  

This includes ASDF VM to manage runtimes, SDKs, and developer tools.  
The ASDF VM plugins for Python and Node.js.  
Python has `virtualenv` installed.  
You'll need Python and Node.js.  

### 1. Use ASDF VM to install the Dependencies

```sh
asdf install
```

### 2. Install all Node.js Dependencies

```sh
npm install
```

### 3. Create Python Virtual Environment

```sh
pip3 install --upgrade pip
pip3 install virtualenv
python3 -m virtualenv venv
```

### 4. Activate Python Virtual Environment

```sh
source ./venv/bin/activate
```

When you want to deactivate the Python virtual environment run the following command: `deactivate`

When you want to come back to this environment, you'll need to re-activate the Python virtual environment to re-run this project.  

### 5. Install the Python Dependencies

Run this **AFTER** you've created and activated the Python virtual environment.  

```sh
pip install -r requirements.txt
```

**NOTE:** Notice how we didn't have `pip3` this time.  This is because the virtual environment was created with Python3, so we're running in a Python3 environment with no risk of accidentally using Python2.  

### 6. Build the UI

```sh
npx parcel build ./public/index.html
```

## Usage

### 1. Activate Python Virtual Environment If You Haven't Done So Already

```sh
source ./venv/bin/activate
```

### 2. Running the Project

```sh
python app.py
```

Server will be running on [http://localhost:5000/](http://localhost:5000/).  
You can use <kbd>ctrl</kbd> + <kbd>C</kbd> to stop the application.  

### 3. Using the socket

1. Enter anything in the textbox.
2. Press the <kbd>send</kbd>
3. When the messages is received via the websocket, the application will return the text that was just sent.  
