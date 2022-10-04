# Денис

import operations as o
from operations import contact_list
import user_interface as ui


def button_click():
    ui.greetings_user()
    while True:
        menu = ui.show_menu()
        choice = ui.get_choice(menu)
        if choice == 1:
            contact = ui.add_contact()
            o.add_contact(contact)
        elif choice == 2:
            searchstring = ui.get_action('Введите данные для поиска: ')
            searched_contact = o.search_contact(searchstring)
            ui.view_dict(searched_contact)
            choice = ui.get_choice_contact('Введите номер контакта: ',searched_contact) 
            selected_contact = o.select_contact(choice, searched_contact)
            ui.view_contact(selected_contact)
            menu_s = ui.menu_search()            
            choice = ui.get_choice(menu_s)
            if choice == 1:
                ui.edit_user_contact(searched_contact)
                o.delete_contact(selected_contact[0])
                contact = ui.add_contact()
                o.add_contact(contact)
                ui.change_user_contact(contact)
            elif choice == 2:
                o.delete_contact(selected_contact[0])
                ui.delete_user_contact(selected_contact)
        elif choice == 3:
            ui.view_data(contact_list)
        elif choice == 4:
            ui.message_read_csv()
            o.read_csv()
            ui.view_data(contact_list)  
        elif choice == 5:
            ui.message_write_csv()
            o.write_csv()
            ui.view_data(contact_list)
        elif choice == 6:
             o.write_json() 
        else:
            ui.farewell_user()
            break
