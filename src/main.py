import os
import re

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

kivy.require("2.1.0")


class WifiPasswordApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical")
        self.label = Label(
            text="Click the button to get Wi-Fi password", font_size="20sp"
        )
        self.button = Button(text="Get Wi-Fi Password", on_press=self.get_wifi_password)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        return self.layout

    def get_wifi_password(self, instance):
        ssid, password = self.read_wifi_password()
        if ssid and password:
            self.label.text = f"SSID: {ssid}\nPassword: {password}"
        else:
            self.label.text = (
                "Could not retrieve Wi-Fi password. Make sure your device is rooted."
            )

    def read_wifi_password(self):
        # Path to the wpa_supplicant.conf file
        wifi_conf_path = "/data/misc/wifi/wpa_supplicant.conf"

        if not os.path.exists(wifi_conf_path):
            return None, None

        ssid = None
        password = None

        with open(wifi_conf_path, "r") as f:
            content = f.read()

            # Regex to find SSID and PSK (pre-shared key / password)
            ssid_match = re.search(r'ssid="([^"]+)"', content)
            password_match = re.search(r'psk="([^"]+)"', content)

            if ssid_match:
                ssid = ssid_match.group(1)
            if password_match:
                password = password_match.group(1)

        return ssid, password


if __name__ == "__main__":
    WifiPasswordApp().run()
