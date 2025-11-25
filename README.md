#### Build Automation Code for Sigma Smart Goal

## Run the API code

## 🛠️ 1. Install Dependencies

Make sure you have:

```
Python 3.9+
pip
Docker Desktop or Colima
```

Install Python dependencies:
```
> pip install -r requirements.txt
```

## ▶️ 2. Run the Application Locally

Inside the project root:

```
> export FLASK_APP=src/app.py
> flask run
```

The API will be available at:

```
> http://127.0.0.1:5000
```

## 🧪 3. Run Unit Tests

```
> PYTHONPATH=. pytest
```

## 🐳 4. Build the Docker Image

````
> docker build -t ci-cd-demo .
````

## ▶️ 5. Run the Docker Container
````
> docker run -p 5000:5000 ci-cd-demo
````

The API can be found at:
```
> http://127.0.0.1:5000
```

-------------

## 🔄 CI Pipeline (GitHub Actions)

The file at:
````
.github/workflows/ci.yml
````

Executes the following steps every push and pull request automatically.

- Checkout code

- Install Python dependencies

- Run tests

- Run lint

- Build Docker image

- Save Docker image into artifact: ci-cd-demo.tar

## 🚀 CD Pipeline (Mock Jenkins)

The Jenkinsfile simulates:

- Download CI artifact

- Load the Docker image:
````
> docker load -i ci-cd-demo.tar
````

- Stop old container (mock ECS behavior)

- Start the new deployed version:
````
> docker run -d -p 5000:5000 ci-cd-demo
````

This simulates:

* ECS blue/green behavior
* No AWS account is required. Everything runs locally.
