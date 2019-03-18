# Zawadi App
#### Date: March 17th 2019
#### By **James Mwangi Nduge**
## Description
Zawadi is swahili for an award/present.It is an app that allows users create an account, view projects posted by themselves and other users,rate and review projects.
## Setup/Installation Requirements
* Access github on a web browser
* clone this repository  from https://github.com/jamesnduge/Jimjam
* Navigate to the cloned project file on your terminal
* Create a Virtual enviroment `python3.7 -m venv virtual` and activate using `source virtual/bin/activate`
* Install Django in your virtual enviroment `pip install django==1.11.17`
* Run the command `pip install -r requirements.txt` to install the required dependencies
* Run the command `python3.7 manage.py runserver` to launch the application
## Testing the Application
* To run tests for the class files:
  * ` python3.7 manage.py test`
## Behaviour Driven Development
|Behaviour| Input | Output|
|---------|-------|-------|
|Homepage| - | -
|user clicks on  project_image| clicks image  | sign in required
|user search for projects  | types in project name | if project is found , it returns else no search results
|user click on visit site| click button| redirects to actual site of project


## Live Demo
 Here is a link to a live demo : https://zawadis.herokuapp.com
## Known Bugs
There are no known bugs for this application
## Technologies Used
* Python3.7
* Html
* CSS
* Django framework

## Support and contact details
Please feel free to contact me at james_mwangi@aol.com for any questions or insight on the application.
### License
*This project is licensed under the MIT License - see the LICENSE.md file for details*
Copyright (c) {2019} **{James Nduge}**