def insert_patient_data(name, age):

    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("age can't be negative")
        else:
            print(age)
            print(name)
            print("inserted in to database")
    
    else:
        raise TypeError("Incorrect Data type")


def update_patient_data(name, age):

    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("age can't be negative")
        else:
            print(age)
            print(name)
            print("Updated")
    
    else:
        raise TypeError("Incorrect Data type")


insert_patient_data("nitish", "thirty")