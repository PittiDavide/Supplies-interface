<script>
  export let name;
</script>

<head>
  <title>Search for Suppliers</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #ededed;
    }
    header {
      background-color: #003366;
      color: #fff;
      padding: 10px;
      text-align: center;
      font-size: 28px;
      font-weight: bold;
    }
    form {
      background-color: #fff;
      padding: 20px;
      margin: 20px auto;
      width: 50%;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    }
    input[type="text"] {
      padding: 10px;
      font-size: 16px;
      border-radius: 5px;
      border: none;
      width: 80%;
      margin-bottom: 10px;
    }
    input[type="submit"] {
      padding: 10px;
      background-color: #003366;
      color: #fff;
      font-size: 16px;
      border-radius: 5px;
      border: none;
      cursor: pointer;
      width: 20%;
    }
    .supplier {
      background-color: #fff;
      padding: 20px;
      margin: 20px auto;
      width: 50%;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
      display: none;
    }
    .supplier h2 {
      font-size: 24px;
      font-weight: bold;
      margin-top: 0;
    }
    .supplier table {
      border-collapse: collapse;
      width: 100%;
      margin-top: 20px;
    }
    .supplier th,
    .supplier td {
      padding: 10px;
      text-align: left;
      border-bottom: 1px solid #ededed;
    }
    .supplier th {
      background-color: #003366;
      color: #fff;
    }
  </style>
</head>
<body>
  <header>Search for Suppliers</header>
  <form>
    <label for="material">Material:</label>
    <input
      type="text"
      id="material"
      name="material"
      placeholder="Enter material name"
    /><br />

    <label for="quantity">Quantity:</label>
    <input
      type="text"
      id="quantity"
      name="quantity"
      placeholder="Enter quantity"
    /><br />

    <input type="submit" value="Search" />
  </form>

  <div class="supplier">
    <h2>Supplier List</h2>
    <table>
      <thead>
        <tr>
          <th>Supplier Name</th>
          <th>Contact Person</th>
          <th>Contact Number</th>
          <th>Email</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Supplier 1</td>
          <td>John Doe</td>
          <td>123-456-7890</td>
          <td>john.doe@supplier1.com</td>
        </tr>
        <tr>
          <td>Supplier 2</td>
          <td>Jane Doe</td>
          <td>123-456-7890</td>
          <td>jane.doe@supplier2.com</td>
        </tr>
        <tr>
          <td>Supplier 3</td>
          <td>Bob Smith</td>
          <td>123-456-7890</td>
          <td>bob.smith@supplier3.com</td>
        </tr>
      </tbody>
    </table>
  </div>

  <script>
    const form = document.querySelector("form");
    const supplierList = document.querySelector(".supplier");

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      supplierList.style.display = "block";
    });
  </script>
</body>
