### Entities
1. Book database (locally stored as a csv or as a python dic in-memory)
2. Borrowers (student, non-student)
3. Lenders (no classification)
4. A member can be a borrower and a borrower can be a member

#### Classes required - member (borrower, lender), book, rules
#### Methods - lend, borrow

### Rules
1. A due date for before which a book has to be returned (6 days)
2. A penalty system when a due date has lapsed (Rs 10 per day)
3. A non-refundable membership fee that has to be paid by each borrower (Rs 100 per student, Rs 300 per non-student)
    - Members are classified as student or non-student based on age (student <= 21 < non-student)
4. A maximum duration that a borrower can keep a book (30 days)

### Workflow
1. Lenders are those who donate their books free of cost
2. Borrowers are those who pay a fee for each book they borrow
3. The database will have a list of books and a flag to indicate whether the book if available or not
