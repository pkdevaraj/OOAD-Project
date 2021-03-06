##**Readme**

####Project Title
Cab Sharing with people from same locality travelling to the same destination.
#####Description
A platform to share the cab with other users in the same locality looking for cab in
the same time and travelling to the same destination.This takes multiple bookings and finds the
shortest path to pick up all the users and split the fare among the users.

###Pre-requisites for Server
* Install MongoDB  from [here](https://docs.mongodb.org/manual/installation/)
* Install Pymongo frem [here](https://api.mongodb.org/python/current/installation.html)

###Pre-requisites for Client
* Install Android Studio  from [here](http://developer.android.com/sdk/installing/index.html)
* Install Java 1.6 or higher frem [here](https://java.com/en/download/)
* Generate Google Maps API Key from [here](https://developers.google.com/maps/documentation/javascript/get-api-key#get-an-api-key)
* Android Device has to be above API 18 for Maps to work as expected
* Enable Developer options on the android device to install the application

## BUILDING and RUNNING THE CODE

* Download the android code and import the project into Android Studio
* Start an instance of Mongodb by running "sudo mongod" command
* Download the Server Code and run cabSharing.py using "python cabSharing.py" command
* Enter the API key in AndroidManifest.xml file and build and install the application on the target device.

##Authors
* Mohammad Hashemi
* Praveen Kumar Devaraj
* Nachiket Bhagawat
