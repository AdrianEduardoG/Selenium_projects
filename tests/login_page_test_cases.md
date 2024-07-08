# Login Page Test Cases

## TC001 - Test Login

### Preconditions: 

1. Open https://www.saucedemo.com
2. Available credentiales

### Test Steps:

1. Write "standard_user" in username input text
2. Write "secret_sauce" in the password input text
3. Click on Login button
### Expected Results:

1. NA
2. NA
3. Page shall be redirected to "https://www.saucedemo.com/inventory.html"


## TC002 - Test Wrong Password
## Preconditions:

1. Open https://www.saucedemo.com
2. Available username

### Test Steps:

1. Write "standard_user" in username input text
2. Write "password" in the password input text
3. Click on Login button

### Expected Results:

1. NA
2. NA
3. Page shall not redirect, shall be "https://www.saucedemo.com"

## TC003 - Test Empty Password 

### Preconditions:

1. Open https://www.saucedemo.com
2. Available credentiales

### Test Steps:

1. Write "standard_user" in username input text
2. Leave emppty the password input text
3. Click on Login button

### Expected Results:

1. NA
2. NA
3. Error message "Password is required" shall be displayed

## TC004 - Test Error Color

### Preconditions:

1. Open https://www.saucedemo.com
2. Available credentiales

### Test Steps:

1. Write "standard_user" in username input text
2. Leave emppty the password input text
3. Click on Login button

### Expected Results:

1. NA
2. NA
3. Error message shall be displayed with red color

## TC005 - Test Error closed

### Preconditions:

1. Open https://www.saucedemo.com
2. Available credentiales

### Test Steps:

1. Write "standard_user" in username input text
2. Leave empty the password input text
3. Click on Login button
4. Close the error message

### Expected Results:

1. NA
2. NA
3. NA
4. Error message shall be closed

## TC006 - Test Redirected To Login Form

### Preconditions:

1. Open https://www.saucedemo.com

### Test Steps:

1. Open "https://www.saucedemo.com/inventory.html"

### Expected Results:

1. Redirected to https://www.saucedemo.com

## TC007 - Test Redirected To Login Form Error

### Preconditions:

1. Open https://www.saucedemo.com

### Test Steps:

1. Open "https://www.saucedemo.com/inventory.html"

### Expected Results:

1. Error message "You can only access '/inventory.html' when you are logged in"

## TC008 - Test Wrong Username

### Preconditions:

1. Open https://www.saucedemo.com
2. Available Password

### Test Steps:

1. Write "user" in username input text
2. Write "secret_sauce" in password input text
3. Click on Login button

### Expected Results:

1. NA
2. NA
3. Error message "Username and password do not match any user in this service"

## TC009 - Test Empty Username

### Preconditions:

1. Open https://www.saucedemo.com
2. Available Password

### Test Steps:

1. Leave empty username input text
2. Write "secret_sauce" in password input text
3. Click on Login button

### Expected Results:

1. NA
2. NA
3. Error message "Username is required" shall be displayed