import pandas as pd
from faker import Faker
import csv
import random
from datetime import timedelta

fake=Faker("en_US")

def generate_customers():
 domain=["gmail.com","yahoo.com","outlook.com"]

 with open("customer.csv","w",newline="",encoding="utf-8")as file:
        writer=csv.writer(file,delimiter=";")
    #header
        writer.writerow([
            "customer_id",
            "first_name",
            "last_name",
            "date_of_birth",
            "email_address",
            "phone_number"
        ])

        for i in range(352):
            customer_id=(fake.unique.numerify(text="############"))
            first_name=(fake.first_name())
            last_name=(fake.last_name())
            date_of_birth=(fake.date_of_birth(minimum_age=18,maximum_age=85))
            email=f"{first_name.lower()}{last_name.lower()}@{random.choice(domain)}"
            phone_number=fake.numerify(text="0##########")

            writer.writerow(
                [
                    customer_id,
                    first_name,
                    last_name,
                    date_of_birth,
                    email,
                    phone_number
                ]
            )

def generate_employees():
    departments = [1,2,3,4,5,6]
    with open("employees.csv","w",newline="",encoding="utf-8")as file:
     writer=csv.writer(file,delimiter=";")
     writer.writerow(
        [
        "employee_id",
        "last_name",
        "first_name",
        "date_of_birth",
        "hire_date",
        "department_id",
        "salary"
        ]
    )
    for employee_id in range(1,41):
        first_name=fake.first_name()
        last_name=fake.last_name()
        date_of_birth=fake.date_of_birth(minimum_age=18,maximum_age=75)
        hire_date=fake.date_between(start_date="-20y",end_date="today")
        deparment_id=random.choice(departments)
        salary=random.randrange(250000,900001,10000)
        writer.writerow(
            [
                employee_id,
                last_name,
                first_name,
                date_of_birth,
                hire_date,
                deparment_id,
                salary
            ])

def generate_supplier():

    with open("suppliers.csv","w",newline="",encoding="utf-8")as file:
        writer=csv.writer(file,delimiter=";")
        #header
        writer.writerow([
            "supplier_id",
            "supplier_name",
            "start_of_contract",
            "end_of_contract",
                        ])

    for i in range(20):
        supplier_id= fake.unique.bothify(text="SUP####")
        supplier_name=fake.company()
        start_of_contract=fake.date_between(start_date="-10y",end_date="-1y")   
        contract_years = random.randint(5,10)
        end_of_contract=start_of_contract+timedelta(days=365*contract_years)
        
        writer.writerow([
                    supplier_id,
                    supplier_name,
                    start_of_contract,
                    end_of_contract,
        ])

def generate_products():
    df=pd.read_csv('products_proto.csv')
    print(df.info)

    df["product_id"] = [f"PROD{i:04d}" for i in range(1, len(df) + 1)]
    print(df.to_string)

    df.to_csv('products.csv',index=False)
    df=pd.read_csv('products.csv')

def generate_warehouse_stock():
    warehouses=['WH001','WH002','WH003'];

    new_df=pd.DataFrame({
        "product_id":df["product_id"],
        "warehouse_id":[random.choice(warehouses) for _ in range(len(df))],
        "stock_quantity": df["stock_quantity"]

    })

    print(new_df)
    new_df.to_csv('warehouse_stock.csv',index=False)

def generate_orders(): 
    customers = pd.read_csv("customer.csv",sep=";")
    products = pd.read_csv("product_availability.csv",sep=";")
    hire_date=pd.read_csv("hire_date.csv")

    print(customers.columns)
    print(products.columns)
    print(hire_date.columns)

    numbers = random.sample(range(10000, 100000), 2167)

    hire_date["hire_date"] = pd.to_datetime(
        hire_date["hire_date"])


    order_ids=[ f"ORD{number}"  for number in numbers]

    orders=[]

    for order_id in order_ids:
        order_date = pd.Timestamp(
            random.choice(
                pd.date_range(
                    start="2017-02-08",
                    end=pd.Timestamp.today()
                )
            )
        )

        eligible_employees=hire_date[
            hire_date["hire_date"]<=order_date]

        employee_id=random.choice(
            eligible_employees["employee_id"].tolist())

        customer_id=random.choice(
            customers["customer_id"].tolist())

        orders.append([
            order_id,
            order_date,
            customer_id,
            employee_id
            
        ])

    orders_df = pd.DataFrame(
        orders,
        columns=[
            "order_id",
            "order_date",
            "customer_id",
            "employee_id",
            
        ]
    )

    orders_df.to_csv(
        "orders.csv",
        index=False
    ) 

def generate_order_items():
    #van összesen 16175 darab termékünk és 2167 rendelésünk 352 vásárlóra
# az order_items táblába kell order_item_id,order_id[létező],product_id[létező],quantity[létező],unit_price[létező]

    orders=pd.read_csv("orders.csv")
    unit_info=pd.read_csv("products_availabe_and unitswprice.csv")

    # Dátumok átalakítása
    orders["order_date"] = pd.to_datetime(
        orders["order_date"]
    )

    unit_info["start_of_contract"] = pd.to_datetime(
        unit_info["start_of_contract"]
    )


    # Ide gyűjtjük az order_items sorokat
    order_items = []


    # Ide kerülnek a már felhasznált order_item_id-k
    used_item_ids = set()


    # Végigmegyünk az összes rendelésen
    for _, order in orders.iterrows():

        # Aktuális rendelés adatai
        order_id = order["order_id"]
        order_date = order["order_date"]


        # Csak azok a termékek választhatók,
        # amelyek a szerződés kezdete után 1 hónappal
        # már elérhetőek voltak
        available_products = unit_info[
            unit_info["start_of_contract"] + pd.DateOffset(months=1)
            <= order_date
        ]


        # Egy rendeléshez 2-6 különböző termék
        number_of_items = random.randint(2, 6)


        # Ha kevesebb elérhető termék van,
        # ne próbáljunk többet kiválasztani
        number_of_items = min(
            number_of_items,
            len(available_products)
        )


        # Véletlenszerű termékek kiválasztása
        selected_products = available_products.sample(
            n=number_of_items
        )


        # Végigmegyünk a kiválasztott termékeken
        for _, product in selected_products.iterrows():

            # Egyedi order_item_id generálása
            while True:

                number = random.randint(10000, 99999)

                order_item_id = f"OIID{number}"

                if order_item_id not in used_item_ids:

                    used_item_ids.add(order_item_id)

                    break


            # Véletlenszerű vásárolt mennyiség
            # 1 és az aktuális készlet között
            stock_quantity = int(product["stock_quantity"])

            quantity = random.randint(
                1,
                stock_quantity
            )


            # Order item létrehozása
            order_items.append([
                order_item_id,
                order_id,
                product["product_id"],
                quantity,
                product["unit_price"]
            ])


    # DataFrame létrehozása
    order_items_df = pd.DataFrame(
        order_items,
        columns=[
            "order_item_id",
            "order_id",
            "product_id",
            "quantity",
            "unit_price"
        ]
    )


    # CSV mentése
    order_items_df.to_csv(
        "order_items.csv",
        index=False
    )

generate_customers()
generate_employees()
generate_supplier()
generate_products()
generate_warehouse_stock()
generate_orders()
generate_order_items()