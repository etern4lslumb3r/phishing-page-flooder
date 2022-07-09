# phishing-page-flooder
This will enable you to flood any phishing pages that you may encounter with fake usernames and passwords which you can customize to your liking.  

**BEFORE USING**
    Make sure to open the .exe file in the folder it was placed in or there will be errors.
    Disclaimer:
      According to virustotal.com, there is a positive flag for there being a virus in this executable. I assure you that this is a false positive
      caused by the fact that the executable being compiled using the pyinstall python library. There are many cases online indicating that there are cases such as this.

**HOW TO USE**:
  1. Find phishing page.
  2. Open dev tools / inspect page.
  3. Open `Network` tab on dev tools and filter such that you only see `Fetch/XHR`.
  4. At the top, check on `Preserve Log` if the page redirects you upon login.
  5. Submit a form to find out the following:
  6. There should be a network request with the name related to "post" or similar. Click it.
  7. Click on `Headers` tab at the top, input `Request URL` into the program. 
  8. Click on `Payload` tab next to `Headers`. Look for where your inputs in Step 5 went.
  9. Input the name of the user and pass fields into their respective fields in the program.
  10. Specify number of threads you want to run the program. More threads = faster sends
  11. If you want a preview of what is happening, input "Y" to the respective prompt to enable mock mode. Input "N" to do it for real.
  
 
 **TO CUSTOMIZE POTENTIAL USERNAMES AND PASSWORDS:**

 Just append to the .txt documents present in the main file
 Make sure each instance of a name, adjective, or password is separated by line.
 
