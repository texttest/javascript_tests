allLink25Jan2006.click()
sleep(6)

addComment25Jan2006.click()
commentField.send_keys("A general comment!")
authorField.send_keys("The Scrum Master")
commentButton.click()

testComment2_25Jan2006Edit.click()
commentField.send_keys("How would I know?")
commentButton.click()

# Delete appears not to work, causes problems in the main page
testComment1_25Jan2006Delete.click()

sleep(2)
accept_alert()
sleep(2)
describe()

back()

sleep(4)
# Show the tooltip
commentMarker2.click()
print "Main window again:"
describe()
quit()
