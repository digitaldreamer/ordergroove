upstream ordergroove_backend {
  #server 127.0.0.1:8080;
  server unix:///var/run/uwsgi_ordergroove.socket;
}

server {
	listen 80;
	server_name ordergroove.digitaldreamer.net;

	access_log  /var/log/nginx/ordergroove.access.log;
	error_log  /var/log/nginx/ordergroove.error.log;

	location / {

		# auth_basic "Restricted";
		# auth_basic_user_file /home/poyzer/www/ordergroove/nginx/.htpasswd;

		#proxy_pass http://ordergroove_backend;
		#include /etc/nginx/proxy.conf;
		try_files $uri @proxy_to_app;
	}

	location @proxy_to_app {
		uwsgi_pass ordergroove_backend;
		include uwsgi_params;
		uwsgi_param UWSGI_SCHEME $scheme;
	}

	location ~ /(static|media) {
		root   /home/poyzer/www/ordergroove/html;
		#index  index.html index.htm;
	}
}
