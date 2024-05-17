def change_on_last_tab(driver):
    """Switch to the last tab in the current window."""

    driver.switch_to.window(driver.window_handles[-1])

