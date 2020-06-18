# install virtualenvironment and python 
check the video [here](https://www.youtube.com/watch?v=w9SlNyMZGiI&list=PLb84syw_FhMFGlDVYFIusJHxRstXUbNSO&index=1)
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
  http://localhost:8000/seventhapp/  
- sample curl code for getting details with token, check url below
  http://127.0.0.1:8000/api-docs/#seventhapp-api-token-auth-create
- Added corapi doc support  
  http://localhost:8000/sixthapp/api-docs/
- Added cors allow all and image upload
  http://localhost:8000/fileupload/
  