FROM python:latest
WORKDIR /myapp_folder
COPY requirements.txt myapp.py /myapp_folder/
RUN pip install -r requirements.txt
EXPOSE 8060
# VOLUME ["/myapp_folder/volumns_folder"]
CMD ["uvicorn", "myapp:app", "--host", "0.0.0.0", "--port", "8060", "--reload"]

