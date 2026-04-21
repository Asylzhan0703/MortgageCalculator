from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout


KV = '''
<ItemDrawer>:
    theme_text_color: "Custom"
    text_color: root.text_color

    IconLeftWidget:
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/logo3-min.png"

    MDLabel:
        id: app_title_label
        text: app.title
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1

    MDLabel:
        id: app_author_label
        text: app.by_who
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 0.7

    ScrollView:
        DrawerList:
            id: md_list


<Tab>:
    BoxLayout:
        orientation: "vertical"

        Widget:


Screen:
    MDNavigationLayout:

        ScreenManager:
            Screen:

                BoxLayout:
                    orientation: "vertical"

                    MDToolbar:
                        id: toolbar
                        title: app.title
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["star-outline", lambda x: app.on_star_click()]]
                        md_bg_color: 0, 0, 0, 1
                        specific_text_color: 1, 1, 1, 1

                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        tab_indicator_anim: False
                        background_color: 0.1, 0.1, 0.1, 1

                        Tab:
                            id: tab_input
                            icon: "calculator-variant"
                            title: "Input"

                            BoxLayout:
                                id: input_box
                                orientation: "vertical"
                                padding: "14dp"
                                spacing: "14dp"

                                BoxLayout:
                                    orientation: "horizontal"
                                    size_hint_y: None
                                    height: "56dp"
                                    spacing: "8dp"

                                    MDIconButton:
                                        id: icon_date
                                        icon: "calendar-month"
                                        theme_text_color: "Custom"
                                        text_color: 1, 1, 1, 1

                                    MDTextField:
                                        id: start_date
                                        hint_text: "Start date"
                                        color_mode: "custom"

                                BoxLayout:
                                    orientation: "horizontal"
                                    size_hint_y: None
                                    height: "56dp"
                                    spacing: "8dp"

                                    MDIconButton:
                                        id: icon_loan
                                        icon: "cash"
                                        theme_text_color: "Custom"
                                        text_color: 1, 1, 1, 1

                                    MDTextField:
                                        id: loan
                                        hint_text: "Loan"
                                        input_filter: "float"
                                        color_mode: "custom"

                                BoxLayout:
                                    orientation: "horizontal"
                                    size_hint_y: None
                                    height: "56dp"
                                    spacing: "8dp"

                                    MDIconButton:
                                        id: icon_months
                                        icon: "clock-time-five-outline"
                                        theme_text_color: "Custom"
                                        text_color: 1, 1, 1, 1

                                    MDTextField:
                                        id: months
                                        hint_text: "Months"
                                        input_filter: "int"
                                        color_mode: "custom"

                                BoxLayout:
                                    orientation: "horizontal"
                                    size_hint_y: None
                                    height: "56dp"
                                    spacing: "8dp"

                                    MDIconButton:
                                        id: icon_interest
                                        icon: "bank"
                                        theme_text_color: "Custom"
                                        text_color: 1, 1, 1, 1

                                    MDTextField:
                                        id: interest
                                        hint_text: "Interest, %"
                                        input_filter: "float"
                                        color_mode: "custom"

                                    MDTextField:
                                        id: payment_type
                                        hint_text: "Payment type"
                                        text: "annuity"
                                        color_mode: "custom"

                                Widget:

                        Tab:
                            id: tab_table
                            icon: "table-large"
                            title: "Table"

                            BoxLayout:
                                id: table_box
                                orientation: "vertical"
                                padding: "16dp"

                                MDLabel:
                                    id: table_label
                                    text: "Table"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1

                        Tab:
                            id: tab_graph
                            icon: "chart-areaspline"
                            title: "Graph"

                            BoxLayout:
                                id: graph_box
                                orientation: "vertical"
                                padding: "16dp"

                                MDLabel:
                                    id: graph_label
                                    text: "Graph"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1

                        Tab:
                            id: tab_chart
                            icon: "chart-pie"
                            title: "Chart"

                            BoxLayout:
                                id: chart_box
                                orientation: "vertical"
                                padding: "16dp"

                                MDLabel:
                                    id: chart_label
                                    text: "Chart"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1

                        Tab:
                            id: tab_sum
                            icon: "book-open-variant"
                            title: "Sum"

                            BoxLayout:
                                id: sum_box
                                orientation: "vertical"
                                padding: "16dp"

                                MDLabel:
                                    id: sum_label
                                    text: "Sum"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
'''


