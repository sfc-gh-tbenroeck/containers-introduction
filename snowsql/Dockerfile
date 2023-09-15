# https://docs.snowflake.com/en/user-guide/snowsql-install-config

# Use a base image with necessary utilities
FROM ubuntu:latest

# Update and Install necessary packages and utilities
RUN apt-get update && \
    apt-get install -y curl gnupg unzip

# Download the SnowSQL installer script and signature
RUN curl -O https://sfc-repo.snowflakecomputing.com/snowsql/bootstrap/1.2/linux_x86_64/snowsql-1.2.28-linux_x86_64.bash && \
    curl -O https://sfc-repo.snowflakecomputing.com/snowsql/bootstrap/1.2/linux_x86_64/snowsql-1.2.28-linux_x86_64.bash.sig

# Download Snowflake GPG public key and import it
RUN gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 630D9F3CAB551AF3

# Verify the package signature
RUN gpg --verify snowsql-1.2.28-linux_x86_64.bash.sig snowsql-1.2.28-linux_x86_64.bash

# Set environment variables for automated install
ENV SNOWSQL_DEST /usr/local/bin
ENV SNOWSQL_LOGIN_SHELL /root/.bashrc

# Install SnowSQL
RUN bash snowsql-1.2.28-linux_x86_64.bash

# Clean up
RUN rm snowsql-1.2.28-linux_x86_64.bash snowsql-1.2.28-linux_x86_64.bash.sig

# Set entrypoint to SnowSQL
ENTRYPOINT ["snowsql"]
