# phishing-page-flooder
This will enable you to flood any phishing pages that you may encounter with fake usernames and passwords which you can customize to your liking.  

**HOW TO USE**:
  1. Find phishing page.
  2. Open dev tools / inspect page.
  3. Open Network tab on dev tools and filter so you only see `Fetch/XHR`.
  4. At the top, click on preserve log if the page redirects you upon login.
  5. Submit a fake form to find out the following:
  6. There should be something related to "post" or similar.
  7. Click on `Headers` tab at the top, input Request URL into the program. 
  8. Click on that item and find the `Form Data` header, usually next to `Headers` tab.
  9. Input username and passwords field_name into their respective fields in the program.
  10. Specify number of threads you want to run the program.
  11. If you want a preview of what is happening, input "Y" to the respective prompt to enable mock mode. Input "N" to do it for real.
  
 
 **TO CUSTOMIZE POTENTIAL USERNAMES AND PASSWORDS:**

 Just append to the .txt documents present in the main file
 
 
 
 Ensure all the files downloaded are in the same folder
