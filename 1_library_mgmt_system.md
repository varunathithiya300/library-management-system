Here’s a **basic-level system design problem statement** that’s perfect for practicing **OOP fundamentals** (classes, objects, inheritance, encapsulation, polymorphism, relationships):


## 📚 Problem Statement: Library Management System (Basic)

Design a simple **Library Management System** using OOP concepts.

### Requirements

1. The system should allow:

   * Adding **Books** (with attributes: title, author, ISBN, availability).
   * Adding **Members** (with attributes: name, member ID, contact info).
   * Issuing and returning books.

2. Rules:

   * A book can be either **available** or **issued**.
   * A member can borrow up to **3 books at a time**.
   * When a book is issued, its status changes to **not available**.
   * When returned, the status updates back to **available**.

3. Classes you might design:

   * `Book`
   * `Member`
   * `Library` (manages collections of books & members)
   * Optionally `Transaction` (to track issue/return history).


### 💡 OOP Concepts to Practice

* **Encapsulation** → Keep book/member details private, expose methods like `issue_book()`, `return_book()`.
* **Inheritance** → You could extend `Member` into `StudentMember` or `FacultyMember` with different borrowing limits.
* **Polymorphism** → Same `issue_book()` behavior but slightly different rules per member type.
* **Abstraction** → Define clear interfaces/methods for actions like `search_book()`, `add_member()`.
* **Composition** → `Library` *has* `Books` and `Members`.


👉 This problem is small enough to code in a day but flexible enough to scale (e.g., add reservations, late fees, digital media).

Would you like me to also **draft a class diagram (UML-style)** for this, so you can visualize the OOP structure before coding?
