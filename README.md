# Reservation-API

>Company needs an internal service for its employees which helps them to reserve company
meeting rooms for internal or external meetings. Each employee should be able to check each
room’s availability, book or cancel a reservation through an API.


## Technologies
  * Django
  * Django REST framework
  * Djoser
  * PostgreSQL
  * Postman

## TO-DO list
  * CREATE reservation
  * GET all reservation
  * GET details reservation
  * CANCEL reservation


## Testing API
* Create user:
   ```sh
   http://127.0.0.1:8000/api/v1/reservations/users/
   ```
* Get token:
   ```sh
   http://127.0.0.1:8000/api/v1/reservations/token/login
   ```
* Autharization with token:
   ```sh
   http://127.0.0.1:8000/api/v1/reservations/restricted';
   ```
   
## Contact
Created by [@aurimas](https://www.linkedin.com/in/aurimas-butkevicius-79718a161/) - feel free to contact me!
