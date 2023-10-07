</head>
<body>


<?php 
echo '<style>
table {
    width: 100%;
    border-collapse: collapse;
}
th, td {
    border: 1px solid black;
    padding: 5px;
    text-align: left;
    min-width: 6em;  // or you can use px instead of em
}
th {
    background-color: #4CAF50;
    color: white;
}
tr:nth-child(even) {background-color: #f2f2f2;}
</style>';

$file = fopen("E:\download\interview\統計檔案\爬蟲：每日紀錄商品價格\\price2.csv", "r");

// Collect all unique dates
$dates = [];
while (($data = fgetcsv($file, 1000, ",")) !== FALSE) {
    if (!in_array($data[5], $dates)) {
        $dates[] = $data[5];
    }
}
fclose($file);

echo "<label for='dateFilter'>Filter by date:</label>";
echo "<select id='dateFilter' onchange='filterTable()'>";
echo "<option value=''>All dates</option>";
foreach ($dates as $date) {
    echo "<option value='" . htmlspecialchars($date) . "'>" . htmlspecialchars($date) . "</option>";
}
echo "</select>";

$file = fopen("E:\download\interview\統計檔案\爬蟲：每日紀錄商品價格\\price2.csv", "r");
echo "<table>";

// Process header
if (($data = fgetcsv($file, 1000, ",")) !== FALSE) {
    echo "<tr>";
    foreach ($data as $cell) {
        echo "<th>" . htmlspecialchars($cell) . "</th>";
    }
    echo "</tr>";
}

// Process rows
while (($data = fgetcsv($file, 1000, ",")) !== FALSE) {
    echo "<tr>";
    foreach ($data as $i => $cell) {
        if ($i == 6) { // change link column
            echo "<td><a href=\"" . htmlspecialchars($cell) . "\">" . htmlspecialchars($cell) . "</a></td>";
        } else {
            echo "<td>" . htmlspecialchars($cell) . "</td>";
        }
    }
    echo "</tr>";
}
echo "</table>";

fclose($file);

?>
<script>
function filterTable() {
  let select, filter, table, tr, td, i;
  select = document.getElementById('dateFilter');
  filter = select.value;
  table = document.querySelector('table');
  tr = table.getElementsByTagName('tr');

  for (i = 1; i < tr.length; i++) {
    td = tr[i].getElementsByTagName('td')[5]; // Assuming date is the first column
    if (td) {
      if (filter === '' || td.innerHTML === filter) {
        tr[i].style.display = '';
      } else {
        tr[i].style.display = 'none';
      }
    } 
  }
}
</script>








<!-- <form action='0.php' method="POST">
    <label for='name'>NAME: </label>
    <input type = 'text' id='name' name='name'>
    <br>

<input type='submit' value='submit'> -->

</form>


</body>
</head>

