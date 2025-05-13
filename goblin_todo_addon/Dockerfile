ARG BUILD_FROM
FROM $BUILD_FROM

# Install dependencies
RUN apk add --no-cache python3 py3-pip chromium nss

# Install Python packages
RUN pip3 install flask playwright && \
    playwright install --with-deps chromium

# Copy addon files
COPY run.sh /run.sh
COPY run.py /run.py
COPY options.py /options.py

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
