def click_ID(driver, wait_time, str_path):
    """
    Clicks on an element using its ID.

    :param driver: The WebDriver instance.
    :param wait_time: The amount of time to wait for the element to be clickable.
    :param str_path: The ID of the element.
    """
    try:
        element = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.ID, str_path))
        )
        element.click()
    except TimeoutException:
        print(f"Element with ID '{str_path}' not found or not clickable.")

