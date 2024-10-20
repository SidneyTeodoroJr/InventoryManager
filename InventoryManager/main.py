import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import flet as ft
from modules.db_utils import *
from modules.ui_components import *

def main(page: ft.Page):
    page.title = "Admin Stock"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.scroll = ft.ScrollMode.HIDDEN

    create_table()

    items_data = []
    edit_mode = False  # Variável para controlar o modo de edição

    def remove_item(item):
        try:
            delete_item_from_db(item['id'])
            items_data[:] = [i for i in items_data if i['id'] != item['id']]
            update_page_controls()
        except Exception as ex:
            print(f"Error removing item: {ex}")

    def on_edit_item(item):
        name_field.value = item['name']
        description_field.value = item['description']
        edit_item_id.value = item['id']
        page.open(edit_modal)

    def confirm_edit_item(e):
        item_id = edit_item_id.value
        new_name = name_field.value.strip()
        new_description = description_field.value.strip()

        if new_name and new_description:
            update_item_in_db(item_id, new_name, new_description)
            for item in items_data:
                if item['id'] == item_id:
                    item['name'] = new_name
                    item['description'] = new_description
                    break
            page.close(edit_modal)
            update_page_controls()

    def remove_all_items(e):
        def confirm_delete_all(e):
            try:
                delete_all_items_from_db()
                items_data.clear()
                page.controls = [search_field]
                page.close(confirmation_modal)
                page.update()
            except Exception as ex:
                print(f"Error deleting all items: {ex}")

        confirmation_modal = ft.AlertDialog(
            title=ft.Text("Confirm Delete All"),
            content=ft.Text("Are you sure you want to delete all items?"),
            actions=[
                create_modal_button("Yes", confirm_delete_all, ft.colors.RED),
                create_modal_button("No", lambda e: page.close(confirmation_modal), ft.colors.GREEN),
            ],
        )
        page.open(confirmation_modal)

    def show_item_details(item):
        item_modal = create_item_details_modal(item, remove_item, page)
        page.open(item_modal)

    def show_confirmation_modal(item):
        confirmation_modal = create_confirmation_modal(item, remove_item, page)
        page.open(confirmation_modal)

    def add_item_to_page(item):
        items_data.append(item)
        update_page_controls()

    def update_page_controls():
        page.controls = [search_field] + [create_list_tile(i, show_item_details, show_confirmation_modal, on_edit_item, edit_mode) for i in items_data]
        page.update()

    def show_bottom_sheet(e):
        modal_user = create_add_item_modal(add_item_to_page, page)
        page.open(modal_user)

    def search_items(e):
        search_term = search_field.value.strip().lower()
        filtered_items = [item for item in items_data if search_term in item['name'].lower() or search_term in item['description'].lower()]
        page.controls = [search_field] + [create_list_tile(i, show_item_details, show_confirmation_modal, on_edit_item, edit_mode) for i in filtered_items]
        page.update()

    search_field = ft.TextField(
        hint_text="Search items...",
        prefix_icon=ft.icons.SEARCH,
        border_radius=ft.border_radius.all(30),
        on_change=search_items,
    )

    page.appbar = ft.CupertinoAppBar(
        bgcolor=ft.colors.GREEN,
        middle=ft.Text("Stock Management", color=ft.colors.WHITE),
    )
    
    edit_button = ft.IconButton(
        icon=ft.icons.EDIT_NOTE_OUTLINED, 
        icon_color=ft.colors.WHITE, 
        on_click=lambda e: toggle_edit_mode()
    )

    def toggle_edit_mode():
        nonlocal edit_mode
        edit_mode = not edit_mode  # Alternar o modo de edição
        edit_button.icon = ft.icons.CHECKLIST_RTL_SHARP if edit_mode else ft.icons.EDIT_NOTE_OUTLINED  # Mudar o ícone
        update_page_controls()  # Atualizar a página para refletir as alterações

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        on_click=show_bottom_sheet
    )
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.GREEN_700,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                edit_button,  # Botão de edição
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.DELETE_SWEEP_ROUNDED, icon_color=ft.colors.WHITE, on_click=remove_all_items),
            ]
        ),
    )

    # Modal para editar itens
    name_field = ft.TextField(label="Name")
    description_field = ft.TextField(label="Description")
    edit_item_id = ft.TextField(visible=False)  # Para armazenar o ID do item que será editado

    edit_modal = ft.AlertDialog(
        title=ft.Text("Edit Item"),
        content=ft.Column(
            width=300,
            height=100,
            controls=[name_field, description_field],
        ),
        actions=[
            create_modal_button("Save", confirm_edit_item, ft.colors.GREEN),
            create_modal_button("Cancel", lambda e: page.close(edit_modal), ft.colors.RED),
        ],
    )

    # Carregar itens do banco de dados e exibi-los
    items_data[:] = get_items_from_db()
    update_page_controls()

ft.app(target=main)