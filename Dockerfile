FROM python:3.10-buster 

# install nginx 
RUN apt-get update && apt-get install nginx -y --no-install-recommends 
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log
COPY nginx.default /etc/nginx/sites-available/default 

# copy source to /opt/app 
WORKDIR /opt/app 
COPY . ./ 
RUN mkdir ./pip_cache; pip3 install -r requirements.txt --cache-dir ./pip_cache \
    && chown -R www-data:www-data /opt/app; chmod 777 -R /root

ENV NUMBA_CACHE_DIR="/tmp"

EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]


