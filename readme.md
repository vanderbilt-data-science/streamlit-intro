# streamlit-tutorial
> An introduction to streamlit for DS projects

In this workshop, we look over some of the basic functionality of streamlit for implementing interactive user applications in Python.  See below for the workshop outline and requirements

# Pre-requisites
This workshop requires the following:
* A local installation of Anaconda
* _Basic_ understanding of Python and pandas
If you don't have an installation of Anaconda available, your best bet is to follow along now and review the workshop videos later when your distribution is installed.  For advanced users, you may be able to hop on Vanderbilt's ACCRE (if you have an ACCRE account), or Vanderbilt's JupyterHub (https://www.vanderbilt.edu/accre/jupyter/) and use the functionality there.  However, in the first case, you will need to create a virtual environment using ACCRE which may take some time, and in the second case, you will need to use pip rather than Anaconda for installation.  Follow along and try the hands-on portions later!

# Installation steps
In case you fall behind, the basic installation steps are noted below:
1. Clone this repository to your location of interest.  You can do this by opening up a command line (Windows: optimally by Anaconda Prompt, but Git Bash, or Bash via WSL can also suffice; OSX: Terminal app) and typing `git clone https://github.com/vanderbilt-data-science/streamlit-intro.git`.
2. `cd` into your directory.  Using an Anaconda prompt (or terminal with Anaconda installed in OSX), type `conda env create -f environment.yml`.  When the installer asks for your approval to install the desired packages, type `y` and then press enter.
3.  Your installation may not be immediate and may take some time.  Be patient.
4.  After your installation completes, you should see a message about how to activate the environment.  Type `conda activate streamlit-env`.
5.  To start an instance of Jupyter Lab, type `jupyter lab`.  Do not close this window!

# Running streamlit
After your repo is cloned and your environment is created, you can run the code!  The way you can do this is through opening a terminal via Jupyter lab and typing `streamlit run penui.py`.  A window should pop up allowing you to see your UI!

# In-class exercises
Now that we have some experience using Streamlit, try one or more of the following tasks on your own:
1. Arrange the Interact plot selectboxes to be in a row rather than a column
2. Modify the original loaded df to persist (i.e., not be reset) whenever UI elements change.
3. Modify the form to be in the sidebar
4. Add one of the seaborn pair plots
5. Add a selectbox to choose the hue (e.g., grouping variable) for seaborn to plot colors with
6. Add an expandable section for one of the plots to be revealed when clicked
7. Use your imagination!

# Streamlit resources
Below are a few resources for using streamlit:
* **Streamlit home**: https://streamlit.io
* **Streamlit App Gallery**: https://streamlit.io/gallery
* **Stramlit Docs**: https://docs.streamlit.io/en/stable/
* **Streamlit API reference**: https://docs.streamlit.io/en/stable/api.html#
* **Streamlit Deployment and Sharing**: https://docs.streamlit.io/en/stable/deploy_streamlit_app.html

