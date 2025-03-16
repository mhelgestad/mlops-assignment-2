# Assignment 2 Demo

## Classification Demo
### Original Class File
![image](./demo_screenshots/class_file_orig.png)
### App Running
![image](./demo_screenshots/app_run.png)
### Add list of classes with POST endpoint (`/add-classes`)
#### Additional GET endpoint to fetch the classes (`/classes`)
![image](./demo_screenshots/add_classes.png)
### Text file after `/add-classes` call
![image](./demo_screenshots/class_file_add.png)
### Any Classes that already exist will not be added twice
![image](./demo_screenshots/repeat_add.png)
### Classification Examples
![image](./demo_screenshots/coffee_classify.png)
![image](./demo_screenshots/medicine_classify.png)
![image](./demo_screenshots/movie_classify.png)

## Code
### loading class file at app startup
![image](./demo_screenshots/load_class.png)
### `load_class_file` function code in `analyze.py`
![image](./demo_screenshots/load_class_code.png)
### `/add-classes` and `/classes` endpoint code in `app.py`
![image](./demo_screenshots/get_add_endpoints.png)
### `get_email_classes` and `add_new_email_classes` code in `analyze.py`
![image](./demo_screenshots/get_add_functions.png)