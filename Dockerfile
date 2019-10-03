FROM httpd:2.4
COPY ./apache_settings/httpd.conf /usr/local/apache2/conf/httpd.conf
COPY ./apache_settings/httpd-ssl.conf /usr/local/apache2/conf/extra/httpd-ssl.conf
COPY ./ssl_certificates/ /usr/local/apache2/conf/
COPY ./www /usr/local/apache2/htdocs
