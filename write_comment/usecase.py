firstError.click()
commentField.send_keys("A new comment!")
authorField.send_keys("The Tests")
commentButton.click()

firstMissing.click()
commentField.clear()
commentField.send_keys("Why is this missing?")
commentButton.click()

# Show the tooltip
commentMarker1.click()
quit()
