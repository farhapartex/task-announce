# Task Announce

You can manage your all tasks by using `Task Announce`. To use follow some instructions:

## Installation:

* Clone this project in your computer

* Create your virtual environment and turn on it. Install all packages from requirements.txt file which would be found in the root folder. If you are familiar with `pipenv` you can run `pipenv install`

* Install RabbitMQ server. For linux user, you can follow below steps:
    * `sudo apt-get install rabbitmq-server`
    * `sudo rabbitmqctl add_user myuser mypassword`
    * `sudo rabbitmqctl add_vhost myvhost`
    * `sudo rabbitmqctl set_user_tags myuser mytag`
    * `sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"`

    Substitute in appropriate values for `myuser`, `mypassword` and `myvhost` above


## Use
* Open terminal and run RabbitMQ server by `sudo rabbitmq-server`
* If running server create some problem stop it by `sudo rabbitmqctl stop` and again run it by `sudo rabbitmq-server`
* Open another terminal in the project root folder and turn on your virtual environment
* To add tasks run `python3 init.py tasks`. Type your tasks one by one with time. Time pattern in `HH:MM am/pm`. To stop providing task provide `stop` as task name.
* To start task-announce run `python3 init.py up`