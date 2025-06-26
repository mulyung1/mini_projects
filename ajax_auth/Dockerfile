FROM nginx:stable-alpine3.20-perl

# Create cache directory and set permissions
RUN mkdir -p /usr/share/nginx/html && \
    chown -R nginx:nginx /usr/share/nginx/html

# rename the default Nginx config
RUN mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.backup

# Copy your custom nginx.conf into the container
COPY nginx.conf /etc/nginx/nginx.conf

# Copy your project files
COPY . /usr/share/nginx/html


#start nginx
CMD ["nginx", "-g", "daemon off;"]
