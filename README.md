# Library Management
https://library-management-ymzu.onrender.com
## Development instructions
The project has integrated frontend and backend code, and is an npm package  
### Environment requirements:
node.js 20.9.0
python 3.10.11
### Install backend and frontend dependencies: 
```
cd backend
source ./bin/activate
pip install -r requirements.txt
```
```
cd frontend
npm install
```
### Run the server and client servers separately:
```
cd backend
python manage.py runserver
```
```
cd frontend
npm run dev
```
### Build the frontend build and serve through backend:
```
cd frontend
npm run build
```
```
cd backend
python manage.py collectstatic --noinput
python manage.py runserver
```
