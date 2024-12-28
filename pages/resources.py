from selene import browser, have, be

import allure
from pages.allure_labels import dynamic_labels


class Contact_form:

    @allure.step("Fill contact form valid data")
    def steps(self, value):
       dynamic_labels()
       browser.config.timeout = 60
       with allure.step("Open brwser"):
           browser.open('https://www.takamul.net.sa/')
           browser.driver.fullscreen_window()
       with allure.step("Fill FNAME"):
           browser.element('[id="mce-FNAME"]').type(value.first_name)
       with allure.step("Fill email"):
           browser.element('[id="email"]').type(value.email)
       with allure.step("Fill message"):
           browser.element('[id="mce-MMERGE6"]').type(value.message)
       browser.element('[class="self-start btn"]').click()
       with allure.step("Submit_success"):
           browser.element('[class="p-3 text-sm border border-Blue/50 bg-Blue/20"]').should(have.text('Thank you! We have received your message.'))

    @allure.step("Fill contact form not valid data")
    def steps_negative(self, value):
       dynamic_labels()
       browser.config.timeout = 12
       with allure.step("Open brwser"):
           browser.open('https://www.takamul.net.sa/')
           browser.driver.fullscreen_window()
       with allure.step("Fill FNAME"):
           browser.element('[id="mce-FNAME"]').type(value.first_name)
       with allure.step("Fill email"):
           browser.element('[id="email"]').type(value.not_email)
       with allure.step("Fill message"):
           browser.element('[id="mce-MMERGE6"]').type(value.message)
       browser.element('[class="self-start btn"]').click()
       with allure.step("Submit_failed"):
           browser.element('[class="p-3 text-sm border border-Blue/50 bg-Blue/20"]').should(have.text('Please enter the correct email.'))

class Digitalproject_buttons:

    @allure.step("Check path and buttons")
    def steps(self, value):
       dynamic_labels()
       browser.config.timeout = 12
       with allure.step("Open brwser"):
           browser.open('https://www.takamul.net.sa/')
           browser.driver.fullscreen_window()
       with allure.step('Check drop down "Services"'):
           browser.element('[id="headlessui-menu-button-:r0:"]').click()
           browser.element('[id="headlessui-menu-item-:r5:"]').click()
       with allure.step('Check "Digital Strategy" link'):
           browser.element('[href="/services/digital-experience/digital-strategy"]').click()
       with allure.step('Check "Digital Projects" buttons'):
           browser.element('[id="headlessui-tabs-tab-:rc:"]').click()
           browser.element('[id="headlessui-tabs-panel-:r3:"]').should(have.text('1 The digital tools, apps'))
           browser.element('[id="headlessui-tabs-tab-:rd:"]').click()
           browser.element('[id="headlessui-tabs-panel-:r4:"]').should(have.text('2 The digital tools, apps'))
           browser.element('[id="headlessui-tabs-tab-:re:"]').click()
           browser.element('[id="headlessui-tabs-panel-:r5:"]').should(have.text('3 The digital tools, apps'))
           browser.element('[id="headlessui-tabs-tab-:rf:"]').click()
           browser.element('[id="headlessui-tabs-panel-:r6:"]').should(have.text('4 The digital tools, apps'))
           browser.element('[id="headlessui-tabs-tab-:rg:"]').click()
           browser.element('[id="headlessui-tabs-panel-:r7:"]').should(have.text('5 The digital tools, apps'))
           browser.element('[id="headlessui-tabs-tab-:rh:"]').click()
           browser.element('[id="headlessui-tabs-panel-:r8:"]').should(have.text('6 The digital tools, apps'))
           browser.element('[id="headlessui-tabs-tab-:ri:"]').click()
           browser.element('[id="headlessui-tabs-panel-:r9:"]').should(have.text('7 The digital tools, apps'))
           browser.element('[id="headlessui-tabs-tab-:rj:"]').click()
           browser.element('[id="headlessui-tabs-panel-:ra:"]').should(have.text('8 The digital tools, apps'))
           browser.element('[id="headlessui-tabs-tab-:rk:"]').click()
           browser.element('[id="headlessui-tabs-panel-:rb:"]').should(have.text('9 The digital tools, apps'))