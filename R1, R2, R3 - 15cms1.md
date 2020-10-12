
#### Test case R1.9 - For any formatting errors, render the login page and show the message 'email/password format is incorrect.'
Mocking:

-   None required.

Actions:

-   open /logout (to invalid any logged-in sessions that may exist)
-   open /login
-   enter any email into element  `#email`
-   enter any password into element  `#password`
-   click element  `input[type="submit"]`
-   validate the email format based on Test Case R1.7.
- validate the password complexity based on Test Case R1.8.
- if either validation fails,  open /login again
-   validate that current page contains  `#email` and `#password` elements
-  display a notification "Email/Password format is Incorrect"

#### Test case R1.10 - If email/password are correct, redirect to /
Mocking:

-   Mock backend.get_user to return a test_user instance

Actions:

-   open /logout (to invalid any logged-in sessions that may exist)
-   open /login
-   enter test user's email into element  `#email`
-   enter test user's password into element  `#password`
-   click element  `input[type="submit"]`
- validate if Test Case R1.9 passes, ensuring there were no formatting issues in the entered email and password
-   open /login again
-   validate that current page contains  `#welcome-header` and `#tickets` elements

#### Test case R1.11 - Otherwise, redict to /login and show message 'email/password combination incorrect'
Mocking:

-   Mock backend.get_user to return a test_user instance

Actions:

-   open /logout (to invalid any logged-in sessions that may exist)
-   open /login
-   enter test user's email into element  `#email`
-   enter test user's password into element  `#password`
-   click element  `input[type="submit"]`
-   open /login again
-   validate that current page contains  `#email` and `#password` elements
- validate if Test Case R1.9 passes, ensuring there were no formatting issues in the entered email and password
- if R1.9 passes, display a notification, 'Email/Password Combination is Incorrect’

#### Test case R2.9 - For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)
Mocking:

-   None required.

Actions:

-   open /logout (to invalid any logged-in sessions that may exist)
-   open /register
-   enter email into element  `#email`
- enter username into element `#name`
-   enter password into element  `#password`
- enter password again into element `#password2`
-   click element  `input[type="submit"]`
-   validate the formats on all four of the above attributes with their corresponding test cases R2.5, R2.6, R2.7, and R2.8.
- if any of the validation fails,  open /login again
- validate that current page contains  `#email`, `#name`, `#password`, and `#password2` elements.
- display an attribute-specific notification, based on the validation that failed, "`Attribute` format is Incorrect."

#### Test case R2.10 - If the email already exists, show message 'this email has been ALREADY used'

Mocking:

-   Mock backend.get_user to return a test_user instance

Actions:
-   open /logout (to invalid any logged-in sessions that may exist)
-   open /register
-   enter email into element  `#email`
- enter username into element `#name`
-   enter password into element  `#password`
- enter password again into element `#password2`
-   click element  `input[type="submit"]`
-   validate that test case R2.9 passes for the formatting of these attributes.
-  compare test user's email and the email entered in the `email` element.
- if the two match, re-open /register, validate that the current page contains  `#email`, `#name`, `#password`, and `#password2` elements, and display notification, "this email has been ALREADY used".

#### Test case R2.11 - If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page

Assumptions:

- The User model will have a balance attribute (possibly as a float)
- The Backend implementation will have an endpoint `update_user_balance` that will take as params a user's e-mail and a float value and set the user's balance attribute as the passed in float value.

Mocking:

-   Mock backend.register_user to register a new user instance
- Mock backend.update_user_balance to update the balance of the newly created user 
- The `/` route (i.e. `index.html`) will have a `div` with the id as `#balance`. This will display the logged in user's in-app balance (R3.3).

Actions:
-   open /logout (to invalid any logged-in sessions that may exist)
-   open /register
-   enter email into element  `#email`
- enter username into element `#name`
-   enter password into element  `#password`
- enter password again into element `#password2`
-   click element  `input[type="submit"]`
-   validate that test case R2.9 passes for the formatting of these attributes.
-  validate that test case R2.10 passes for no conflicting email.
- use the validated values on `#email`, `#name`, `#password`, and `#password2` elements to register a user instance through the mocked `register_user` end-point.
-  Update the balance of this user to 5000 through the mocked `update_user_balance` endpoint.
- open the /login page
- validate that current page contains  `#email` and `#password` elements
- display notification "You have successfully registered. Please proceed with the login."

#### Test case R3.8  - The ticket-selling form can be posted to /sell

Assumptions:

- The ticket-selling form is on the `/ (index.html)` route with id `#ticket-sell`

Mocking:

-   Mock backend.get_user to return a test_user instance

Actions:
-   open /logout (to invalid any logged-in sessions that may exist)
-   login to the application by entering test user credentials, validate based on R1.10.
- validate that the page contains a form element with id `#ticket-sell`
- validate that the attribute `action` is defined on this element with value as `/sell`
- validate that the attribute `method` is defined on this element with value as `post`

#### Test case R3.9  -The ticket-buying form can be posted to /buy
Assumptions:

- The ticket-buying form is on the `/ (index.html)` route with id `#ticket-buy`

Mocking:

-   Mock backend.get_user to return a test_user instance

Actions:
-   open /logout (to invalid any logged-in sessions that may exist)
-   login to the application by entering test user credentials, validate based on R1.10.
- validate that the page contains a form element with id `#ticket-buy`
- validate that the attribute `action` is defined on this element with value as `/buy`
- validate that the attribute `method` is defined on this element with value as `post`


#### Test case R3.10  -The ticket-update form can be posted to /update
Assumptions:

- The ticket-update form is on the `/ (index.html)` route with id `#ticket-update`

Mocking:

-   Mock backend.get_user to return a test_user instance

Actions:
-   open /logout (to invalid any logged-in sessions that may exist)
-   login to the application by entering test user credentials, validate based on R1.10.
- validate that the page contains a form element with id `#ticket-update`
- validate that the attribute `action` is defined on this element with value as `/update`
- validate that the attribute `method` is defined on this element with value as `post`