# SafeBlood

## Overview
SafeBlood is a blood donation platform built using Django and Django REST Framework. It connects blood donors with those in need of blood. Donors can submit their donation information, and users can accept requests to donate blood.

## Features

### User Functionality
- **User Authentication**: Register, login, and logout functionalities.
- **Profile Management**: Donors can create and update their profiles.
- **Donation Requests**: Users can submit blood donation requests and track ongoing requests.
- **Accept/Cancel Requests**: Users can accept or cancel blood donation requests.
- **Donation History**: View history of past donations.

## API Endpoints

### Authentication Endpoints
- **POST /register/**: Register a new user.
- **POST /login/**: User login.
- **POST /logout/**: User logout.
- **GET /active/<uid64>/<token>/**: Activate user account via email link.

### Donor Endpoints
- **GET /profile/**: Retrieve donor profile.
- **PATCH /update-profile/<int:pk>/**: Update donor profile by ID.
- **GET /list/**: List all donors.
- **GET /details/<int:pk>/**: Get details of a specific donor.
- **POST /accept-request/<int:id>/**: Accept a blood donation request by ID.
- **POST /cancel-request/<int:id>/**: Cancel a blood donation request by ID.
- **GET /donation-history/**: View donation history.
- **GET /bloods/**: List available blood types.

### Blood Request Endpoints
- **POST /blood-request/**: Submit a new blood donation request.
- **GET /blood-request-list/**: List all blood donation requests.
- **GET /ongoing-requests/**: List all ongoing blood donation requests.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sakayat/blood_bank_backend.git
   cd safeblood
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the server:
   ```bash
   python manage.py runserver
   ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to submit issues and pull requests for enhancements or bug fixes!
