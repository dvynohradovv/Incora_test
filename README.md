# **MyUser Django Rest Framework**
# **Create RESTful API:**

***

1. `/users POST` - create user with the next fields: first_name (required, only letters),
last_name (only letters), email (required, unique, correct format), phone (correct format),
password (hash)
![image](https://user-images.githubusercontent.com/55922843/158596901-72a32558-88bc-4534-b1ad-5930a7f4e85b.png)


2. `/login POST` - create API for user login by email and password. Use JWT authentication
![image](https://user-images.githubusercontent.com/55922843/158596954-ef57bb90-d056-46ea-9e13-8d2915dfdcac.png)


4. `/users/:id GET` - get 1 user by id.
![image](https://user-images.githubusercontent.com/55922843/158597100-02042c35-e147-4e99-8332-489876a72b6d.png)


6. `/users/:id PUT` - update user, add validation. Connect Socket.IO for sending push
notifications after user update.
![image](https://user-images.githubusercontent.com/55922843/158597164-d21b88de-cb03-489c-9055-8cee65dee98c.png)

