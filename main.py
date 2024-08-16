from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.text import LabelBase

# Register the custom font
LabelBase.register(name='NewTimesRoman', fn_regular='NewTimesRoman.ttf')

class TaxApp(App):
    def build(self):
        return TaxLayout()

    def calculate_tax(self, instance):
        income = float(self.root.ids.income_input.text or 0)
        deductions = float(self.root.ids.deductions_input.text or 0)
        taxable_income = income - deductions

        # Sample tax calculation logic
        if taxable_income <= 250000:
            tax = 0
        elif taxable_income <= 500000:
            tax = (taxable_income - 250000) * 0.05
        elif taxable_income <= 1000000:
            tax = (taxable_income - 500000) * 0.1 + 12500
        else:
            tax = (taxable_income - 1000000) * 0.2 + 112500

        self.root.ids.result_label.text = f'Total Tax: ₹{tax:.2f}'

class TaxLayout(BoxLayout):
    pass

if __name__ == '__main__':
    TaxApp().run()
