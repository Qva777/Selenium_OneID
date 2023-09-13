class UserData:
    PHONE_NUMBER = ''
    INN = ''


class Selectors:
    MOBILE_ID = '.css-3wp8qm-MuiButtonBase-root-MuiTab-root:nth-of-type(2)'
    INPUT_PHONE_NUMBER = '#sign-in-phone'
    SEND_SMS = '.css-64w305-MuiButtonBase-root-MuiButton-root-MuiLoadingButton-root'
    HAS_ENTERED = 'div.Profile_name'
    LOGIN_BIRDARCHA = 'div.AuthPage_panelButton__20oKy'
    ADD_FILTER = '.FilterAdd_button'
    SELECT_INN = "(//div[@class='FilterAdd_itemTitle'])[7]"
    # INN = "//div[@class='FilterAdd_itemTitle' and text()='ИНН']"
    PRESS_ON_INN = 'div.FilterInput_buttonTitle'
    INPUT_INN = 'input#filter-input'
    THREE_POINTS = 'div.Table_content--more'
    CONTINUE = "//div[contains(@class, 'Dropdown_menuItemTitle')"
    # CONTINUE = "//div[contains(@class, 'Dropdown_menuItemTitle') and text()='Продолжить']"