class Tab(MDFloatLayout, MDTabsBase):
    title = StringProperty("")
    icon = StringProperty("")


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty([1, 1, 1, 1])

    def on_release(self):
        app = MDApp.get_running_app()
        if self.text == "Dark/Light":
            app.toggle_theme()
        self.parent.set_color_item(self)


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        for item in self.children:
            item.text_color = self.theme_cls.text_color
        instance_item.text_color = self.theme_cls.primary_color


class MortgageCalculatorApp(MDApp):
    title = "Mortgage Calculator"
    by_who = "author Olke Asylzhan"

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        root = Builder.load_string(KV)
        Clock.schedule_once(self.refresh_ui_colors, 0.2)
        return root

    def on_start(self):
        menu_items = {
            "account-cowboy-hat": "About author",
            "youtube": "My YouTube",
            "coffee": "Donate author",
            "github": "Source code",
            "share-variant": "Share app",
            "shield-sun": "Dark/Light",
        }

        for icon_name, item_text in menu_items.items():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=item_text)
            )

        Clock.schedule_once(self.refresh_ui_colors, 0.2)

    def set_textfield_colors(self, field, text_c, hint_c, line_c):
        field.text_color = text_c
        field.line_color_normal = line_c
        field.line_color_focus = line_c
        field.current_hint_text_color = hint_c
        field.hint_text_color_normal = hint_c
        field.helper_text_mode = "none"

    def refresh_ui_colors(self, *args):
        toolbar = self.root.ids.toolbar
        tabs = self.root.ids.tabs
        drawer = self.root.ids.content_drawer

        if self.theme_cls.theme_style == "Dark":
            bg_tabs = [0.10, 0.10, 0.10, 1]
            fg_main = [1, 1, 1, 1]
            fg_soft = [1, 1, 1, 0.7]
            field_line = [0.35, 0.35, 0.35, 1]
        else:
            bg_tabs = [0.95, 0.95, 0.95, 1]
            fg_main = [0, 0, 0, 1]
            fg_soft = [0, 0, 0, 0.7]
            field_line = [0.25, 0.25, 0.25, 1]

        toolbar.md_bg_color = [0, 0, 0, 1] if self.theme_cls.theme_style == "Dark" else [1, 1, 1, 1]
        toolbar.specific_text_color = fg_main

        tabs.background_color = bg_tabs
        tabs.text_color_normal = fg_soft
        tabs.text_color_active = fg_main

        for lbl in tabs.get_tab_list():
            lbl.text_color_normal = fg_soft
            lbl.text_color_active = fg_main
            lbl.color = fg_soft

        drawer.ids.app_title_label.text_color = fg_main
        drawer.ids.app_author_label.text_color = fg_soft

        self.root.ids.table_label.text_color = fg_main
        self.root.ids.graph_label.text_color = fg_main
        self.root.ids.chart_label.text_color = fg_main
        self.root.ids.sum_label.text_color = fg_main

        for icon_id in ("icon_date", "icon_loan", "icon_months", "icon_interest"):
            self.root.ids[icon_id].text_color = fg_main

        self.set_textfield_colors(self.root.ids.start_date, fg_main, fg_soft, field_line)
        self.set_textfield_colors(self.root.ids.loan, fg_main, fg_soft, field_line)
        self.set_textfield_colors(self.root.ids.months, fg_main, fg_soft, field_line)
        self.set_textfield_colors(self.root.ids.interest, fg_main, fg_soft, field_line)
        self.set_textfield_colors(self.root.ids.payment_type, fg_main, fg_soft, field_line)

    def toggle_theme(self):
        self.theme_cls.theme_style = "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
        Clock.schedule_once(self.refresh_ui_colors, 0.1)

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        if self.theme_cls.theme_style == "Dark":
            normal = [1, 1, 1, 0.7]
            active = [1, 1, 1, 1]
        else:
            normal = [0, 0, 0, 0.7]
            active = [0, 0, 0, 1]

        for lbl in instance_tabs.get_tab_list():
            lbl.color = normal

        instance_tab_label.color = active

    def on_star_click(self):
        print("star clicked!")


MortgageCalculatorApp().run()