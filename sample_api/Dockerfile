FROM registry.access.redhat.com/ubi9/ubi-minimal
RUN microdnf install -y python3 && microdnf install -y python3-pip
WORKDIR /app
COPY ./requirements.txt . ./
RUN python3 -m pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3" ] 
CMD ["sampleAPI.py"]