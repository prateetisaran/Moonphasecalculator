# Moon Phase Calculator

The moon phase calculator is a program that operates on a few base calculations, and then applies the calculations into different contexts to create a user-friendly interface

## The calculations
The calculations are present in two base functions in the program (converttojulian and datetophase) 

#### Converttojulian 
Julian dates are a date system that express a date in terms of the number of days after January 1, 4713 BC 12pm. 
I decided to convert all the dates into Julian dates since it is much easier to use for more complex calcultations.  
This function inputs 3 integer variables, the date, month and year. It then performs a series of calculations (Lines 3 to 8) 
To then determine the julian date of the date input. This calcualation does not consider the time, and the decimal part of a julian date represents the time. So the decimal part on the value returned is negligible and does not represent much. 
Since the time on the original date was 12:00 from which the dates are calculated, a number ending in 0 decimal places would represent 12:00pm on a given day. 
However, for this calculation, the duration of the entire day needs to be considered, so I had taken the integer part of the result value and then subtracted 0.5 from it. 
Now, the value returned is the julian date representing 00:00 on the particular date. 

#### Datetophase
Date to phase is the core of the program that converts any given julian date and returns the lunar phase on that day. This function is used everywhere to produce different kinds of values. 
Firstly, in line 28 it calculates the number of days since a given julian date where there was a full moon. 
(I calculated this date with the information given in the pdf. Since a new moon happened on 1/6/2000 at 12:24:01, and the length of a lunar month is 29.54 days, I was able to calculate the earliest new moon in the julian date period.)  
After the number of days since is calculated, I divided that value by 29.54 to get the number of lunar months that have happened since that date. 
Line 20 calculates the date of the last new moon using this information. The decimal part of the previous value is ignored, and the remaining is multiplied by the 29.54(the duration of a lunar month) and then added to the date of the first new moon to obtain the date of the last new moon before the given date. 
The dates of the 4 major phases are calculated by dividing 29.54 by 4 and then adding that value repeatedly. 
New Moon, Full Moon, First Quarter and Third Quarter are such phases that theoretically only exist perfectly for a moment.
The results obtained now show the (near) exact moment when these 4 phases will occur. 
The next 4 if statements determine if any of these phases have occured anytime in the 24 hour duration of the date specified. 
If not: 
The other four phases: Waning Gibbous, Waning Crescent, Waxing Gibbous and Waxing crescent all are interim phsaes that exist for the entire time between moments when the 4 major phases happen. 
The next four if statements determine what major phases have happened before and after the given date to then determine what interim phase is happening for the duration of the day. 

## The GUI
These two base calculations are established, and then used in different ways for better user interface. 
I divided the GUI Application into three parts that perform three different functions: 

#### Specific Date
This is the simplest one that lets the user input a date (using the calendar Tkinter widget), and the lunar phase for this specific date is then calculated using the above calculations and then displayed in a label, and the corresponding image is also displayed. 

#### Today 
This one also performs the same calculations, but it uses the datetime library to automatically input the current date and perform the calculations and display the result. This one does not require any user input, and displays as soon as it is opened. 

#### When Next
The calculation for this one is slightly different from the base calculations. It essentially does the same thing until the dates of the four major phases are calculated. After that, if the user clicks the full moon button, the difference between the date of the full moon and the current date is calculated, if the date of the new moon is before the current date, it adds 29.54 to that to find the date of the next full moon. The difference between the current date and the next full moon is calculated, then using timedelta, added to the current date and the result is displayed.
The same thing is done for the new moon. The user can see when the next full moon and new moon are. 

