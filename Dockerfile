# 1. base Python image
FROM python:3.11-slim

# 2. working directory inside container
WORKDIR /app

# 3. copy your entire project into the container
COPY . .

# 4. install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. expose Streamlit port
EXPOSE 8501

# 6. run the app when the container starts
CMD ["streamlit", "run", "app/app.py", "--server.headless=true"]
