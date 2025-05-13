ARG BUILD_FROM
FROM $BUILD_FROM

# Install dependencies
RUN apt-get update && apt-get install -y \
    chromium libnss3 libatk1.0-0 \
    libatk-bridge2.0-0 libcups2 libdrm2 libgbm1 libgtk-3-0 \
    libpango-1.0-0 libxcomposite1 libxdamage1 libxrandr2 libxss1 libxtst6 \
    nodejs npm && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip3 install --no-cache-dir flask playwright && \
    playwright install chromium

# Copy addon files
WORKDIR /app
COPY run.sh /run.sh
COPY run.py /run.py
COPY options.py /options.py

RUN chmod a+x /run.sh

# Run the addon
CMD [ "/run.sh" ]
