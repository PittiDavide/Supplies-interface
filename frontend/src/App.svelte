<script>
  //get supplier list from backend
  import { onMount } from "svelte";
  import { array } from "./store.js";

  let material = "";
  let quantity = 0;
  let date = new Date();
  let price = 0;
  let show = false;

  onMount(async () => {
    const response = await fetch("/suppliers");
    const data = await response.json();
    console.log($array.length);
    //array.set(data);
  });

  //search function to filter supplier list and create the table
  async function search() {
    try {
      console.log(date.length);
      if (material == "" || quantity == 0 || date.length != 10) {
        alert("Please fill all the fields");
        show = false;
        return;
      }
    } catch (error) {
      console.log(error);
    }
    const response = await fetch(
      "/search/" + material + "/" + quantity + "/" + date
    );
    const data = await response.json();
    console.log(data);
    array.set(data);
    show = true;
  }
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
    input[type="number"] {
      padding: 10px;
      font-size: 16px;
      border-radius: 5px;
      border: none;
      width: 80%;
      margin-bottom: 10px;
    }
    button {
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
      overflow-x: auto;
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
      bind:value={material}
    /><br />

    <label for="quantity">Quantity:</label>
    <input
      type="number"
      id="quantity"
      name="quantity"
      placeholder="Enter quantity"
      bind:value={quantity}
    /><br />

    <label for="date">Date:</label>
    <input type="date" id="date" name="date" bind:value={date} /><br />

    <button on:click={search}>search</button>
  </form>
  <div class="supplier">
    <h2>Supplier List</h2>
    <table>
      <thead>
        <tr>
          <th>Supplier Name</th>
          <th>Email</th>
          <th>Goods</th>
          <th>Inizial Price</th>
          <th>Quantity</th>
          <th>Quantity Discover</th>
          <th>Value Discover</th>
          <th>Date Discover</th>
          <th> Delivery Time</th>
          <th>Total Price</th>
        </tr>
      </thead>
      <tbody>
        {#each $array as supplier}
          <tr>
            <td>{supplier.name_s}</td>
            <td>{supplier.address}</td>
            <td>{supplier.name_g}</td>
            <td>{(price = supplier.price * quantity)}</td>
            <td>{supplier.quantity}</td>
            <td>{supplier.quantity_discount}</td>
            <td>{supplier.value_discount}</td>
            <td>{supplier.date_discount}</td>
            <td>{supplier.delivery_time} days</td>
            <td>{supplier.total_price}</td>
          </tr>
        {/each}
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
