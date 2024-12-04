from bs4 import BeautifulSoup
from collections import Counter

html_file= """
<html>
<head>
<title>Our Python Class exam</title>

<style type="text/css">
    
    body{
        width:1000px;
        margin: auto;
    }
    table,tr,td{
        border:solid;
        padding: 5px;
    }
    table{
        border-collapse: collapse;
        width:100%;
    }
    h3{
        font-size: 25px;
        color:green;
        text-align: center;
        margin-top: 100px;
    }
    p{
        font-size: 18px;
        font-weight: bold;
    }
</style>

</head>
<body>
<h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
<table>
    
    <thead>
        <th>DAY</th><th>COLOURS</th>
    </thead>
    <tbody>
    <tr>
        <td>MONDAY</td>
        <td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
    </tr>
    <tr>
        <td>TUESDAY</td>
        <td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
    </tr>
    <tr>
        <td>WEDNESDAY</td>
        <td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
    </tr>
    <tr>
        <td>THURSDAY</td>
        <td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
    </tr>
    <tr>
        <td>FRIDAY</td>
        <td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
    </tr>

    </tbody>
</table>

<p>Examine the sequence below very well, you will discover that for every 1s that appear 3 times, the output will be one, otherwise the output will be 0.</p>
<p>0101101011101011011101101000111 <span style="color:orange;">Input</span></p>
<p>0000000000100000000100000000001 <span style="color:orange;">Output</span></p>
<p>
</body>
</html>
"""


data = BeautifulSoup(html_file, 'html.parser')

rows = data.find_all('tr')

list_colours = []
for row in rows:
    cols = row.find_all('td')
    if len(cols) > 1:
        colours = cols[1].text.strip()
        list_colours.extend(colours.split(', '))

corrected_colours = [colour.strip().upper() for colour in list_colours]
colour_count = Counter(corrected_colours)


print(" The colour analysis:")
for colour, count in colour_count.most_common():
    print(f"{colour}:{count} occurrence")

top_colours = colour_count.most_common(3)
print("\n Assummed colour for the shirt")

for colour, count in top_colours:
    print (f"{colour}(This is based on {count} occurence)")