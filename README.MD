# install virtualenvironment and python 
check the video [here](https://www.youtube.com/watch?v=w9SlNyMZGiI&list=PLb84syw_FhMFGlDVYFIusJHxRstXUbNSO&index=1)
# Heroku link here 
https://djrestapp.herokuapp.com/api-docs/ 

# Install requirements
```bash
$ pip install -r requirements
```
# Create db structure
```bash
$ python manage.py migrate
```
# run server
```bash
$ python manage.py runserver
```
# links for examples
- using views and writing code manually with functions  
  http://localhost:8000/firstapp/students/
-  using views and writing code manually with classes  
  http://localhost:8000/secondapp/students/
- using mixin from django framework  
  http://localhost:8000/thirdapp/students/
- using generics from django framework  
  http://localhost:8000/fourthapp/students/
- using viewsets from django framework, also class level pagination example added  
  http://localhost:8000/fifthapp/students/
- this example has nested serializers. Check serializer.py  
  http://localhost:8000/sixthapp/
- django restapi basic authentication, tokenauthentication with djangomodelpermissions  
  added tokencheck  
  an example without any model  
  added id and name search for employee  
  http://localhost:8000/seventhapp/  
- Added cors allow all and image upload  
  http://localhost:8000/fileupload/
- Added corapi doc support - check this to find all api documentation  
  Added group as a slugfield  
  http://localhost:8000/sixthapp/api-docs/
  