while True:
    result = {}
    phone_number = input("Введите номер телефона в международном формате: ")
    if len(phone_number) != 13:
        result["success"] = False
        result["description"] = "Phone number should contains only 13 symbols"
        print(result)
    if phone_number[0] != "+":
        result["success"] = False
        result["description"] = "Phone number should starts with +"
        print(result)
    for char in phone_number[1:13:1]:
        if not char.isdigit():
            result["success"] = False
            result["description"] = "Phone number\
                should contains digits after +"
            print(result)
        break
    if phone_number[1:4] != "375":
        result["success"] = False
        result["description"] = "The code of the country should be 375"
        print(result)
    if phone_number[4:6] not in ["25", "29", "33", "44"]:
        result["success"] = False
        result["description"] = "The code of the operator\
            should be 25, 29, 33, 44"
        print(result)
    if phone_number[4:6] == "25":
        result["success"] = True
        result["phone"] = phone_number
        result["operator"] = "Life:)"
        print(result)
    if phone_number[4:6] == "33":
        result["success"] = True
        result["phone"] = phone_number
        result["operator"] = "MTC"
        print(result)
    if phone_number[4:6] == "44":
        result["success"] = True
        result["phone"] = phone_number
        result["operator"] = "A1"
        print(result)
    if phone_number[4:6] == "29":
        if phone_number[7:8] in ["1", "3", "6", "9"]:
            result["success"] = True
            result["phone"] = phone_number
            result["operator"] = "A1"
            print(result)
        elif phone_number[7:8] in ["2", "5", "7", "8"]:
            result["success"] = True
            result["phone"] = phone_number
            result["operator"] = "MTC"
            print(result)
    exit_choice = input("Хотите проверить ещё один номер Y/N: ")
    if exit_choice == "N":
        break
