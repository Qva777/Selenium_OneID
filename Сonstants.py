class UserData:
    PHONE_NUMBER = ''
    ID_PASPORT = ""
    INN = ''
    PDF_FILE_PATH = "iman_halal_investments_2023.pdf"
    PINFL = ""
    INCREASE_CAPITAL_SUM = ""


class Selectors:
    """ Page element selectors """

    """ LOGIN """
    MOBILE_ID = '.css-3wp8qm-MuiButtonBase-root-MuiTab-root:nth-of-type(2)'
    LOGIN_INPUT_PHONE_NUMBER = '#sign-in-phone'
    SEND_SMS = '.css-64w305-MuiButtonBase-root-MuiButton-root-MuiLoadingButton-root'
    LOGIN_BIRDARCHA = 'div.AuthPage_panelButton__20oKy a.Button_wrapper--variant-blue'

    """ TASK ONE """
    ADD_FILTER = '.FilterAdd_button'
    SELECT_INN = "(//div[@class='FilterAdd_itemTitle'])[7]"
    # SELECT_INN = "//div[@class='FilterAdd_itemTitle' and text()='ИНН']"
    PRESS_ON_INN = 'div.FilterInput_buttonTitle'
    INPUT_INN = 'input#filter-input'
    THREE_POINTS = 'div.Table_content--more'
    # CONTINUE = "//div[contains(@class, 'Dropdown_menuItemTitle')"
    CONTINUE = "//div[contains(@class, 'Dropdown_menuItemTitle') and text()='Продолжить']"

    # Examples:
    # //*[contains(text()[2],'50103036180018')]
    # (//div[contains(text()[2], '50103036180018')]/ancestor::div[contains(@class, 'BusinessFounder_item')]/ancestor::div)[7]/div[contains(@class, 'ant-row')]/div[2]/button
    FIND_USER_BY_PINFL_REDUCTION = f"(//div[contains(text()[2], '{UserData.PINFL}')]/ancestor::div[contains(@class, 'BusinessFounder_item')]/ancestor::div)[7]/div[contains(@class, 'ant-row')]/div[2]/button"
    DROP_DOWN_REASON_DECREASE = 'div.ant-select'
    SELECT_MONEY_RETURN = 'div.ant-select-item[title="возврат"]'
    CURRENT_CAPITAL = "(//div[@class='Typography_wrapper Typography_wrapper--variant-primary'])[4]"
    INPUT_REDUCTION_AMOUNT = 'input#amount'
    UPLOAD_PDF = "(//input[@type='file'])[2]"
    SAVE_BUTTON = "//button[contains(@class, 'Button_wrapper--variant-blue') and contains(., 'Сохранить')]"

    """ TASK TWO """
    ADD_FOUNDER = "//div[contains(@class, 'BusinessActivity_itemTitle') and text()='Добавить учредителя']"
    SELECT_INDIVIDUAL = "//div[@class='RadioList_optionTitle' and text()='Физическое лицо']"
    CONTINUE_INDIVIDUAL = "//button[@class='Button_wrapper Button_wrapper--variant-blue']/div[@class='Button_title']"
    TYPE_OF_DOCUMENT = "//span[@class='ant-select-selection-placeholder']"
    CITIZENS_PASSPORT = "//div[@title='Паспорт гражданина Рес. Узб./ИД-карта']"
    INPUT_PASSPORT_SERIES = "//input[@id='documentNumber']"
    INPUT_PINFL = "//input[@id='pin']"
    SEARCH_PERSON = "//button[@class='Button_wrapper Button_wrapper--variant-blue Button_wrapper--block']/div[text()='Поиск']"
    NUMBER_CODE = "(//div[@class='Select_wrapper']//div[@class='ant-select-selector'])[2]"
    SELECT_NUMBER_CODE = "//div[@class='ant-select-item ant-select-item-option' and @title='91']"
    INPUT_PHONE_NUMBER_CODE = "//input[@id='mask-field']"
    INPUT_EMAIL = "//input[@id='email']"
    ADD_PERSON = "//button[@class='Button_wrapper Button_wrapper--variant-green']/div[@class='Button_title']"

    """ TASK THREE """
    # (//div[contains(text()[2], '50103036180018')]/ancestor::div[contains(@class, 'BusinessFounder_item')]/ancestor::div)[7]/div[contains(@class, 'ant-row')]/div[1]/button
    FIND_USER_BY_PINFL_INCREASE = f"(//div[contains(text()[2], '{UserData.PINFL}')]/ancestor::div[contains(@class, 'BusinessFounder_item')]/ancestor::div)[7]/div[contains(@class, 'ant-row')]/div[1]/button"
    INCREASE_CAPITAL = "//input[@id='amount']"
