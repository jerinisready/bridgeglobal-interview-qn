Milli Order
---

MilliOrder is a project for Interview From BridgeGlobal, 
with the problem statement below.

> 
>    Hello Jerin,
>
>    As discussed, the client shared a tech challenge task, and PFB the details.
>
>    As a next step we'd like to send a tech challenge, with the following brief:
>
>    Take the following example schema:
>
>    - Model: Order
>       - Field: ID
>    - Model: OrderStatus
>       - Field: ID
>       - Field: Created (DateTime)
>       - Field: Status (Text: Pending/Complete/Cancelled)
>       - Field: OrderID (ForeignKey)
>
>    We have a database of many Orders, and each Order has one or many OrderStatus records. 
>    Each OrderStatus row has columns for created datetime and a status of Pending/Complete/Failed. 
>    The status of every Order in the database is dictated by the most recent OrderStatus. 
>    A `Pending` OrderStatus will be created for an Order when it is first created, `Complete` 
>    OrderStatus is created after successful payment or `Cancelled` is created if payment fails, 
>    or also if a `Complete` Order is refunded it is also given status `Cancelled`.
> 
>    Using the Django ORM, how would you structure a query to list all `Cancelled` orders in the 
>    database without changes to the schema. Given that the database may contain millions of 
>    Orders, what optimisations would you suggest to make through the use of other query 
>    techniques, technologies or schema changes to reduce burden on the database resources 
>    and improve response times.
> 
>    Please use Django / Python for your solution. The logic and thought process demonstrated
>    are the most important considerations rather than truly functional code, however code 
>    presentation is important as well as the technical aspect. If you cannot settle on a
>    single perfect solution, you may also discuss alternative solutions to demonstrate your
>    understanding of potential trade-offs as you encounter them. Of course if you consider a
>    solution is too time consuming you are also welcome to clarify or elaborate on potential
>    improvements or multiple solution approaches conceptually to demonstrate understanding
>    and planned solution.
> 
>    Please advise once Jerin has reviewed the challenge when we should expect his solution, 
>    ideally however we could have it early next week if possible.

---

# RUN CODE
- Create virtualenv with Python3.9  (SQLITE3 Connected)

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py generateorders`    # this will take around 6-8 minutes to get the data.

`python manage.py runserver`


Now go to link: http://localhost:8000/api/v1/orders/cancelled/

Now go to link: http://localhost:8000/api/v1/orders/cancelled/?page=2

Now go to link: http://localhost:8000/api/v1/orders/cancelled/?page=3


