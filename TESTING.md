## Testing

### Manual Testing

The application was manually tested to ensure that all features functioned as expected. 
The following tests were completed:

![Testing Menu](README.images/test-menu.png)

The above screenshot demonstrated input validation and successful programme execusion.

### PEP8 Validation

### User Story Testing

#### Bugs Encountered and Fixes
During development, several issues were identified through manual testing and were successfully resolved.

- The application originally crashed if a user entered letters instead of a record number when deleting a training record. This was resolved by validating that the input contains only numeric values before converting it to an integer.

- Initially, users could enter blank employee names and training names. Input validation was added to ensure these fields cannot be left empty.

- Training status was originally free text, allowing inconsistent values to be stored. Validation was added so only **Completed**, **In Progress**, or **Not Started** can be entered.

- A bug occurred when deleting records because the incorrect Google Sheets method was used ('delete_row'). This was corrected by using the 'delete_rows()' method.

- Initially, users could enter a record number that did not exist when deleting records. Additional validation was implemented to ensure only displayed records can be deleted.

#### Remaining Bugs

No known bugs remain at the time of submission.
