ARG BUILD_FROM
FROM $BUILD_FROM

# Install dependencies for headless chromium
RUN apk add --no-cache chromium nss harfbuzz ttf-freefont

# Install Python packages
RUN pip3 install --no-cache-dir flask playwright     && playwright install chromium

WORKDIR /app
COPY run.sh /run.sh
COPY run.py /run.py
COPY options.py /options.py

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
