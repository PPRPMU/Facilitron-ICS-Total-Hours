install_packages.sh
Script to ensure all necessary python packages are installed. Run this once the first time you clone it.

ICS-summary.py
Script for use by PPR to count the total number of hours we've used facilitron. 

NOT GOING TO WORK ON CITY WIFI

You can generate an approriate data file from sharepoint by setting up a view
for all school permits in the date range you're interested in. Once you have the view,
just export to excel and save the query as a csv. 

If you get an SSL error, you're probably on City wifi, which will break this script.
If you're not on City wifi, install the certifi package.

The script downloads ICS files from Facilitron.com reservation by reservation.
It counts each hour an ammenity is used seperately, which means if one reservation uses multiple
ammenities at the same times, it will count each of those hours seperately.


