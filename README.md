Restaurant Menu Web Application (Cloud Deployment)

This project is a Flask-based restaurant menu web application that allows users to browse menu items, select quantities, and generate an order summary with total price.

---

Features

- Browse restaurant menu items
- Select item quantities
- Generate order summary with total price
- Responsive HTML interface
- Health check endpoint for monitoring

---

Technologies Used

- Python (Flask)
- HTML / CSS
- Docker
- GitHub
- GitHub Actions (CI/CD)
- Microsoft Azure App Service

---

Cloud Deployment Architecture

Developer → GitHub Repository → GitHub Actions CI/CD → Docker Build → Azure App Service → Live Web Application

---

Health Check Endpoint

The application includes a monitoring endpoint:

"/health"

Example response:

{"status":"running"}

---

Live Application

https://surya-menu-app.azurewebsites.net

---

How the Application Works

1. User opens the Menu page
2. Selects quantities for menu items
3. Clicks "Place Order"
4. Application calculates total price
5. Order summary is displayed

---

CI/CD Pipeline

This project uses GitHub Actions for Continuous Integration and Continuous Deployment.

Pipeline workflow:

1. Developer pushes code to GitHub repository
2. GitHub Actions pipeline automatically triggers
3. Application dependencies are installed
4. Docker container is built
5. Application is deployed to Azure App Service
6. Live web application is updated automatically

---

Author

Surya S
