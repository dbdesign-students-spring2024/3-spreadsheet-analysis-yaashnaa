# Spreadsheet Analysis
# Data Set Details

## Origin of Data Set
The data set used in this analysis originates from [NYU libraries](https://guides.nyu.edu/c.php?g=276966&p=1846654). It provides information about citibike data including the trip duration, start time, station ID, station name and longitude, as well as the stop time, station ID, name and longitude. It also informs us about the bike ID, user type, birth year, and gender.


## Format of Original Data File
The original data file was in [CSV] format. There were a total of 9758 rows and 15 columns. 

## Raw Data Display
Here are the first 20 rows of the raw data:

| Trip Duration | Start Time           | Stop Time            | Start Station ID | Start Station Name    | Start Station Latitude | Start Station Longitude | End Station ID | End Station Name       | End Station Latitude | End Station Longitude | Bike ID | User Type   | Birth Year | Gender |
|---------------|----------------------|----------------------|------------------|-----------------------|------------------------|-------------------------|-----------------|------------------------|-----------------------|------------------------|---------|-------------|------------|--------|
| 165           | 2016-08-01 00:09:40  | 2016-08-01 00:12:25  | 3270             | Jersey & 6th St       | 40.72528910781132      | -74.04557168483734      | 3273            | Manila & 1st           | 40.721650724879986   | -74.04288411140442    | 24679   | Subscriber  | 1968       | 1      |
| 705           | 2016-08-01 01:45:08  | 2016-08-01 01:56:53  | 3186             | Grove St PATH         | 40.71958611647166      | -74.04311746358871      | 3206            | Hilltop                | 40.7311689            | -74.0575736           | 24530   | Subscriber  | 1978       | 1      |
| 854           | 2016-08-01 02:22:26  | 2016-08-01 02:36:41  | 3183             | Exchange Place        | 40.7162469             | -74.0334588             | 3190            | Garfield Ave Station   | 40.7104670233797     | -74.07003879547119    | 24649   | Subscriber  | 1988       | 1      |
| 211           | 2016-08-01 03:05:10  | 2016-08-01 03:08:41  | 3194             | McGinley Square       | 40.7253399253558       | -74.06762212514877      | 3195            | Sip Ave                | 40.73074262530658    | -74.06378388404846    | 24624   | Subscriber  | 1986       | 1      |
| 506           | 2016-08-01 03:25:42  | 2016-08-01 03:34:09  | 3195             | Sip Ave               | 40.73074262530658      | -74.06378388404846      | 3193            | Lincoln Park           | 40.7246050998869     | -74.07840594649315    | 24624   | Subscriber  | 1986       | 1      |
| 132           | 2016-08-01 04:17:50  | 2016-08-01 04:20:03  | 3213             | Van Vorst Park        | 40.71848892            | -74.047726625           | 3186            | Grove St PATH          | 40.71958611647166    | -74.04311746358871    | 24663   | Subscriber  | 1965       | 1      |
| 172           | 2016-08-01 04:41:49  | 2016-08-01 04:44:41  | 3279             | Dixon Mills           | 40.721630142638354     | -74.04996782541275      | 3186            | Grove St PATH          | 40.71958611647166    | -74.04311746358871    | 24559   | Subscriber  | 1982       | 1      |
| 776           | 2016-08-01 05:14:20  | 2016-08-01 05:27:17  | 3207             | Oakland Ave           | 40.7376037             | -74.0524783             | 3276            | Marin Light Rail       | 40.71458403535893    | -74.04281705617905    | 24532   | Subscriber  | 1984       | 2      |
| 629           | 2016-08-01 05:18:08  | 2016-08-01 05:28:37  | 3212             | Christ Hospital       | 40.734785818           | -74.050443636           | 3195            | Sip Ave                | 40.73074262530658    | -74.06378388404846    | 24561   | Subscriber  | 1965       | 1      |
| 325           | 2016-08-01 05:20:48  | 2016-08-01 05:26:13  | 3207             | Oakland Ave           | 40.7376037             | -74.0524783             | 3195            | Sip Ave                | 40.73074262530658    | -74.06378388404846    | 24721   | Subscriber  | 1958       | 1      |
| 461           | 2016-08-01 05:39:37  | 2016-08-01 05:47:18  | 3225             | Baldwin at Montgomery | 40.7236589             | -74.0641943             | 3186            | Grove St PATH          | 40.71958611647166    | -74.04311746358871    | 24470   | Subscriber  | 1977       | 1      |
| 2673          | 2016-08-01 05:40:13  | 2016-08-01 06:24:46  | 3213             | Van Vorst Park        | 40.71848892            | -74.047726625           | 3213            | Van Vorst Park         | 40.71848892            | -74.047726625          | 24562   | Subscriber  | 1969       | 1      |
| 185           | 2016-08-01 05:52:04  | 2016-08-01 05:55:09  | 3267             | Morris Canal          | 40.7124188237569      | -74.03852552175522      | 3184            | Paulus Hook            | 40.7141454            | -74.0335519           | 24456   | Subscriber  | 1961       | 1      |
| 373           | 2016-08-01 05:53:41  | 2016-08-01 05:59:54  | 3187             | Warren St             | 40.7211236             | -74.03805095            | 3203            | Hamilton Park          | 40.727595966          | -74.044247311         | 24413   | Subscriber  | 1985       | 2      |
| 2047          | 2016-08-01 05:54:07  | 2016-08-01 06:28:14  | 3192             | Liberty Light Rail    | 40.7112423             | -74.0557013             | 3192            | Liberty Light Rail     | 40.7112423            | -74.0557013           | 24641   | Subscriber  | 1986       | 2      |
| 215           | 2016-08-01 05:57:15  | 2016-08-01 06:00:51  | 3267             | Morris Canal          | 40.7124188237569      | -74.03852552175522      | 3183            | Exchange Place         | 40.7162469            | -74.0334588           | 24612   | Subscriber  | 1974       | 1      |
| 319           | 2016-08-01 06:06:32  | 2016-08-01 06:11:52  | 3207             | Oakland Ave           | 40.7376037             | -74.0524783             | 3195            | Sip Ave                | 40.73074262530658    | -74.06378388404846    | 24551   | Subscriber  | 1977       | 1      |
| 259           | 2016-08-01 06:06:41  | 2016-08-01 06:11:00  | 3225             | Baldwin at Montgomery | 40.7236589             | -74.0641943             | 3195            | Sip Ave                | 40.73074262530658    | -74.06378388404846    | 24419   | Subscriber  | 1987       | 1      |
| 269           | 2016-08-01 06:06:46  | 2016-08-01 06:11:16  | 3186             | Grove St PATH         | 40.71958611647166      | -74.04311746358871      | 3278            | Monmouth and 6th       | 40.72568548362901    | -74.04879033565521    | 24559   | Subscriber  | 1985       | 2      |


# Data Scrubbing Details
 #### I only used python and the CSV model for scrubbing
1.  Removed any rows with missing values (indicated by a blank space) from all columns. This helped organise the data more clearly. 
2. Organised the data into seperate columns with appropriate space so that excel could import the values correctly by calculating the column widths needed for each column. 
   ```python 
   def format_and_write(data, output_file_path):
    # Extract column headings from the first row
    column_headings = data[0]

    # Calculate the maximum width for each column
    column_widths = calculate_column_widths(data)

    # Write the formatted data to a new CSV file
    with open(output_file_path, 'w', newline='') as output_file:
        # Use a tab '\t' as the delimiter
        writer = csv.writer(output_file, delimiter='\t')

        # Write the column headings
        formatted_headings = [f"{heading:<{width+1}}" for heading, width in zip(column_headings, column_widths)]
        writer.writerow(formatted_headings)

        # Write the formatted data
        for row in data[1:]:
            formatted_row = [f"{str(cell):<{width+1}}" for cell, width in zip(row, column_widths)]
            writer.writerow(formatted_row)
   
## Problems in the Original Data
 - **Problem 1:** The raw data I accquired was quite confusing to read, with only commas seprating the heading and values, it was hard to tell which value belonged in which column. I particularly had problem with the start and stop time (2016-08-01 00:09:40,2016-08-01 00:12:25)
 - **Problem 2:** There were some missing values which made the dataset more confusing to read. 
 - **Problem 3:** The dataset was very large and was slowing down my computer quite a lot, therefore I had to minimise the amount of data I analysed. 

# Links 
- [Raw data](/data/raw_data.csv)
- [Clean data](/data/clean_data.csv)
- [Spreadhseet](/data/spreadsheet.xlsx)

# Analysis 

## Aggregate statistics 

1. I first calculated the average, total, minimum, and maximum values for each column to get a quick overview of the dataset. The average was calculate using the (AVERAGE) formula, the total was calculated using the (SUM) formula, the shortest ride was calculate using the (MIN) formula, and the maximum was calulated using (MAX) formula. I also converted the trip duration and all statistics into minutes for easier understanding.

2. I then calculated the same statistics but only for users who were subscriber instead of customers.The average was calculate using the (AVERAGEIF) formula, the total was calculated using the (SUMIF) formula, the shortest ride was calculate using the (MINIF) formula, and the maximum was calulated using (MAXIF) formula.

3. I also calculated the age of the riders from the birth year in the original data, and used this data to calculate the average age of the rider, the oldest rider and the youngest rider. These were done by using the (AVERAGE), (MAX), and (MIN) formulas respectively. The youngest rider was older than I expected but it is important to remember that this was an edited dataset and therefore does not reflect the actual values from the original. 

4. For all of the analysis I used the (ROUNDDOWN) formula to  remove any decimal places that may have been added by Excel when calculating the values. 

5. Multiple pivot tables were used for further analysis:
   ### Table 1
      This lists the end station names as well as the sum of the trip duration to these stations. The trip duration is displayed in seconds as well as minutes. 
      | End Station Name     | Sum of Trip Duration | Sum of Trip duration in minutes |
      |-----------------------|----------------------|---------------------------------|
      | Exchange Place        | 672526               | 10729                           |
      | Grove St PATH         | 634249               | 9917                            |
      | Liberty Light Rail    | 470550               | 7718                            |
      | Newport Pkwy          | 403024               | 6547                            |
      | Hamilton Park         | 385408               | 6134                            |
      | Newport PATH          | 384578               | 6131                            |
      | Morris Canal          | 358263               | 5795                            |
      | Paulus Hook           | 314091               | 5073                            |
      | Jersey & 3rd          | 285475               | 4670                            |
      | Sip Ave               | 280560               | 4413                            |
      | Marin Light Rail      | 248535               | 4008                            |
      | Essex Light Rail      | 242664               | 3904                            |
      | Newark Ave            | 241501               | 3897                            |
      | Warren St             | 216395               | 3460                            |
      | Lafayette Park        | 194097               | 3213                            |
      | JC Medical Center     | 189174               | 3072                            |
      | City Hall             | 176599               | 2802                            |
      | Van Vorst Park        | 170922               | 2719                            |
      | Lincoln Park          | 150288               | 2423                            |
      | Brunswick St          | 147203               | 2323                            |

   ### Table 2
      This table calculated the average age for the riders who are subscriber and customers. It also calulated the average age of both of them combined. The blank space indicates the average for those who didn't have the data available.
      | User Type   | Average Age of Rider |
      |-------------|----------------------|
      | Subscriber  | 44.38777815          |
      | Customer    | 40.18518519          |
      |             | 37                   |
      | Grand Total | 44.37084975          |
   ### Table 3
      This table provides the sum of the trip duration by the subscribers and customers. It also calulated the sum for both of them combined. The blank space indicates the sum for those who didn't have the data available.
      | User Type   | Sum of Trip Duration |
      |-------------|----------------------|
      | Subscriber  | 5951106              |
      | Customer    | 1801139              |
      |             | 4604                 |
      | Grand Total | 7756849              |

6. 2 charts were used for analysis:
   ### Bar chart 
      The bar chart indicates the age of the subscribers, customers and the users who didn't have the data available.
      ![Bar chart](/images/chart.png)
   ### Pie chart
   The pie chart shows the ratio of subscribers to customers. 
      ![Pie chart](/images/pie.png)

## Extra-credit
I believe I deserve extra credit because I used a large dataset comprising of 9758 rows and 15 columns. I also converted the appropriate values from seconds to minutes, calculated the birth year and did further analysis on it. I also used multiple pivot tables and charts. 
