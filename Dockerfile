# Use a base image
FROM nginx:latest

# Copy your HTML files to the appropriate location in the image
COPY ./site /usr/share/nginx/html/

