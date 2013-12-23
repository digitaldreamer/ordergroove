PROJECT=ordergroove
ROOT_DIR=$(HOME)/www
ENVS_DIR=$(HOME)/envs
PROJECT_DIR=$(ROOT_DIR)/$(PROJECT)
VIRTUALENV=$(HOME)/envs/$(PROJECT)/bin/activate
BUILD_DIR=./html/static

.PHONY: build css js

run:
	. $(VIRTUALENV); python ./manage.py runserver 0.0.0.0:8000

help:
	######################
	#
	# TARGETS
	#
	# run: runserver for development
	# runplus: runserver plus for debug
	# shell: django shell
	# shellplus: django shell plus
	# dbshell: django dbshell
	# build: build the static assets of the project
	# debug: build the static assets uncompressed
	# clean: cleans all build files
	# reload: reload the web servers
	# restart: restart the web servers
	# server: install the ubuntu server
	# virtualenv: install the virtualenv
	#
	######################

runplus:
	. $(VIRTUALENV); python ./manage.py runserver_plus 0.0.0.0:8000

shell:
	. $(VIRTUALENV); python ./manage.py shell_plus

dbshell:
	. $(VIRTUALENV); python ./manage.py db_shell

build: collectstatic
	$(MAKE) css
	$(MAKE) js

debug: collectstatic
	$(MAKE) cssdebug
	$(MAKE) jsdebug

collectstatic:
	. $(VIRTUALENV); python ./manage.py collectstatic --noinput

css:
	lessc $(BUILD_DIR)/css/styles.less > $(BUILD_DIR)/css/styles.css
	java -jar utils/yuicompressor-2.4.8.jar $(BUILD_DIR)/css/styles.css -o $(BUILD_DIR)/css/styles.min.css

cssdebug:
	lessc $(BUILD_DIR)/css/styles.less > $(BUILD_DIR)/css/styles.min.css

js:
	node $(BUILD_DIR)/js/libs/r.js -o $(BUILD_DIR)/js/build.js
	java -jar utils/yuicompressor-2.4.8.jar $(BUILD_DIR)/js/main-build.js -o $(BUILD_DIR)/js/main.min.js
	rm $(BUILD_DIR)/js/main-build.js

jsdebug:
	node $(BUILD_DIR)/js/libs/r.js -o $(BUILD_DIR)/js/build.js optimize=none
	cp $(BUILD_DIR)/js/main-build.js > $(BUILD_DIR)/js/main.min.js
	rm $(BUILD_DIR)/main-build.js

reload:
	sudo service uwsgi reload
	sudo service nginx reload

restart:
	sudo service uwsgi restart
	sudo service nginx restart

server: web postgres node virtualenv

web:
	sudo apt-get install -y openjdk-7-jdk
	sudo apt-get install -y python-software-properties
	sudo apt-get install -y libjpeg-dev
	sudo apt-get install -y nginx
	sudo apt-get install -y libpq-dev
	sudo apt-get install -y python-psycopg2
	sudo apt-get install -y sqlite3
	sudo easy_install virtualenv

postgres:
	sudo apt-get install -y libpq-dev
	sudo apt-get install -y postgresql

redis:
	sudo apt-get install -y redis-server

mongo:
	sudo apt-get install -y mongodb

node:
	sudo add-apt-repository ppa:chris-lea/node.js
	sudo apt-get update
	sudo apt-get install -y nodejs

less: node
	cd ~/; npm install less jshint

virtualenv:
	mkdir -p $(ENVS_DIR)
	cd $(ENVS_DIR); virtualenv $(PROJECT)
	. $(ENVS_DIR)/$(PROJECT)/bin/activate; pip install -Ur $(PROJECT_DIR)/requirements/requirements.txt

clean:
	rm -rf html/static
