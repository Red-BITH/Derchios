import phonenumbers
from phonenumbers import carrier, timezone, geocoder

def clear_console():

    import os

    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def main():
    clear_console()
    print("\033[34mCyberDark.Org ---> RED-BITH /Telefon nom. scan/")
    number = input("Telefon nömrəsini girin--->")

    if number.startswith("+"):
        try:
            parsed_number = phonenumbers.parse(number, None)
            if phonenumbers.is_valid_number(parsed_number):
                print("Yazılan nömrə doğrudur.")
                time_zones = timezone.time_zones_for_number(parsed_number)
                carrier_name = carrier.name_for_number(parsed_number, "az")
                region = geocoder.description_for_number(parsed_number, "az")

                print("Sim Şəbəkəsi:", carrier_name)
                print("Nömrənin Ölkəsi:", region)
                print("Nömrənin Bölgəsi:", time_zones)

            else:
                print("Yazılan nömrə səhvdir!")
        except phonenumbers.phonenumberutil.NumberFormatException:
            print("Xətalı nömrə formatı.")
    else:
        print("+Ölkə kodunu yazmaği unutdunuz!.")

if __name__ == "__main__":
    main()
