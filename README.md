# Google Trend Analysis
This script shows the most popular search terms for specific languages, regions and years. They are arranged chronologically based on the month of highest relative popularity. 

## Options
<table>
    <tr>
        <td>--year</td>
        <td>Year to display top trends. </td>
    </tr>
    <tr>
        <td>--language</td>
        <td>Language of the search terms. For example 'en' or 'de'. </td>
    </tr>
    <tr>
        <td>--region</td>
        <td>Country and state/province. For example 'US-AL' for Alabama. The state/province are not mandatory. </td>
    </tr>
</table>

## Dependencies
* __pytrends__ is used to get the information
* __matplotlib__ is used to generate the plot
* __PyQT5__ is sometimes required to run on Windows machines

## Example
Let's display the most popular _german_ search terms in _Switzerland_ for the year _2020_: 
```
python toptrends.py --year 2020 --language de --region CH
```

The result should look like this: 
![example_trends](example.png)