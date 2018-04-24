# Welcome to BinkSearch!

### A small search tool used to enable Colour-based searches for random items leveraging the AWESOME power of Google!

## Getting Started

This little app is writtten using Python 3 and utilising the Flask micro framework so if you are using your defaul Python on a Mac, It's probably Python 2. If you're using a Windows machine you may not even have Python installed at all! In any case, open a Terminal window in MacOS or open the Command Line in Windows and type the following: `python --version`. If you have anything other than "3.'something'" you'll need to remedy that by installing Python 3. The easiest way to do this is is by going to: https://www.python.org/downloads/ and click on the download option for your operating system. Their website should auto detect which OS you are using (Windows / MacOS / Linux etc.) so just go ahead and download VERSION 3.whatever and install in the usual way.

Now you need to ensure that you are using a virtual environment before going any further. There are MANY reasons for this which would take far too long to go into in a simple ReadMe, the simplest being that you want to ensure that each project you build runs the way you want it to without relying on code from elsewhere that might be out of date/sync with your current project. It's just less hassle in the long run. So, with that in mind you need to make sure you can do this. Once again, using the command line/terminal type the following: `virtualenv --version`. This will show you if you have "Virtualenv" installed or not. If not type `pip3 install virtualenv` (`pip install virtualenv` for Windows) and let your machine do its thing. Once that is done you need to create the virtual environment that you will be using for this project. In the command line / terminal type `virtualenv "whatever name you like"` typically you would use sometjong like "venv" but if you nave a number of projects on the go, you may want to be more specific like "searchvenv" or something distinct to your own project. Once that is done you need to activate your environment so that you can work in it. Do this in windows by typing `"name of your environment"\Scripts\activate` or for MacOS it's `source "name of your environment"/bin/activate`. You should see the name of your environment now in brackets at the start of your command line. Something similar to this: `(venv) Richard-2:binksearch Rich$ ` or this `(venv) C:\Users\Richard\Desktop\binksearch>`. 

You can now go ahead and install Flask in this virtual environment and really start cooking! so without further ado, type `pip install flask` and watch the magic happen. Once that is done you are now ready to fork this repository and access the wonders that lie within.

## What was done

Initally a framework was set up using a simple flask arangement for routing to a single Home Page. This page was styled using Bootstrap 4 via their CDN rather than downloaing the entire library. There was very little that needed changing so better to keep things simple and reduce the number of requirements.

The main requirement was to set up a custom google search engine. This can be done by visiting https://cse.google.co.uk and setting up a new custom engine. It's fairy self explanatory but you do need a Google ID to set one up. Once that is in place you can grab the code from the CSE dashboard and embed wherever you wish within your own code. My plan was to embed the code into the buttons created and work the code to include both the colour of the box selected and the required random word. 

## Issues encountered

The main issue I encountered was getting JavaScript to work. Having set up a custom search with Google prioritising Images over pages, restricting this to five results and embedding the call to the function into the button, I am still unable to get this to work! Currently tearing my hair at at the moment, but I WILL get there . . . . 

If you get stuck at all, or want to discuss anything to do with thos code, I would love to hear from you so please do get in touch 